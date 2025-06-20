import random
import datetime
import time
import json
import discord
from discord.ext import commands
import logging
import asyncio 

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  

bot = commands.Bot(command_prefix = '$', intents = intents)

client = discord.Client(intents = intents)
handler = logging.FileHandler(filename = 'discord.log', encoding = 'utf-8', mode = 'w')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}. (ID: {bot.user.id})")
    
@bot.command()
async def helpme(ctx): 
    await ctx.send("""Greetings! My name is John ProdBot, AnyoCorp's Employee of the Month for the past nine years running! 

I'm still under development right now, but at the moment, I'm still happy to check your vibes, tell you how profitable you are today, answer your yes or no questions, or post a meme of the day for you in the mornings. In the future, I'll be able to fetch images, videos and reactions for you, remember your birthday, fetch current special Warframe mission information, and maybe even play some music for you! 

All my commands start with either "prodbot" or the $ character. While I'm still under development, my commands include:

> **Meme of the Day:** Bind this feature to a channel, and I'll post a meme from a curated selection for you every morning, including holidays! Set this feature up or turn it off by sending "prodbot motd" or "$motd" into the channel of your choice.
> **Ask ProdBot:** Ask me a yes or no question with "prodbot i have a question" or "$askprodbot" and I'll do my best to answer.
> **Vibe Check:** Enter "prodbot vibecheck [name]" or "$vibecheck [name]" and I'll tell you that person or thing's vibes.
> **Curse Scale:** How cursed are you today? If you enter "prodbot how cursed is/are/am [name]" or "$cursescale [name]", I'll tell you.
> **Profit Scale:** Like the curse scale, I can tell you how profitable you are today. Just say "prodbot how profitable is/are/am [name]" or "$profitscale [name]".
> **Reaction Image Database:** Need to express an emotion fast? Soon I'll be able to call a random reaction image for you, categorized by emotion. You'll be able to call on me for special videos, too. Anybody want Subway? How about some grofit?""")

@bot.command()
async def planned(ctx):
    await ctx.send("""While they're not ready yet, some planned features include:
> **ProdBot's Singalong:** Ask me to sing a song for you and I'll pull up a random entry from a list of my favorite songs.
> **ProdBot Reacts:** I might have some things to say about special keywords in the chat.
> **Birthday Tracker:** Soon, I'll have a feature that allows you to input your birthday. Then, when it rolls around, I'll post an announcement about it.
> **Integrated Warframe Tracker:** Need to check today's sortie, the week's Nightwave tasks, the current time on the Plains, or the current Arbitration or fissures, but don't want to log into the game? Using the data provided by the official API, I can fetch that for you!
> **Echobox:** Want to save that quote out of context for later use? If you put it in the echobox, I'll take it, and return another, random stored quote.
> **Music Player:** There's nothing that adheres to the Tenets more than telling another corporation where to shove it in order to seize your desires. Invite me into your voice channel and I'll play whatever Youtube links you want, and I'll even store a cache of already-played tracks for quick recall and minimal Youtube interference.""")

@bot.command()
async def angery(ctx):
    await ctx.send("a random reaction image, defined as angry by reactionDB.json")

@bot.command()
async def sad(ctx):
    await ctx.send("a random reaction image, defined as sad by reactionDB.json")

@bot.command()
async def fear(ctx):
    await ctx.send("a random reaction image, defined as fear by reactionDB.json")

@bot.command()
async def hug(ctx):
    await ctx.send("a random reaction image, defined as a hug by reactionDB.json")

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
async def disgust(ctx):
    await ctx.send("a random reaction image, defined as disgust by reactionDB.json")
    
@bot.command()
async def anguish(ctx):
    await ctx.send("a random reaction image, defined as anguish by reactionDB.json")

@bot.command()
async def nut(ctx):
    await ctx.send("a random reaction image, defined as 'nut' by reactionDB.json")

@bot.command()
async def clown(ctx):
    await ctx.send("a random reaction image, defined as 'clown' by reactionDB.json")

@bot.command()
async def evil(ctx):
    await ctx.send("a random reaction image, defined as evil by reactionDB.json")

@bot.command()
async def shutup(ctx):
    await ctx.send("a random reaction image, defined as 'shut up' by reactionDB.json")

@bot.command()
async def subway(ctx):
    await ctx.send("https://www.youtube.com/watch?v=y3VRXVvr6XU")

@bot.command()
async def florida(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1071547517847732305/1305253566348529696/florida.gif")

@bot.command()
async def kill(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/920819855790325770/920821252912975872/Tumblr_l_692488891846876.gif?ex=685698de&is=6855475e&hm=bddae18894705be594c691e55207194b410fa8eaf66c2c9105f645542427bf14&")

@bot.command()
async def sin(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/920819855790325770/920821567901032448/Screenshot_20210719-1351082.png?ex=68569929&is=685547a9&hm=2274832e28d73d5ad89c29b202bcb67697155c7a75ba9d6a000bc9c7aecdf437&")

@bot.command()
async def mysterysolved(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/920819855790325770/920821925079580672/Screenshot_20201227-220959_Adblock_Browser.jpg?ex=6856997e&is=685547fe&hm=89732f951d663580e28c2e7dd02be0a696bdb1bc2a9435c853d843d3674600e4&")

@bot.command()
async def shamecube(ctx):
    await ctx.send("https://media.discordapp.net/attachments/920819855790325770/921147285201616996/when_ur_weird_kinks_appear_in_any_medium.gif?ex=68567702&is=68552582&hm=e2b017cda8cf7869135abe25b7b3c29e732e69f85ccd7302a212b0eafbcac6c2&=")

@bot.command()
async def typo(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/920819855790325770/923409667013619732/typoinchat.png?ex=6856c904&is=68557784&hm=0ae82fd0b7042ff399344ab12fdc48bb98c6c2bc92b58225a32a5a1af21f3b3b&")

@bot.command()
async def controversial(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/920819855790325770/924618508753567774/D0hpoRPWsAAEzgx.png?ex=68569197&is=68554017&hm=6134b1227373bd055d1d44b223092061f9cf37ff9a12a8e25156b395027610f6&")

@bot.command()
async def playedyourself(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/920819855790325770/924618530970808380/Dz2GUyaX4AAfTLs.png?ex=6856919c&is=6855401c&hm=c716b16568f018f8a2c76e7ca379fa557a309fe6ae939f0aea647c3acfd93c50&")

@bot.command()
async def apollo(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/920819855790325770/920821163079376996/Tumblr_l_41969194844092.jpg?ex=685698c9&is=68554749&hm=5934b7addafcc08d84d2836b5490b3195a702209daa907e6fb39229c0f91f984&")

@bot.command()
async def right(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/920819855790325770/924619346452557904/Screen_Shot_2017-11-06_at_12.41.31_PM.png?ex=6856925e&is=685540de&hm=a31d5fb35501546dba7d03fbe3ed9a03ee27bb086db02307fafb353ca6c9fc8b&")

@bot.command()
async def dumpster(ctx):
    await ctx.send("https://tenor.com/view/1997_hello-chat-gif-24146200")

@bot.command()
async def twitter(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/920819855790325770/978476252275040286/tumblr_192794f83de045c36648deadd8e3b6ff_94021001_540.jpg?ex=6856b9c5&is=68556845&hm=01928339bd95c071adacf844fc856db70ab3ceb803b57ad9cbfcf9246cd5e28c&")

@bot.command()
async def freakshow(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/920819855790325770/1043884196495634512/Tumblr_l_204983250472480.jpg?ex=6856b6ea&is=6855656a&hm=36d942bff30f97d21ed06d908fa32aeebbc7bb216ee0bbe2f2fb3ae5e6c109f5&")

@bot.command()
async def nonsense(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/920819855790325770/1062228591997362286/IMG_2424.jpg?ex=6856dfb7&is=68558e37&hm=d2f7d7794a27fd2bf434d76dc5871e110e4b1350b4a06c6ad9830f9f6224d2e5&")

@bot.command()
async def fakejs(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/920819855790325770/1351926442224779315/tumblr_d066eb2362e8bd3407b94e548aec7ea2_f2b7ac64_500.png?ex=6856c29d&is=6855711d&hm=8a29233bcdf3f4f52825c758f31ea3181e62586ea0b7e04f261b5e4d42463cd6&")

@bot.command()
async def respects(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/920819855790325770/924618973574754314/DtDb8TSXcAUg85F.jpg?ex=68569205&is=68554085&hm=7af4739cd83a0e4407412309bb49db6c405509dee02c2227d704af0ba9e9f379&")

def cursecheck():
    cursepercent = random.randrange(0, 101)
    text = f"{arg} is {cursepercent}% cursed."
    if cursepercent == 69:
        print(text + " Nice.")
    else:
        print(text) 

# curse check isn't working yet
@bot.command()
async def cursescale(ctx, arg):
        await ctx.send(cursecheck(arg))

def profitcheck():
    profit = random.randrange(0, 101)
    text = f"*Username* is {profit}% profitable."
    if profit > 50:
        print(text + " That's great!")
    else:
        print(text)

# profit check isn't working yet
@bot.command()
async def profitscale(ctx, arg):
    await ctx.send(profitcheck(arg))

bot.run("TOKEN REDACTED", log_handler = handler)

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

# 8ball style "ask yes or no" feature
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

def motd():
    calendar = datetime.datetime.now()
    month = calendar.month
    date = calendar.day 
    day = int(calendar.strftime("%w"))
    hour = calendar.hour
    minute = calendar.minute
    second = calendar.second 
    # extremely rudimentary time check function. eventual plan is to have this function bind to a channel (probably the bot channel) and post a meme every day based on the day of the week/holiday. as of right now the day check works the way it should and i'm not sure it can get much better without branching into other files, but i don't know how to make a timer without being this incredibly specific about it just yet
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
