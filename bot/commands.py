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
    count, count1, count2, fastmove, XL, minRank, maxRank= 1,1,0,None,False,1,5
    matchoppt, matchrate, countoppt, countrate, chargemove = [], [], [], [], []
    if meta == "Great":
        meta1 = "Great League"
        parser = ijson.parse(open("bot/pvpoke/gl-rankings-1500.json"))
        thumb = "https://silph.gg/img/badges/great-league.png"
        listXL = ["Diggersby", "Lickitung", "Pachirisu", "Wobbuffet", "Sableye (Shadow)", "Spritzee", "Grimer (Alolan)"]
    elif meta == "Remix Great":
        meta1 = "Great League Remix"
        parser = ijson.parse(open("bot/pvpoke/glremix-rankings-1500.json"))
        thumb = "https://silph.gg/img/badges/great-league.png"
        listXL = ["Diggersby", "Lickitung", "Pachirisu", "Wobbuffet", "Grimer (Alolan)", "Wormadam (Trash)", "Chansey", "Sandshrew (Alolan)"]
    elif meta == "Glacial":
        meta1 = "Glacial Cup"
        parser = ijson.parse(open("bot/pvpoke/glacial-rankings-1500.json"))
        thumb = "https://assets.sil.ph/silph-arena/assets/2021-12-01-glacial-cup/glacial-cup-badge.png"
        listXL = ["Grimer (Alolan)", "Poliwhirl"]
    embedVar = discord.Embed(title="PvPoke | " + meta1 + " - Ranks " + str(ranks-4) + " to " + str(ranks), description="", color=0x000000)
    for prefix, event, value in parser:
        if (ranks-4) <= count and count <= ranks:
            if prefix.endswith('.speciesName'):
                pokemon = str(value).upper()
                for poke in listXL:
                    if poke == value:
                        XL = True
                if XL == False:
                    if meta == "Great":
                        parser1 = ijson.parse(open("bot/pvpoke/gl-rankings-1500.json"))
                    elif meta == "Remix Great":
                        parser1 = ijson.parse(open("bot/pvpoke/glremix-rankings-1500.json"))
                    elif meta == "Glacial":
                        parser1 = ijson.parse(open("bot/pvpoke/glacial-rankings-1500.json"))
                    for prefix1, event1, value1 in parser1:
                        if count < count1:
                            if prefix1.endswith('.speciesName'):
                                if value == value1:
                                    XL = True
                        if prefix1 == 'item':
                            if event1 == 'end_map':    
                                count1 += 1
            elif prefix.endswith('.matchups.item.opponent'):
                matchoppt.append(str(value).title().replace("_"," ").replace(" Shadow"," (Shadow)").replace(" Alolan"," (Alolan)"))
            elif prefix.endswith('.matchups.item.rating'):
                matchrate.append(str(value))
            elif prefix.endswith('.counters.item.opponent'):
                countoppt.append(str(value).title().replace("_"," ").replace(" Shadow"," (Shadow)").replace(" Alolan"," (Alolan)"))
            elif prefix.endswith('.counters.item.rating'):
                countrate.append(str(value))
            elif prefix.endswith('item.moveset.item'):
                if count2 == 0:
                    fastmove = str(value).title().replace("_"," ")
                    count2 += 1
                elif count2 == 1 or count2 == 2:
                    chargemove.append(str(value).title().replace("_"," "))
                    count2 += 1
            elif prefix == 'item':
                if event == 'end_map':
                    #add emoji on
                    with open('bot/pvpoke/movesets/water') as file:
                        for item in file:
                            if item.replace("\n","") == chargemove[0]:
                                chargemove[0] = "<:water:919749820795732058>" + chargemove[0]
                            if item.replace("\n","") == chargemove[1]:
                                chargemove[1] = "<:water:919749820795732058>" + chargemove[1]
                            if item.replace("\n","") == fastmove:
                                fastmove = "<:water:919749820795732058>" + fastmove
                    with open('bot/pvpoke/movesets/ice') as file:
                        for item in file:
                            if item.replace("\n","") == chargemove[0]:
                                chargemove[0] = "<:ice:919749820741214288>" + chargemove[0]
                            if item.replace("\n","") == chargemove[1]:
                                chargemove[1] = "<:ice:919749820741214288>" + chargemove[1]
                            if item.replace("\n","") == fastmove:
                                fastmove = "<:ice:919749820741214288>" + fastmove
                    with open('bot/pvpoke/movesets/ground') as file:
                        for item in file:
                            if item.replace("\n","") == chargemove[0]:
                                chargemove[0] = "<:ground:919750721442832395>" + chargemove[0]
                            if item.replace("\n","") == chargemove[1]:
                                chargemove[1] = "<:ground:919750721442832395>" + chargemove[1]
                            if item.replace("\n","") == fastmove:
                                fastmove = "<:ground:919750721442832395>" + fastmove
                    if XL == True:
                        embedVar.add_field(name="»»»» #" + str(count) + ": " + pokemon + " (XL) ««««",value="**Suggested Moveset>>**\n" + fastmove + "\n" + chargemove[0] + " & " + chargemove[1], inline=False)
                    else:
                        embedVar.add_field(name="»»»» #" + str(count) + ": " + pokemon + " ««««",value="**Suggested Moveset>>**\n" + fastmove + "\n" + chargemove[0] + " & " + chargemove[1], inline=False)
                    embedVar.add_field(name="Key Wins>>",value=matchoppt[0] + " *[" + matchrate[0] + "]*\n" + matchoppt[1] + " *[" + matchrate[1] + "]*\n" + matchoppt[2] + " *[" + matchrate[2] + "]*\n" + matchoppt[3] + " *[" + matchrate[3] +  "]*\n" + matchoppt[4] + " *[" + matchrate[4] + "]*", inline=True)
                    embedVar.add_field(name="Key Losses>>",value=countoppt[0] + " *[" + countrate[0] + "]*\n" + countoppt[1] + " *[" + countrate[1] + "]*\n" + countoppt[2] + " *[" + countrate[2] + "]*\n" + countoppt[3] + " *[" + countrate[3] +  "]*\n" + countoppt[4] + " *[" + countrate[4] + "]*", inline=True)
                    matchoppt.clear()
                    matchrate.clear()
                    countoppt.clear()
                    countrate.clear()
                    chargemove.clear()
                    fastmove, XL = None,False
                    count1, count2 = 0,0
        if prefix == 'item':
            if event == 'end_map':
                count += 1
    embedVar.set_footer(text="All data has been provided from www.pvpoke.com | www.seagullsbot.com",icon_url = "https://pbs.twimg.com/profile_images/1085243290671304704/3XyaT2qY_400x400.png")
    embedVar.set_thumbnail(url=thumb)
    await inter.reply(embed=embedVar)
    await channelPrint.send('PvPoke Ranks - ' + str(inter.guild.name) + ' - ' + str(inter.author) + '.')
