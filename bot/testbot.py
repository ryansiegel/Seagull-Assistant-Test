import discord,asyncio,os,re,commands as mod,random,requests,string,ijson
from datetime import datetime, timedelta, date
from discord.ext import commands, tasks
from urllib import parse, request
from importlib import reload
from dislash import *
from time import sleep

bot = commands.Bot(command_prefix='!', description="This is a Helper Bot")
inter_client = InteractionClient(bot, test_guilds=[869586825025552424])

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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>facts command
@inter_client.slash_command(
	description="Generate a random fact!",
	options=[Option("facts",description="Generate a random fact!",type=OptionType.STRING,required=True,
			choices=[OptionChoice("bidoof", "Bidoof"), OptionChoice("seagull", "Seagull")])])
async def facts(inter, facts):
	ALIVE = bot.get_channel(int(os.getenv("TEST_COMMANDS")))
	reload(mod) #reload commands.py
	await mod.facts(inter, ALIVE, facts)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>pvpoke command
@inter_client.slash_command(name="pvpoke", description=".")
async def pvpoke(inter): 
    pass
@pvpoke.sub_command(name="rank-list", description=".", options=[Option("meta", ".", OptionType.STRING, required=True, choices=[OptionChoice("great", "Great"), 
						       OptionChoice("great-remix", "Remix Great"), OptionChoice("ultra", "Ultra"), OptionChoice("ultra-remix", "Remix Ultra"), OptionChoice("glacial", "Glacial")]), 
							Option("ranks", ".", OptionType.STRING, required=True, choices=[OptionChoice("1to5", 5), OptionChoice("6to10", 10), OptionChoice("11to15", 15), OptionChoice("16to20", 20), OptionChoice("21to25", 25), OptionChoice("26to30", 30), OptionChoice("31to35", 35), OptionChoice("36to40", 40), OptionChoice("41to45", 45), OptionChoice("46to50", 50),OptionChoice("51to55", 55), OptionChoice("56to60", 60), OptionChoice("61to65", 65), OptionChoice("66to70", 70), OptionChoice("71to75", 75), OptionChoice("76to80", 80), OptionChoice("81to85", 85), OptionChoice("86to90", 90), OptionChoice("91to95", 95), OptionChoice("96to100", 100)])])
async def rankList(inter, meta, ranks):
	ALIVE = bot.get_channel(int(os.getenv("TEST_COMMANDS")))
	reload(mod) #reload commands.py
	await mod.rankList(inter, ALIVE, meta, ranks)


bot.run(os.getenv("DISCORD_TOKEN"), bot=True, reconnect=True)
