#!/usr/bin/env python3 
import discord
from discord.ext import tasks, commands
import feedparser
import asyncio
from dotenv import dotenv_values
# ====== CONFIGURATION ======
config = dotenv_values(".env")  # Your bot token from the Discord Dev Portal

TOKEN = config["TOKEN"]
CHANNEL_ID = 1317898361185243146


CHANNEL_URL = "https://www.youtube.com/feeds/videos.xml?channel_id=UCz2_M6-NBgdiLvDOmlH074g"

# ====== END CONFIGURATION ======

intents = discord.Intents.default()
intents.message_content = True  # Make sure this is enabled in your bot settings on the Discord developer portal.
bot = commands.Bot(command_prefix="!", intents=intents)

# Store the latest video ID to detect new uploads
last_video_id = None
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
            # Start the loop after the bot is ready
    #check_for_new_videos.start()
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hey I figured this shit out ! Fuck the discord API! ")

'''
@tasks.loop(minutes=1)  # Checks every 24 hours , adjust as needed
async def check_for_new_videos():
    global last_video_id
    feed = feedparser.parse(CHANNEL_URL)
    if not feed.entries:
        return  # No videos found in the feed

    latest_entry = feed.entries[0]
    video_id = latest_entry.yt_videoid
    video_title = latest_entry.title
    video_link = latest_entry.link

        # If we haven't stored a last_video_id yet, initialize it and don't send a message
            # This prevents spamming on the first run
    if last_video_id is None:
        last_video_id = video_id
        return

    # Check if there is a new video
    if video_id != last_video_id:
        last_video_id = video_id
        channel = bot.get_channel(CHANNEL_ID)
        if channel is not None:
        # Send a message about the new video
            embed = discord.Embed(title=video_title, url=video_link, description="A new video has been uploaded!", color=0xFF0000)
            embed.set_author(name="New YouTube Upload")
            await channel.send(embed=embed)

@check_for_new_videos.before_loop
async def before_check_for_new_videos():
    await bot.wait_until_ready()

'''
@bot.command(name="test")
async def test_command(ctx):
    await ctx.send("Test successful , I figured this shit out !")

try:
    bot.run(TOKEN)

except Exception as e:
    print(e)

