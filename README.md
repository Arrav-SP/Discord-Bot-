# Discord-Bot-
Discord Bot for GDSC

Discord Bot with Chat, Polls, Reminders, and Music Functionality

Overview-
This Discord bot is designed to enhance server engagement by providing AI-powered chat responses, poll creation, reminder management, and music playback functionality. Additionally, it includes advanced features such as AI-powered message summaries, custom welcome messages, and an efficient music queue system.

Features-
A)AI Chatbot

1)Responds to user messages using the Gemini API.
2)Provides meaningful and context-aware responses.

B)Reminders
1)Users can set reminders using a specific format (e.g., !remind me to "Meeting at 5PM" on 2025-03-10).
2)The bot stores and triggers reminders at the specified time.
3)Users can delete and modify reminders.

C)Polls
1)Users can create polls using a command format (e.g., !poll "Best programming language?" "Python, Java, C++").
2)The bot collects and displays votes.

D)Additional Features
1)AI-Powered Summaries
2)Users can request a summary of long messages or discussions using !summarize <message>.
3)Custom Welcome Messages
4)Greets new members with a customizable welcome message.

E)Music Queue System
1)Allows users to queue and play songs in a voice channel.
2)Supports basic playback controls such as play, pause, skip, and stop.
3)Auto-Delete Expired Reminders
4)Keeps the system clean by removing past reminders.

Technology Stack

Programming Language: Python

Libraries Used:

1)discord.py for bot interactions

2)google-generativeai for Gemini API integration

3)sqlite3 for storing reminders and polls

4)youtube-dl and FFmpeg for music playback

5)asyncio for asynchronous task management

Setup Instructions

Clone the Repository

git clone https://github.com/your-repo/discord-bot.git
cd discord-bot

Install Dependencies
1)pip install discord.py google-generativeai youtube-dl ffmpeg asyncio
2)Set Up API Keys
3)Obtain a Discord bot token from the Discord Developer Portal
4)Get a Gemini API key from Google AI services
5)Store them in a .env file:
6)DISCORD_TOKEN=your_discord_bot_token
GEMINI_API_KEY=your_gemini_api_key
7)Run the Bot--->python bot.py

Usage Guide
1)Chat with the bot: Mention the bot or use !ask <message>.
2)Set a reminder: !remind me to "task" on YYYY-MM-DD HH:MM.
3)Create a poll: !poll "question" "option1, option2, option3".
4)Play music: !play <song name or URL>.
5)Summarize text: !summarize <message>.
6)Future Enhancements
    a)Integrate more AI-driven responses.
    b)Implement better music playback controls.
    c)Provide more customization options for polls and reminders.

This bot serves as an interactive and functional addition to any Discord server, enhancing engagement and productivity.

