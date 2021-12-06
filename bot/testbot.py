import discord,asyncio,os,re,speedtest
from datetime import datetime, timedelta, date
from discord.ext import commands, tasks
from urllib import parse, request
from importlib import reload
from dislash import *

TOKEN, ALIVE = os.getenv("DISCORD_TOKEN"), os.getenv("ALIVE_CHANNEL")
bot = commands.Bot(command_prefix='!', description="This is a Helper Bot")
inter_client = InteractionClient(bot)
    

@bot.event
async def on_ready(): 
	await ALIVE.send('Bot restarted - ' + str(datetime.now())[:-10])
	await asyncio.sleep(60)
	if not stayAlive.is_running():
		stayAlive.start()
	
@tasks.loop(seconds=3600) #repeats every 1 hour
async def stayAlive():
	speedChannel = bot.get_channel(915229249974181928)
	wifi  = speedtest.Speedtest()
	await ALIVE.send('Test Bot is alive - ' + str(datetime.now())[:-10])
	await speedChannel.send("Heroku Download Speed at " + str(datetime.now())[:-10] + " is: *" + str('{0:.2f}'.format(wifi.download() * 0.000001)) + " Mbps*\nHeroku Upload Speed at " + str(datetime.now())[:-10] + " is: *" + str('{0:.2f}'.format(wifi.upload() * 0.000001)) + " Mbps*")
    
	
bot.run(TOKEN, bot=True, reconnect=True)
