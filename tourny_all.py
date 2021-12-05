import discord,asyncio,os
from discord.ext import commands, tasks
import re
from discord.utils import get
from importlib import reload

bot = commands.Bot(command_prefix='!', description="This is a Helper Bot")

@bot.event
async def on_ready(): 
    # canton 72hr
    channel1 = bot.get_channel(909865466116337724)
    embedVar1 = discord.Embed(title="Canton PvP: Glacial Cup (Extended - 72hr)", description="", color=0x00679b)
    embedVar1.add_field(name="》TOURNAMENT INFORMATION",value="**Format:** Glacial Cup <:glacial:914793522996072448>\n**Link:** https://silph.gg/t/4ac7/ \n**Start Time:** Dec 5th at 7pm Central \n**Round Time Limit:** 72hr / 3 day rounds", inline=False)
    embedVar1.add_field(name="》CUP INFORMATION AND TEAM BUILDING HELP",value="Full Information on the Glacial Cup: [CLICK HERE](https://silph.gg/cup/glacial) \nPvPoke Ranking Meta: [CLICK HERE](https://pvpoke.com/rankings/glacial/1500/overall/) \n Meta Simplified by PvPSteve: [CLICK HERE](https://www.youtube.com/watch?v=K3bg5mcffHo)", inline="False")
    embedVar1.set_thumbnail(url="https://silph.gg/img/badges/glacial.png")
    await channel1.send(embed=embedVar1)
    await asyncio.sleep(5)
    embedVar1 = discord.Embed(title="COMMONLY ASKED QUESTIONS AND ISSUES", description="", color=0x000000)
    embedVar1.add_field(name="》How can I participate in Silph Arena?",value="You must have a Silph Travelers Card to participate in this tournament.\n:movie_camera: How to make your Silph Account: [CLICK HERE](https://www.youtube.com/watch?v=Vy-Tlhizpsc&t) \n<:silpharena:757384959706136658> Link to make Silph Account: [CLICK HERE](https://thesilphroad.com/users/registration)", inline="False")
    embedVar1.add_field(name="》What is the best way to arrange a match with my opponent?",value="Our advice is to arrange a match via DMs (right-click/hold down on the name -> message). It's fine to try to arrange a match in the tournament channel too, and use the tag to try to get your opponent's attention, but if that doesn't work, try to use DMs. Share your availability for the next few days with each other and try to find the best time for both to battle! In the case of no response from your opponent, or bad luck with finding the available time for both to battle, contact your Tournament Organizers by sending a ***/dispute*** command in the ***#extended-disputes*** channel and explain the situation as soon as possible.", inline="False")
    embedVar1.add_field(name="》What if we have an issue during our match that we need a TO to look into?",value="If there is a problem during your match, right away send a ***/dispute*** command in the ***#extended-disputes*** channel.", inline="False")
    embedVar1.add_field(name="》We are the last pair to complete our battles, how do we advance the round?",value="Once you have completed your battles and you are the final pair to complete their battles in the round, send the ***/advance-round*** command in the tournament channel.", inline="False")
    await channel1.send(embed=embedVar1)
    await asyncio.sleep(10)
    # canton 48hr
    channel2 = bot.get_channel(909867256199135242)
    embedVar2 = discord.Embed(title="Canton PvP: Glacial Cup (Extended - 48hr)", description="", color=0x00679b)
    embedVar2.add_field(name="》TOURNAMENT INFORMATION",value="**Format:** Glacial Cup <:glacial:914793522996072448>\n**Link:** https://silph.gg/t/tqcn/ \n**Start Time:** Dec 12th at 7pm Central \n**Round Time Limit:** 48hr / 2 day rounds", inline=False)
    embedVar2.add_field(name="》CUP INFORMATION AND TEAM BUILDING HELP",value="Full Information on the Glacial Cup: [CLICK HERE](https://silph.gg/cup/glacial) \nPvPoke Ranking Meta: [CLICK HERE](https://pvpoke.com/rankings/glacial/1500/overall/) \n Meta Simplified by PvPSteve: [CLICK HERE](https://www.youtube.com/watch?v=K3bg5mcffHo)", inline="False")
    embedVar2.set_thumbnail(url="https://silph.gg/img/badges/glacial.png")
    await channel2.send(embed=embedVar2)
    await asyncio.sleep(5)
    embedVar2 = discord.Embed(title="COMMONLY ASKED QUESTIONS AND ISSUES", description="", color=0x000000)
    embedVar2.add_field(name="》How can I participate in Silph Arena?",value="You must have a Silph Travelers Card to participate in this tournament.\n:movie_camera: How to make your Silph Account: [CLICK HERE](https://www.youtube.com/watch?v=Vy-Tlhizpsc&t) \n<:silpharena:757384959706136658> Link to make Silph Account: [CLICK HERE](https://thesilphroad.com/users/registration)", inline="False")
    embedVar2.add_field(name="》What is the best way to arrange a match with my opponent?",value="Our advice is to arrange a match via DMs (right-click/hold down on the name -> message). It's fine to try to arrange a match in the tournament channel too, and use the tag to try to get your opponent's attention, but if that doesn't work, try to use DMs. Share your availability for the next few days with each other and try to find the best time for both to battle! In the case of no response from your opponent, or bad luck with finding the available time for both to battle, contact your Tournament Organizers by sending a ***/dispute*** command in the ***#extended-disputes*** channel and explain the situation as soon as possible.", inline="False")
    embedVar2.add_field(name="》What if we have an issue during our match that we need a TO to look into?",value="If there is a problem during your match, right away send a ***/dispute*** command in the ***#extended-disputes*** channel.", inline="False")
    embedVar2.add_field(name="》We are the last pair to complete our battles, how do we advance the round?",value="Once you have completed your battles and you are the final pair to complete their battles in the round, send the ***/advance-round*** command in the tournament channel.", inline="False")
    await channel2.send(embed=embedVar2)
    await asyncio.sleep(10)
    # btw 48hr
    channel4 = bot.get_channel(900869599006965780)
    embedVar4 = discord.Embed(title="B.T.W. Presents: Glacial Cup", description="", color=0x00679b)
    embedVar4.add_field(name="》TOURNAMENT INFORMATION",value="**Format:** Glacial Cup <:glacial:914793522996072448>\n**Link:** https://silph.gg/t/ped7/ \n**Start Time:** Dec 10th at 8pm Eastern \n**Round Time Limit:** 48hr / 2 day rounds", inline=False)
    embedVar4.add_field(name="》CUP INFORMATION AND TEAM BUILDING HELP",value="Full Information on the Glacial Cup: [CLICK HERE](https://silph.gg/cup/glacial) \nPvPoke Ranking Meta: [CLICK HERE](https://pvpoke.com/rankings/glacial/1500/overall/) \n Meta Simplified by PvPSteve: [CLICK HERE](https://www.youtube.com/watch?v=K3bg5mcffHo)", inline="False")
    embedVar4.set_thumbnail(url="https://silph.gg/img/badges/glacial.png")
    await channel4.send(embed=embedVar4)
    await asyncio.sleep(5)
    embedVar4 = discord.Embed(title="COMMONLY ASKED QUESTIONS AND ISSUES", description="", color=0x000000)
    embedVar4.add_field(name="》How can I participate in Silph Arena?",value="You must have a Silph Travelers Card to participate in this tournament.\n:movie_camera: How to make your Silph Account: [CLICK HERE](https://www.youtube.com/watch?v=Vy-Tlhizpsc&t) \n<:silpharena:757384959706136658> Link to make Silph Account: [CLICK HERE](https://thesilphroad.com/users/registration)", inline="False")
    embedVar4.add_field(name="》What is the best way to arrange a match with my opponent?",value="Our advice is to arrange a match via DMs (right-click/hold down on the name -> message). It's fine to try to arrange a match in the tournament channel too, and use the tag to try to get your opponent's attention, but if that doesn't work, try to use DMs. Share your availability for the next few days with each other and try to find the best time for both to battle! In the case of no response from your opponent, or bad luck with finding the available time for both to battle, contact your Tournament Organizers by sending a ***/dispute*** command in the tournament channel and explain the situation as soon as possible.", inline="False")
    embedVar4.add_field(name="》What if we have an issue during our match that we need a TO to look into?",value="If there is a problem during your match, right away send a ***/dispute*** command in the tournament channel.", inline="False")
    embedVar4.add_field(name="》We are the last pair to complete our battles, how do we advance the round?",value="Once you have completed your battles and you are the final pair to complete their battles in the round, send the ***/advance-round*** command in the tournament channel.", inline="False")
    await channel4.send(embed=embedVar4)
    await asyncio.sleep(10)
    # pogolex 48hr
    channel5 = bot.get_channel(909864997830680596)
    embedVar5 = discord.Embed(title="KY Silph Arena: Glacial Cup (Extended Rounds)", description="", color=0x00679b)
    embedVar5.add_field(name="》TOURNAMENT INFORMATION",value="**Format:** Glacial Cup <:glacial:914793522996072448>\n**Link:** https://silph.gg/t/8ggg/ \n**Start Time:** Dec 3rd at 6pm Eastern \n**Round Time Limit:** 48hr / 2 day rounds", inline=False)
    embedVar5.add_field(name="》CUP INFORMATION AND TEAM BUILDING HELP",value="Full Information on the Glacial Cup: [CLICK HERE](https://silph.gg/cup/glacial) \nPvPoke Ranking Meta: [CLICK HERE](https://pvpoke.com/rankings/glacial/1500/overall/) \n Meta Simplified by PvPSteve: [CLICK HERE](https://www.youtube.com/watch?v=K3bg5mcffHo)", inline="False")
    embedVar5.set_thumbnail(url="https://silph.gg/img/badges/glacial.png")
    await channel5.send(embed=embedVar5)
    await asyncio.sleep(5)
    embedVar5 = discord.Embed(title="COMMONLY ASKED QUESTIONS AND ISSUES", description="", color=0x000000)
    embedVar5.add_field(name="》How can I participate in Silph Arena?",value="You must have a Silph Travelers Card to participate in this tournament.\n:movie_camera: How to make your Silph Account: [CLICK HERE](https://www.youtube.com/watch?v=Vy-Tlhizpsc&t) \n<:silpharena:757384959706136658> Link to make Silph Account: [CLICK HERE](https://thesilphroad.com/users/registration)", inline="False")
    embedVar5.add_field(name="》What is the best way to arrange a match with my opponent?",value="Our advice is to arrange a match via DMs (right-click/hold down on the name -> message). It's fine to try to arrange a match in the tournament channel too, and use the tag to try to get your opponent's attention, but if that doesn't work, try to use DMs. Share your availability for the next few days with each other and try to find the best time for both to battle! In the case of no response from your opponent, or bad luck with finding the available time for both to battle, contact your Tournament Organizers by sending a ***/dispute*** command in the tournament channel and explain the situation as soon as possible.", inline="False")
    embedVar5.add_field(name="》What if we have an issue during our match that we need a TO to look into?",value="If there is a problem during your match, right away send a ***/dispute*** command in the tournament channel.", inline="False")
    embedVar5.add_field(name="》We are the last pair to complete our battles, how do we advance the round?",value="Once you have completed your battles and you are the final pair to complete their battles in the round, send the ***/advance-round*** command in the tournament channel.", inline="False")
    await channel5.send(embed=embedVar5)
    await asyncio.sleep(10)


bot.run('TOKEN', bot=True, reconnect=True)
