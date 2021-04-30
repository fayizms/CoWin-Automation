import discord
import req_module

bot = discord.Client()
api_key = 'ODM3MzgwNjI3NjU2NzM2Nzkz.YIrtew.2pgCECLo8fbuiOIcMCer2o5UWE0'

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(msg):
    if msg.contents.startswith('Check'):
        result = req_module.main(req_module.PIN, req_module.DATE)

bot.run(api_key)