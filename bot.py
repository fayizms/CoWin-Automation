import discord
from api import PIN

bot = discord.Client()
API_KEY = '' #TOKEN HIDDEN
check = PIN()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(msg):
    if msg.content.startswith('Check'):
        data = check.Data()
        await msg.channel.send(data)

bot.run(API_KEY)
