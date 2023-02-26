import os
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID'))

intents = discord.Intents.default()
intents.guilds = True  # enable guild intents to receive guild events

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    guild = client.get_guild(GUILD_ID)
    await guild.leave()
    print(f'{client.user} has left the guild {guild.name} ({guild.id})')


client.run(TOKEN)

# Quest Systems https://discord.gg/BsMPHWmXuM