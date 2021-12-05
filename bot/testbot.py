import discord,asyncio,os
from datetime import datetime, timedelta, date
from discord.ext import commands, tasks
from urllib import parse, request
import re
from discord.utils import get
import random
from importlib import reload
from dislash import *
from enum import Enum

TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix='!', description="This is a Helper Bot")
inter_client = InteractionClient(bot)
    

@bot.event
async def on_ready(): 
    print('We have logged in as {0.user}'.format(bot))
    aliveChannel = bot.get_channel(910039460383698995)
    currentTime = str(datetime.now())[:-10]
    await aliveChannel.send('Bot restarted - ' + currentTime)
    await asyncio.sleep(60)
    stayAlive.start()
	
@tasks.loop(seconds=3600) #repeats every 1 hour
async def stayAlive():
    aliveChannel = bot.get_channel(910039460383698995)
    currentTime = str(datetime.now())[:-10]
    print('Bot is alive - ' + currentTime)
    await aliveChannel.send('Bot is alive - ' + currentTime)
	
bot.run(TOKEN, bot=True, reconnect=True)
