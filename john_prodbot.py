import random
import datetime
import time
import json
import discord
from discord.ext import commands
import logging

greetingHelper = """Greetings! My name is John ProdBot, AnyoCorp's Employee of the Month for the past nine years running! 

I'm still under development right now, but at the moment, I'm still happy to check your vibes, tell you how profitable you are today, answer your yes or no questions, or post a meme of the day for you in the mornings. In the future, I'll be able to fetch images, videos and reactions for you, remember your birthday, fetch current special Warframe mission information, and maybe even play some music for you! 

All my commands start with either "prodbot" or the $ character. While I'm still under development, my commands include:

> **Meme of the Day:** Bind this feature to a channel, and I'll post a meme from a curated selection for you every morning, including holidays! Set this feature up or turn it off by sending "prodbot motd" or "$motd" into the channel of your choice.
> **Ask ProdBot:** Ask me a yes or no question with "prodbot i have a question" or "$askprodbot" and I'll do my best to answer.
> **Vibe Check:** Enter "prodbot vibecheck [name]" or "$vibecheck [name]" and I'll tell you that person or thing's vibes.
> **Curse Scale:** How cursed are you today? If you enter "prodbot how cursed is/are/am [name]" or "$cursescale [name]", I'll tell you.
> **Profit Scale:** Like the curse scale, I can tell you how profitable you are today. Just say "prodbot how profitable is/are/am [name]" or "$profitscale [name]".
> **Reaction Image Database:** Need to express an emotion fast? Soon I'll be able to call a random reaction image for you, categorized by emotion. You'll be able to call on me for special videos, too. Anybody want Subway? How about some grofit?"""

plannedFeatures = """While they're not ready yet, some planned features include:
> **ProdBot's Singalong:** Ask me to sing a song for you and I'll pull up a random entry from a list of my favorite songs.
> **ProdBot Reacts:** I might have some things to say about special keywords in the chat.
> **Birthday Tracker:** Soon, I'll have a feature that allows you to input your birthday. Then, when it rolls around, I'll post an announcement about it.
> **Integrated Warframe Tracker:** Need to check today's sortie, the week's Nightwave tasks, the current time on the Plains, or the current Arbitration or fissures, but don't want to log into the game? Using the data provided by the official API, I can fetch that for you!
> **Echobox:** Want to save that quote out of context for later use? If you put it in the echobox, I'll take it, and return another, random stored quote.
> **Music Player:** There's nothing that adheres to the Tenets more than telling another corporation where to shove it in order to seize your desires. Invite me into your voice channel and I'll play whatever Youtube links you want, and I'll even store a cache of already-played tracks for quick recall and minimal Youtube interference."""  

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix = '$', intents = intents)

client = discord.Client(intents = intents)
handler = logging.FileHandler(filename = 'discord.log', encoding = 'utf-8', mode = 'w')

client.run("TOKEN REDACTED FOR GITHUB COPY", log_handler = handler)

@client.event
async def on_ready():
    print(greetingHelper)

# everything below is commented out as reference code for the discord implementation because as it turns out, sending print(whatever) is not how it actually works. functions that are confirmed to be working as intended will be removed from the commented out code as i go    
"""def vibecheck():
    vibecheckpass = ["are good.", "are great.", "are within normal range.", "are huge.", "are massive.", "are fantastic.", "are radical.", "are amazing.", "are superb.", "are sublime.", "are radiant.", "are wonderful.", "are good for business.", "have raised our stock prices.", "are powerful.", "are profitable.", "are magical.", "are whimsical.", "are Employee of the Month-worthy.", "are beautiful.", "are glamourous.", "are perfection.", "are OSHA-approved.", "are in accordance with the Tenets.", "are groovy.", "are tubular.", " are way cool.", "are gnarly.", "are awesome.", "are brilliant."]
    vibecheckmystery = ["are beyond comprehension.", "have been beheld by That Which Bears No Name.", "have been stolen.", "are [DATA EXPUNGED].", "are missing.", "are gone.", "are broken.", "have been lost to the Void.", "have been taken.", "are too much for me.", "are ominous.", "are above my paygrade.", "are missingno.", "have clipped into the floor.", "are a mystery.", "are incomprehensible.", "are destabilizing the stock market.", "are unusual.", "are strange.", "are weird.", "have disappeared.", "are corrupted.", "are werewolves.", "have vanished.", "are not of this world.", "have fucked off.", "are on vacation.", "are [garbled static].", "are unreadable.", "just Are."]
    vibecheckfail = ["are bad.", "are terrible.", "are awful.", "are horrible.", "might be counterfeit.", "are ass.", "are unprofitable.", "look a bit shit.", "are horrifying.", "are musty.", "are stinky.", "are making me sad.", "are crashing the stock market.", "made me lose at the Index.", "are unholy.", "are illegal.", "are ugly.", "are not OSHA approved.", "are sad.", "are wack.", "would get you glassed.", "are atrocious.", "are smelly.", "are dogshit.", "are cheesy.", "make sweet sundae ramen look like fine dining.", "will put you in debt.", "are terrifying.", "are weak.", "are cursed, and not in the cool way."] 
    passtext = f"Vibe check passed. Your vibes {random.choice(vibecheckpass)}"
    mysterytext = f"Vibe check ???. Your vibes {random.choice(vibecheckmystery)}"
    failtext = f"Vibe check failed. Your vibes {random.choice(vibecheckfail)}"
    vibes = random.randrange(1, 4)
    if vibes < 2:
        print(failtext)
    elif vibes == 2:
        print(mysterytext)
    else:
        print(passtext)

# can't stand to go without the daily cursescale.
def cursescale():
    cursepercent = random.randrange(0, 101)
    text = f"*Username* is {cursepercent}% cursed."
    if cursepercent == 69:
        print(text + " Nice.")
    else:
        print(text) 

# a new scale, based on the same idea as the cursescale 
def profitscale():
    profit = random.randrange(0, 101)
    text = f"*Username* is {profit}% profitable."
    if profit > 50:
        print(text + " That's great!")
    else:
        print(text)

# 8ball style "ask yes or no" feature. also works and was easy to make happen
def askProdbot():
    yes = ["Yes.", "It is certain.", "Absolutely.", "Positively.", "Why not?", "Yeah.", "Definitely.", "For sure.", "By all means."]
    no = ["No.", "Nah.", "Absolutely not.", "Negatory.", "Nein.", "Bad call, boss.", "Doesn't sound work-safe to me.", ":sparkles: No :sparkles:", "Not a chance."] 
    maybe = ["Maybe.", "Uncertain.", "Ask me after my break.", "Great question! I can't answer it.", "Probably?", "No idea.", "It is a mystery.", "Maybe, maybe not.", "Who knows."]
    yestext = f"{random.choice(yes)}"
    notext = f"{random.choice(no)}"
    maybetext = f"{random.choice(maybe)}"
    answer = random.randrange(1, 4)
    if answer < 2:
        print(notext)
    elif answer == 2:
        print(maybetext)
    else:
        print(yestext)

# this function will eventually be used to call a random meme from a json file in the directory the bot is running from. i already have a directory borrowed from the friend's bot i'm basing this function on but do not yet know how to make it call a random line from a given area in the list
def motdGet():
    with open("motdDB.json") as motd:
        print(motd.readline())

def motd():
    calendar = datetime.datetime.now()
    month = calendar.month
    date = calendar.day 
    day = int(calendar.strftime("%w"))
    hour = calendar.hour
    minute = calendar.minute
    second = calendar.second 
    # extremely rudimentary time check function. eventual plan is to have this function bind to a channel (probably the bot channel) and post a meme every day based on the day of the week/holiday. as of right now the day check works the way it should and i'm not sure it can get much better without branching into other files, but i don't know how to make a timer without being this incredibly specific about it just yet. help is appreciated, commenting it out for the discord implementation for now so it doesn't freak it the fuck out
    if hour == 8 and minute == 0 and second == 1:
        match date:
            case 1:
                if month == 1:
                    print("new years/fuck you it's january")
                elif month == 4:
                    print("april fools")
                elif month == 5:
                    print("what a year huh")
                elif month == 6:
                    print("pride month start")
                elif month == 8:
                    print("digimon august 1st")
                elif month == 10:
                    print("it's spooky month")
                elif month == 11:
                    print("incoming mariah carey")
                elif month == 12:
                    print("kringlefucker")
                else:
                    pass
            case 2: 
                if day == 4:
                    print("thursday the 2")
                else:
                    pass
            case 4:
                if month == 5:
                    print("may the fourth")
                else:
                    pass
            case 5:
                if month == 6:
                    print("ronald reagan death day")
                elif month == 11:
                    print("remember remember")
                else:
                    pass
            case 6:
                if month == 2:
                    print("mewtwo birthday")
                else:
                    pass
            case 9:
                if month == 10: 
                    print ("leif erikson day, hinga dinga durgen")
            case 10:
                if month == 3:
                    print("mario day")
                elif month == 5:
                    print("april 40th")
                elif month == 12:
                    print("it's december 10th")
                else:
                    pass
            case 12:
                if month == 5:
                    print("find a meme for the starlit heroics anniversary")
                elif day == 4:
                    print("thursday the 12th")
                else:
                    pass
            case 13:
                if month == 4:
                    print("homestuck day and/or neil banging out the tunes")
                elif day == 5:
                    print("friday the 13th")
                else:
                    pass 
            case 14:
                if month == 2: 
                    print("valentine's day")
                elif month == 3:
                    print("pi day")
                elif month == 6:
                    print("happy birthday to this parrot in particular")
                else:
                    pass
            case 15:
                if month == 1:
                    print("boston molasses flood day")
                elif month == 3:
                    print("ides of march")
                else:
                    print("GIVE IT UP FOR DAY 15")
            case 16:
                if month == 2:
                    print("shirley temple day")
                else:
                    pass
            case 18:
                if month == 5: 
                    print("shrek anniversary")
                else:
                    pass
            case 19:
                if month == 7:
                    print("one piece day")
                elif month == 9:
                    print("pirate day")
                elif day == 3:
                    print("wednesday the 19th")
                else:
                    pass
            case 20:
                if month == 4 and day == 4:
                    print("thursday the 420th")
                elif month == 4 and day != 4:
                    print("4/20")
                elif month == 9:
                    print("day before the 21st night of september")
                elif day == 4:
                    print("thursday the 20th. may be simpsons or columbo depending on the mood")
                else: 
                    pass
            case 21:
                if month == 6:
                    print("spongebob summer solstice")
                elif month == 9:
                    print("do you remember")
                elif month == 12:
                    print("find a winter solstice meme that isn't cthulhu")
                else: 
                    pass
            case 22:
                if month == 3:
                    print("warframe anniversary")
            case 23:
                if month == 9:
                    print("little shop of horrors")
                elif month == 12:
                    print("festivus")
                else:
                    pass
            case 24:
                if month == 12:
                    print("santa's comin tonight")
                else:
                    pass
            case 25:
                if month == 12:
                    print("spongebob santa")
                else:
                    pass
            case 26:
                if month == 7:
                    print("intro to shrek. do not elaborate, if you know you know")
                elif day == 0:
                    print("spongebob sunday the 26th")
                else:
                    pass
            case 28:
                if month == 5:
                    print("squids was invented")
                else:
                    pass
            case 29:
                if month == 1:
                    print("happy birthday cars")
                elif month == 11:
                    print("happy birthday video games")
            case 31:
                if month == 10:
                    print("halloween")
                elif month == 12:
                    print("new year's eve. use the kalymos kiss scene OR randomize which kiss, instead of using auld lang syne")
                else:
                    pass
            case _:
                if day == 0:
                    print("sunday meme; remove harry potter and that awful fly")
                elif day == 1:
                    print("monday meme; remove karl marx, he is not invited to epoch")
                elif day == 2:
                    print("tuesday meme")
                elif day == 3:
                    print("wednesday meme")
                elif day == 4:
                    print("thursday meme")
                elif day == 5:
                    print("friday meme")
                elif day == 6:
                    print("saturday meme")
    else:
        pass"""   

@bot.command()
async def help(ctx):
    await ctx.send(greetingHelper)

@bot.command()
async def planned(ctx):
    await ctx.send(plannedfeatures)

@bot.command()
async def angery(ctx):
    await ctx.send("a random reaction image, defined as angry by reactionDB.json")

@bot.command()
async def sad(ctx):
    await ctx.send("a random reaction image, defined as sad by reactionDB.json")

@bot.command()
async def hug(ctx):
    await ctx.send("a random reaction image, defined as a hug by reactionDB.json")

@bot.command()
async def kiss(ctx):
    await ctx.send("a random reaction image, defined as a kiss by reactionDB.json")

@bot.command()
async def confused(ctx):
    await ctx.send("a random reaction image, defined as confused by reactionDB.json")

@bot.command()
async def happy(ctx):
    await ctx.send("a random reaction image, defined as happy by reactionDB.json")

@bot.command()
async def what(ctx):
    await ctx.send("a random reaction image, defined as 'what the fuck' by reactionDB.json")

@bot.command()
async def no(ctx):
    await ctx.send("a random reaction image, defined as 'no' by reactionDB.json")

@bot.command()
async def yes(ctx):
    await ctx.send("a random reaction image, defined as 'yes' by reactionDB.json")

@bot.command()
async def subway(ctx):
    await ctx.send("https://www.youtube.com/watch?v=y3VRXVvr6XU")

@bot.command()
async def florida(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1071547517847732305/1305253566348529696/florida.gif")

@bot.command()
async def cursecheck(ctx, arg):
    cursepercent = random.randInt(0, 100)
    selftext = f"*Username* is {cursepercent}% cursed."
    othertext = f"{arg} is {cursepercent}% cursed."
    if arg == "me":
        if cursepercent == 69:
            await ctx.send(selftext + " Nice.")
        else:
            await ctx.send(selftext)
    else:
        if cursepercent == 69:
            await ctx.send(othertext + " Nice.")
        else:
            await ctx.send(othertext)

@bot.command()
async def profitcheck(ctx, arg):
    profit = random.randrange(0, 101)
    selftext = f"*Username* is {profit}% profitable."
    othertext = f"{arg} is {profit} profitable."
    if arg == "me":
        if profit > 50:
            await ctx.send(selftext + " That's great!")
        else:
            await ctx.send(selftext)
    else:
        if profit > 50:
            await ctx.send(othertext + " That's great!")
        else:
            await ctx.send(othertext)
