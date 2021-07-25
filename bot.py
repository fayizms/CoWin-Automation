import discord
from api import PIN

bot = discord.Client()
API_KEY = 'ODM3MzgwNjI3NjU2NzM2Nzkz.YIrtew.2pgCECLo8fbuiOIcMCer2o5UWE0'
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