import discord,asyncio,os,re,commands as mod,random,requests,string
from datetime import datetime, timedelta, date
from discord.ext import commands, tasks
from urllib import parse, request
from importlib import reload
from dislash import *
from time import sleep

bot = commands.Bot(command_prefix='!', description="This is a Helper Bot")
inter_client = InteractionClient(bot)

@bot.event
async def on_ready(): 
	await asyncio.sleep(30)
	ALIVE = bot.get_channel(int(os.getenv("ALIVE_CHANNEL")))
	await ALIVE.send('Bot restarted - ' + str(datetime.now())[:-10]) #alert when bot is started up / restarted
	await asyncio.sleep(60)
	if not stayAlive.is_running(): #if stayAlive is not already running, then start stayAlive
		stayAlive.start(ALIVE)	

@tasks.loop(seconds=3600) #repeats every 1 hour
async def stayAlive(ALIVE):
	await ALIVE.send('Test Bot is alive - ' + str(datetime.now())[:-10]) #alert that bot is still alive

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>facts command
@inter_client.slash_command(
	description="Generate a random fact!",
	options=[Option("facts",description="Generate a random fact!",type=OptionType.STRING,required=True,
			choices=[OptionChoice("bidoof", "Bidoof"), OptionChoice("seagull", "Seagull")]])
async def facts(inter, facts):
	ALIVE = bot.get_channel(int(os.getenv("TEST_COMMANDS")))
	reload(mod) #reload commands.py
	await mod.facts(inter, ALIVE, facts)

bot.run(os.getenv("DISCORD_TOKEN"), bot=True, reconnect=True)
