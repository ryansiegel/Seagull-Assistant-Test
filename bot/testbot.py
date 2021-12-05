import discord,asyncio,os,re
from datetime import datetime, timedelta, date
from discord.ext import commands, tasks
from urllib import parse, request
from importlib import reload
from dislash import *

TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix='!', description="This is a Helper Bot")
inter_client = InteractionClient(bot)
    

@bot.event
async def on_ready(): 
	aliveChannel = bot.get_channel(910039460383698995)
	await aliveChannel.send('Bot restarted - ' + str(datetime.now())[:-10])
	await asyncio.sleep(60)
	if not stayAlive.is_running():
		stayAlive.start()
	
@tasks.loop(seconds=3600) #repeats every 1 hour
async def stayAlive():
	aliveChannel = bot.get_channel(910039460383698995)
	await aliveChannel.send('Bot is alive - ' + str(datetime.now())[:-10])
    
	
bot.run(TOKEN, bot=True, reconnect=True)
