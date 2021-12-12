import discord,asyncio,os,re,speedtest,random,requests,string,ijson
from datetime import datetime, timedelta, date
from discord.ext import commands, tasks
from urllib import parse, request
from importlib import reload
from time import sleep

async def facts(inter, channelPrint, facts):
    if facts == "Seagull":
        fact1 = 'Seagulls are very clever. They learn, remember and even pass on behaviours, such as stamping their feet in a group to imitate rainfall and trick earthworms to come to the surface.'
        fact2 = 'Seagulls are attentive and caring parents. The male and female pair for life and they take turns incubating the eggs, and feeding and protecting the chicks.'
        fact3 = 'A small claw halfway up their lower leg enables them to sit and roost on high ledges without being blown off.'
        fact4 = 'In Native American symbolism, the seagull represents a carefree attitude, versatility, and freedom.'
        fact5 = 'Seagulls can be found all over the planet including the margins of Antarctica, and are found in the high Arctic, as well.'
        fact6 = 'Lifespan of seagulls depends on the species. Most seagulls have a lifespan from 10 to 15 years in the wild.'
        fact7 = 'The smallest seagull species is the little gull (Hydrocoloeus minutus or Larus minutus), with a length of 25–30 cm (9.8–11.8 in), a wingspan of 61–78 cm (24–31 in), and a mass of 68–162 g (2.4–5.7 oz).'
        fact8 = 'Seagulls are one of the rare animals that are able to drink salt water. They have special glands (located above the eyes) which eliminate excess salt from the body.'
        fact9 = 'Seagulls often steal food from other birds, animals and people. They occasionally eat young members of their own species (phenomenon called cannibalism).'
        fact10 = 'Seagulls are monogamous creatures (they mate for a lifetime). Mating couple gathers each year during the mating season to reproduce and to take care of their offspring.'
        factsList = [fact1, fact2, fact3, fact4, fact5, fact6, fact7, fact8, fact9, fact10]
        randomFact = random.choice(factsList)
        embedVar = discord.Embed(title="Seagull Facts!", description=randomFact, color=0x000000)
        await inter.reply(embed=embedVar)
        await channelPrint.send('Seagull Facts - ' + str(inter.guild.name) + ' - ' + str(inter.author) + '.')
    elif facts == "Bidoof":
        fact1 = 'Bidoof is a brown, rodent like Pokemon with four short legs.'
        fact2 = 'Protruding from Bidoof’s upper jaw are large incisors, which it uses for gnawing on wood and rocks.'
        fact3 = 'These teeth grow constantly, so this Pokémon needs to gnaw on hard substances to keep them ground down.'
        fact4 = 'This Pokémon can be found nesting in groups near bodies of water.'
        fact5 = 'Despite its stout body, this Pokémon can be agile and is not easily perturbed.'
        fact6 = 'A comparison revealed that Bidoofs front teeth grow at the same rate as Rattatas.'
        fact7 = 'Bidoof appears to be based on a beaver or a gopher. It is particularly similar to the mountain beaver, a primitive relative of beavers lacking tails.'
        factsList = [fact1, fact2, fact3, fact4, fact5, fact6, fact7]
        randomFact = random.choice(factsList)
        embedVar = discord.Embed(title="Bidoof Facts!", description=randomFact, color=0x000000)
        await inter.reply(embed=embedVar)
        await channelPrint.send('Bidoof Facts - ' + str(inter.guild.name) + ' - ' + str(inter.author) + '.')

async def rankList(inter, channelPrint, meta, ranks):
    count, counting, fastmove = 1,0,None
    matchoppt, matchrate, countoppt, countrate, chargemove = [], [], [], [], []
    if meta == "Great":
        meta = "Great League"
        parser = ijson.parse(open("bot/all-rankings-1500.json"))
    embedVar = discord.Embed(title="PvPoke | " + meta + " - Ranks 1 to 10", description="", color=0x000000)
    for prefix, event, value in parser:
        if count <= 10:
            if prefix.endswith('.speciesName'):
                pokemon = str(value).upper()
            elif prefix.endswith('.matchups.item.opponent'):
                matchoppt.append(str(value).title().replace("_"," "))
            elif prefix.endswith('.matchups.item.rating'):
                matchrate.append(str(value))
            elif prefix.endswith('.counters.item.opponent'):
                countoppt.append(str(value).title().replace("_"," "))
            elif prefix.endswith('.counters.item.rating'):
                countrate.append(str(value))
            elif prefix.endswith('item.moveset.item'):
                if counting == 0:
                    fastmove = str(value).title().replace("_"," ")
                    counting += 1
                elif counting == 1 or counting == 2:
                    chargemove.append(str(value).title().replace("_"," "))
                    counting += 1
            elif prefix == 'item':
                if event == 'end_map':
                    embedVar.add_field(name="#" + str(count) + ": " + pokemon,value="Suggested Moveset- " + fastmove + " | " + chargemove[0] + " & " + chargemove[1]) + "\n\tKey Wins>>\t" + matchoppt[0] + "(RATING: " + matchrate[0] + "), " + matchoppt[1] + "(RATING: " + matchrate[1] + "), " + matchoppt[2] + "(RATING: " + matchrate[2] + "), " + matchoppt[3] + "(RATING: " + matchrate[3] +  "), " + matchoppt[4] + "(RATING: " + matchrate[4] + ")\n\tKey Losses>>\t" + countoppt[0] + "(RATING: " + countrate[0] + "), " + countoppt[1] + "(RATING: " + countrate[1] + "), " + countoppt[2] + "(RATING: " + countrate[2] + "), " + countoppt[3] + "(RATING: " + countrate[3] +  "), " + countoppt[4] + "(RATING: " + countrate[4] + ")", inline=False)
                    matchoppt.clear()
                    matchrate.clear()
                    countoppt.clear()
                    countrate.clear()
                    fastmove = None
                    count += 1
                    counting = 0
                    chargemove.clear()
    embedVar.set_footer(text="www.seagullsbot.com")
    await inter.reply(embed=embedVar)
    await channelPrint.send('Bidoof Facts - ' + str(inter.guild.name) + ' - ' + str(inter.author) + '.')
