import discord
import os
import google.generativeai as genai
import asyncio
import sqlite3
from discord.ext import commands, tasks
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

# Initialize the bot
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Database setup
conn = sqlite3.connect("bot_data.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS reminders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    message TEXT,
    reminder_time TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS polls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    options TEXT,
    votes TEXT
)
""")
conn.commit()

# AI Chat Response
def get_ai_response(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    check_reminders.start()

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="general")
    if channel:
        await channel.send(f"Welcome {member.mention} to {member.guild.name}! 🎉")

@bot.command()
async def ask(ctx, *, question):
    response = get_ai_response(question)
    await ctx.send(response)

# Reminder functionality
@bot.command()
async def remind(ctx, time: str, *, message: str):
    reminder_time = datetime.strptime(time, "%Y-%m-%d %H:%M")
    cursor.execute("INSERT INTO reminders (user_id, message, reminder_time) VALUES (?, ?, ?)",
                   (ctx.author.id, message, reminder_time.strftime("%Y-%m-%d %H:%M")))
    conn.commit()
    await ctx.send(f"Reminder set for {reminder_time}!")

@tasks.loop(minutes=1)
async def check_reminders():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    cursor.execute("SELECT id, user_id, message FROM reminders WHERE reminder_time = ?", (now,))
    reminders = cursor.fetchall()
    for r in reminders:
        user = await bot.fetch_user(r[1])
        await user.send(f"Reminder: {r[2]}")
        cursor.execute("DELETE FROM reminders WHERE id = ?", (r[0],))
    conn.commit()

# Poll functionality
@bot.command()
async def poll(ctx, question: str, *, options: str):
    option_list = options.split(", ")
    embed = discord.Embed(title=question, color=discord.Color.blue())
    reactions = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
    for i, option in enumerate(option_list[:5]):
        embed.add_field(name=reactions[i], value=option, inline=False)
    poll_message = await ctx.send(embed=embed)
    for i in range(len(option_list[:5])):
        await poll_message.add_reaction(reactions[i])

# AI Summarization
@bot.command()
async def summarize(ctx, *, text: str):
    summary = get_ai_response(f"Summarize this: {text}")
    await ctx.send(summary)

# Music functionality
@bot.command()
async def play(ctx, url: str):
    if ctx.author.voice is None:
        await ctx.send("You need to be in a voice channel!")
        return
    voice_channel = ctx.author.voice.channel
    vc = await voice_channel.connect()
    vc.play(discord.FFmpegPCMAudio(url))
    while vc.is_playing():
        await asyncio.sleep(1)
    await vc.disconnect()

bot.run(TOKEN)
