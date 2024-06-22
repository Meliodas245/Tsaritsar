import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    activity=discord.Activity(name='Tsaritsa', type=discord.ActivityType.watching),
    intents = discord.Intents.all()
)

intents = discord.Intents.all()

# Load environment variables from .env file
load_dotenv()

# Retrieve the token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

client.run(TOKEN)
