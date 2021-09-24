import os
from os import system, name
import discord
from discord.ext import commands
import asyncio
import random
import time
import email
import string
import sys
import asyncio
from datetime import datetime
from discord.ext.commands import Bot
from discord_components import Button, Select, SelectOption, ComponentsBot, DiscordComponents
from math import sqrt
import threading
from pyrandmeme import *
import subprocess
#import website  #this runs the file website.py
#Importing modules
#if discord components doeset work: pip install --upgrade discord-components
#go to packages and install discord components


#https://uptimerobot.com/dashboard?ref=website-header#tvMode to monitor bot 
#post that helps for uptime robot https://replit.com/talk/learn/How-to-use-and-setup-UptimeRobot/9003?order=new








bot = commands.Bot(command_prefix='$')
#bot commmands prefix


@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online, activity = discord.Game(name="The ping game, online!"))
  
  print("BOT ONLINE")
  DiscordComponents(bot)

  threading.Thread(target=runsitefunc).start()
  print("WEBSITE ONLINE")

#detects when bot logs in with auth token (hash) then sets presence to onine


client = discord.Client()
#sets the bot client
    
'''
def msg(user, message):
  msg.invoke(bot.get_command('send'), User=user, Message=message)

@bot.command()
@commands.has_any_role("moderator")
async def send(ctx, User, Message):
  await User.send('From website: ```'+User+'```\n'+'Message: ```'+Message+'```')
'''


@bot.command(brief='Creates a random number', description='Creates a random number, useful for bets or draws', aliases=['rannum', 'randomnum', 'dice'])
@commands.has_any_role("Verified")
async def roll(ctx, Min, Max):
    try:
        Min1 = int(Min)
        Max1 = int(Max)
        Res = random.randint(Min1, Max1)
        Res1 = str(Res)
        await ctx.send(Res1+' was your random number')
    except:
        await ctx.send('Sorry, but an error occoured in my code. Please try again')
#command to create a random num, uses random module

@bot.command(brief='Timer in discord', description='Set a timer with operators of s, m, h, d for seconds, minutes, hours, or days', aliases=['tmr'])
@commands.has_any_role("Verified")
async def timer(ctx, Time):
    try:
        TimeParam = Time[::-1]
        length = len(Time)
        Time = Time[:-1]
        while length > 1:
            TimeParam = TimeParam[:-1]
            length = length - 1
        Time1 = Time
        timetype = ''
        Time = int(Time)
        if TimeParam == "s":
            Time = Time*1
            timetype = 'seconds'
        elif TimeParam == "m":
            Time = Time*60
            timetype = 'minutes'
        elif TimeParam == "h" :
            Time = Time*60*60
            timetype = 'hours'
        elif TimeParam == "d" :
            Time = Time*86400
            timetype = 'days'
        Time = str(Time)
        await ctx.send('Timer set for '+Time1+' '+timetype)
        message = await ctx.send(Time+' seconds left')
        Time = int(Time)
        Time = Time + 1
        while Time > 0:
            Time = Time - 1
            Time = str(Time)
            await message.edit(content=Time+' seconds left')
            Time = int(Time)
            time.sleep(1)
        await ctx.send(ctx.author.mention+' Timer up!!!!!!!!!!!!!!!!!!')
    except:
        await ctx.send('Sorry, but an error occoured in my code. Please try again')
#a timer that uses operators such as 10m, 1d, 3h

@bot.command(brief='ask if the bot is alive', description='Tells you if the bot is online, and the response speed', aliases=['pingthebot'])
@commands.has_any_role("Verified")
async def ping(ctx):
  try:
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")
  except:
    await ctx.send('Sorry, but an error occoured in my code. Please try again')
#latency commnd, returns in ms

@bot.command(brief='Bot programmer only, stops the bot program', description='dev only -_-', aliases=['shut', 'shutdown'])
@commands.has_any_role('moderator')
async def shutdownbot(ctx):
  if ctx.message.author.id == 739326255706406944 or 641422032495706170:
    message = await ctx.send('**⚠** Are you sure? **THIS PROCESS CANNOT BE CANCELLED! ⚠**\n', components=[[Button(label='Yes', custom_id='confirmed', style=int(3)), Button(label='No', custom_id='cancelled', style=int(4))]])
    confirmcancel = await bot.wait_for("button_click")
    if confirmcancel.component.custom_id == "cancelled":
      if ctx.author.id == confirmcancel.author.id:
        await confirmcancel.respond(type=6)
        await message.edit(content='Shutdown cancelled.')
        time.sleep(5)
        await message.delete()
      else:
        await message.edit(content= confirmcancel.author.mention+' You cannot press these buttons.')
        time.sleep(5)
        await message.delete()
        await ctx.invoke(ctx.bot.get_command('shutdownbot'))
    elif confirmcancel.component.custom_id == "confirmed":
      if ctx.author.id == confirmcancel.author.id:
        await confirmcancel.respond(type=6)
        Time = "5"
        await message.edit(content='Shutting down bot in '+Time+' seconds')
        Time = int(Time)
        while Time > 0:
          Time = str(Time)
          await message.edit(content= "Shutting down bot in "+Time+" seconds")
          Time = int(Time)
          Time = Time - 1
          time.sleep(1)
        await message.delete()
        await bot.change_presence(status= discord.Status.dnd, activity= discord.Game(name="⚠GOING OFFLINE⚠"))
        sys.exit('bot has been stopped.')
      else:
        await message.edit(content= confirmcancel.author.mention+' You cannot press these buttons.')
        time.sleep(5)
        await message.delete()
        await ctx.invoke(ctx.bot.get_command('shutdownbot'))
  else:
    ctx.send('Developer of the bot only, sorry >:)\n**-Glitchedcheses**')
#a remote shut down command to stop execution

@bot.command(brief='Spams a remind message after a set amount of time', description='Set a message and amount to spam remind, and set a time', aliases=['remind', 'rme'])
@commands.has_any_role("Verified")
async def remindme(ctx, Time, amountoftimes, *, Message):
    try:
        TimeParam = Time[::-1]
        length = len(Time)
        Time = Time[:-1]
        while length > 1:
            TimeParam = TimeParam[:-1]
            length = length - 1
        Time1 = Time
        timetype = ''
        Time = int(Time)
        if TimeParam == "s":
            Time = Time*1
            timetype = 'seconds'
        elif TimeParam == "m":
            Time = Time*60
            timetype = 'minutes'
        elif TimeParam == "h" :
            Time = Time*60*60
            timetype = 'hours'
        elif TimeParam == "d" :
            Time = Time*86400
            timetype = 'days'
        Time = str(Time)
        message = await ctx.send('Reminding you in '+Time1+' '+' seconds with the message: '+'**__'+Message+'__** __for__ ***'+amountoftimes+'*** __times__')
        Time = int(Time)
        Time = Time + 1
        while Time > 0:
            Time = Time - 1
            Time = str(Time)
            await message.edit(content='Reminding you in '+Time+' seconds with the message: '+'**__'+Message+'__** __for__ ***'+amountoftimes+'*** __times__')
            Time = int(Time)
            time.sleep(1)
            user = ctx.author
        amountoftimes = int(amountoftimes)          
        while amountoftimes > 0:
          await user.send(ctx.author.mention+' **YOU NEED TO DO:__ '+Message+'__**')
          amountoftimes = amountoftimes - 1
    except:
        await ctx.send('Sorry, but an error occoured in my code. Please try again')
#a command to remind a user after a amount of time, for a amount of times

@bot.command(brief='Suggust a feature to add to bot', description='Suggest a feature to bot', aliases=['suggest'])
@commands.has_any_role('Verified')
async def suggestions(ctx, *, feature):
  try:
    f = open("templates/suggestions.txt", "a")
    f.write("\n<br>Suggestion by: "+str(ctx.author)+', <br>\nSuggestion: '+feature+"\n<br>\n")
    f.close()
    await ctx.send('You suggested: **__'+feature+'__** and it is saved in my data banks for later review.')
  except:
    await ctx.send('Sorry, but an error occoured in my code. Please try again')

@bot.command(brief='Read or delete suggestions', description='r for read and c for clear', aliases=['viewsuggest', 'views'])
@commands.has_any_role('moderator')
async def viewsuggestions(ctx, action):
  try:
    if action == 'r':
      f = open("templates/suggestions.txt", "r")
      await ctx.send('```'+f.read(-1)+'```')
      f.close()
    elif action == 'c':
      F = open("templates/suggestions.txt", "r+")
      F.truncate(0)
      F.close()
      Ff = open("templates/suggestions.txt", "a")
      Ff.write('Suggestions:\n<br>\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n<br>')    
      Ff.close()

      await ctx.send('Cleared Suggestions!')
  except:
    await ctx.send('Sorry, but an error occoured in my code. Please try again')

@bot.command(brief='', description='', aliases=['calculate', 'cal'])
@commands.has_any_role('Verified')
async def calculator(ctx):
  try:
    await ctx.message.delete()
    user = str(ctx.author)
    equation = ''
    usercal = await ctx.send(str(ctx.author)+"'s calculator")
    screen = await ctx.send('```python\n'+equation+'\n```')
    group1 = await ctx.send('** **', components=[[Button(label='+', custom_id=user+'1', style=int(3)), Button(label='-', custom_id=user+'2', style=int(3)), Button(label='/', custom_id=user+'3', style=int(3)), Button(label='*', custom_id=user+'4', style=int(3)), Button(label='=', custom_id=user+'5', style=int(3))]])
    group2 = await ctx.send('** **', components=[[Button(label='1', custom_id=user+'6', style=int(1)), Button(label='2', custom_id=user+'7', style=int(1)), Button(label='3', custom_id=user+'8', style=int(1)), Button(label='4', custom_id=user+'9', style=int(1)), Button(label='5', custom_id=user+'10', style=int(1))]])
    group3 = await ctx.send('** **', components=[[Button(label='6', custom_id=user+'11', style=int(1)), Button(label='7', custom_id=user+'12', style=int(1)), Button(label='8', custom_id=user+'13', style=int(1)), Button(label='9', custom_id=user+'14', style=int(1)), Button(label='0', custom_id=user+'15', style=int(1))]])
    group4 = await ctx.send('** **', components=[[Button(label='(', custom_id=user+'16', style=int(1)), Button(label=')', custom_id=user+'17', style=int(1)), Button(label='.', custom_id=user+'18', style=int(1)), Button(label='Sqrt', custom_id=user+'23', style=int(1)), Button(label='Exp', custom_id=user+'24', style=int(1))]])
    group5 = await ctx.send('** **',components=[[Button(label='clr', custom_id=user+'19', style=int(2)), Button(label='Backspace', custom_id=user+'20', style=int(2)), Button(label='Type equation', custom_id=user+'21', style=int(3)), Button(label='CLOSE CAL', custom_id=user+'22', style=int(4))]])
    while True:
      button = await bot.wait_for('button_click')
      if user in button.component.custom_id: 
        if button.author.id == ctx.author.id:
          if button.component.custom_id == user+'6':
            await button.respond(type=6)
            equation = equation + '1'
            await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'7':
            await button.respond(type=6)
            equation = equation + '2'
            await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'8':
            await button.respond(type=6)
            equation = equation + '3'
            await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'9':
            await button.respond(type=6)
            equation = equation + '4'
            await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'10':
            await button.respond(type=6)
            equation = equation + '5'
            await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'11':
            await button.respond(type=6)
            equation = equation + '6'
            await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'12':
            await button.respond(type=6)
            equation = equation + '7'
            await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'13':
            await button.respond(type=6)
            equation = equation + '8'
            await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'14':
            await button.respond(type=6)
            equation = equation + '9'
            await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'15':
            await button.respond(type=6)
            equation = equation + '0'
            await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'1':
            await button.respond(type=6)
            equation = equation + '+'
            await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'2':
            await button.respond(type=6)
            equation = equation + '-'
            await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'3':
            await button.respond(type=6)
            equation = equation + '/'
            await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'4':
            await button.respond(type=6)
            equation = equation + '*'
            await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'5':
            await button.respond(type=6)
            try:
              if equation == '1+1':
                answer = 3
                equation = equation + '='
                await screen.edit(content='```python\n'+equation+''+str(answer)+'```')
                after1 = await bot.wait_for('button_click')
                await after1.respond(type=6)
                equation = ''
                await screen.edit(content='```python\n'+equation+'\n```')
              else:
                answer = eval(equation)
                equation = equation + '='
                await screen.edit(content='```python\n'+equation+''+str(answer)+'```')
                after1 = await bot.wait_for('button_click')
                await after1.respond(type=6)
                equation = ''
                await screen.edit(content='```python\n'+equation+'\n```')
            except:
              answer = 'undefined'
              equation = equation + '='
              await screen.edit(content='```python\n'+equation+''+str(answer)+'```')
              after2 = await bot.wait_for('button_click')
              await after2.respond(type=6)
              equation = ''
              await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'19':
            await button.respond(type=6)
            equation = ''
            await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'22':
            await button.respond(type=6)
            await screen.delete()
            await group1.delete()
            await group2.delete()
            await group3.delete()
            await group4.delete()
            await group5.delete()
            await usercal.delete()
            break
          elif button.component.custom_id == user+'20':
            await button.respond(type=6)
            equation = equation[:-1]
            await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'16':
            await button.respond(type=6)
            equation = equation + '('
            await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'17':
            await button.respond(type=6)
            equation = equation + ')'
            await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'18':
            await button.respond(type=6)
            equation = equation + '.'
            await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'21':
            await button.respond(type=6)
            pastemsg = await ctx.send('Enter an number/equation:')
            paste = await bot.wait_for('message')
            if paste.author.id == ctx.author.id:
              await paste.delete()
              await pastemsg.delete()
              equation = equation + str(paste.content)
              await screen.edit(content='```python\n'+equation+'\n```')
            else:
              Error = await ctx.send('error...')
              await pastemsg.delete()
              await Error.delete()
            continue
          elif button.component.custom_id == user+'23':
            await button.respond(type=6)
            equation = equation + 'sqrt('
            await screen.edit(content='```python\n'+equation+'\n```')
          elif button.component.custom_id == user+'24':
            await button.respond(type=6)
            equation = equation + '**'
            await screen.edit(content='```python\n'+equation+'\n```')
          
        else:
          await button.respond(content='Not your calculator!')
          continue
      else:
        continue
    
  except:
    await ctx.send('Sorry, but an error occoured in my code. Please try again')

@bot.command(brief='funni button', description='is funni button click me', aliases=['funni'])
@commands.has_any_role('Verified')
async def funnibutton(ctx):
  try:
    await ctx.message.delete()
    emojifromserver = bot.get_emoji(875944257515565057)
    message = await ctx.send('**CLICK ME**', components=[Button(label='Funni Button ', custom_id='funni', style=int(3), emoji=emojifromserver)])
    button = await bot.wait_for('button_click')
    if button.component.custom_id == 'funni':
      await button.respond(type=6)
      await message.edit(content=button.author.mention+'\n**__<:funni:875944257515565057> FUNNI:__\n A term used when talking about a meme, that is a video, because memes are pictures, and vines aren’t in style anymore, that awkward moment arises when you want to to say you have a “funni” to show to someone, that’s what it simply is. “Bruh check this out, lemme show you this funni”**')
      time.sleep(20)
      await message.delete()
  except:
    await ctx.send('Sorry, but an error occoured in my code. Please try again')

'''
@bot.command(brief='A voting/poll command, STILL UNDER DEV', description='Use this to make a poll or vote, STILL UNDER DEV', aliases=['vote'])
@commands.has_any_role('moderator')
async def poll(ctx, question, option1, option2):
    #try:
        print('>NEW POLL CREATED: '+question+', CREATED BY: '+str(ctx.author)+' WITH THE OPTIONS '+option1+' '+option2)
        await ctx.message.delete()
        poleselect = await ctx.send(str(ctx.author)+' poll:\n'+question+':\n', components=[Select(placeholder='Select a option', options=[SelectOption(label=option1, value='option1'), SelectOption(label=option2, value='option2')], custom_id=question)])
        vote1 = "0"
        vote2 = "0"
        message = await ctx.send('**VOTING: \n__'+option1+':__ '+vote1+' \n__'+option2+':__ '+vote2+'**', components=[Button(label='End poll/vote', custom_id=question, style=int(3))])
        voted = []
        while True:
          def waitclick():
            click = bot.wait_for('buttpn_click')

          def waitselect():
            select = bot.wait_for('select_option')
          threading.Thread(target=waitselect).start()
          threading.Thread(target=waitclick).start()
          import main
          if main.select.component.custom_id == question:
            if main.select.author.id in voted:
              await main.select.send(content='You already voted!')
            else:
              selected = main.select.values[0]
              if selected == 'option1':
                await main.select.send(content="You voted for: "+option1)
                print('>'+question+' POLL LOG: '+str(main.select.author)+' voted for '+option1)
              else:
                await main.select.send(content="You voted for "+option2)
                print('>'+question+' POLL LOG: '+str(main.select.author)+' voted for '+option2)
              voted.append(main.select.author.id)
              if main.select.values[0] == 'option1':
                vote1 = int(vote1)
                vote1 = vote1 + 1
                vote1 = str(vote1)
                await message.edit(content='**VOTING: \n__'+option1+':__ '+vote1+'** \n**__'+option2+':__ '+vote2+'**')
              elif main.select.values[0] == 'option2':
                vote2 = int(vote2)
                vote2 = vote2 + 1
                vote2 = str(vote2)
                await message.edit(content='**VOTING: \n__'+option1+':__ '+vote1+'** \n**__'+option2+':__ '+vote2+'**')
          elif main.click.component.custom_id == question:
              if main.click.author.id == ctx.author.id:
                await poleselect.delete()
                await message.delete()
                win = ''
                winvotes = ''
                if vote1 > vote2:
                  win = option1
                  winvotes = str(vote1)
                  await main.click.send(content='Pole ended and '+win+' won with '+winvotes+'!', ephemeral=False)
                elif vote2 > vote1:
                  win = option2
                  winvotes = str(vote2)
                  await main.click.send(content='Pole ended and '+win+' won with '+winvotes+'!', ephemeral=False)
                else:
                  win = 'Tie'
                  await main.click.send(content='Pole ended and a '+win+' happened so nither '+option1+' or '+option2+' won!', ephemeral=False)
                break
              else:
                await main.click.send('Not your poll')
              continue
    #except:
      #await ctx.send('Sorry, but an error occoured in my code. Please try again')
'''

@bot.command(brief='Sends a random meme', description='Send a random meme', aliases=['rmeme', 'randmeme'])
@commands.has_any_role('Verified')
async def randommeme(ctx):
  try:
    await ctx.send(embed=await pyrandmeme())
  except:
    await ctx.send('Sorry, but an error occoured in my code. Please try again')













def runsitefunc():
  import website

my_secret = os.environ['Token']
threading.Thread(target=bot.run(my_secret)).start()

#start bot


'''
@bot.command(brief='', description='', aliases=[''])
@commands.has_any_role('Verified')
async def Command(ctx):
  try:
    await ctx.send()
    
  except:
    await ctx.send('Sorry, but an error occoured in my code. Please try again')
'''
#a template for a command





'''
@bot.command(brief='', description='', aliases=['sure?'])
@commands.has_any_role('moderator')
async def areusure(ctx):
  message = await ctx.send("Are you sure?")
  await message.add_reaction("✅")
  await message.add_reaction("❌")

  check = lambda r, u: u == ctx.author and str(r.emoji) in "✅❌"

  try:
    reaction, user = await ctx.bot.wait_for("reaction_add", check=check, timeout=30)
  except asyncio.TimeoutError:
    await message.edit(content="False, timed out.")
    time.sleep(5)
    await message.delete()
    return

  if str(reaction.emoji) == "✅":
      await message.edit(content= "True.")
      time.sleep(5)
      await message.delete()
      return

  await message.edit(content="False.")
  time.sleep(5)
  await message.delete()
'''
#useful confirm system

'''
@bot.command()
async def select(ctx):
    await ctx.send(
        "Selects!",
        components=[
            Select(
                placeholder="Select something!",
                options=[
                    SelectOption(label="a", value="a"),
                    SelectOption(label="b", value="b"),
                ],
                custom_id="select1",
            )
        ],
    )

    interaction = await bot.wait_for(
        "select_option", check=lambda inter: inter.custom_id == "select1"
    )
    await ctx.send(f"{interaction.values[0]} selected!")
'''
#discord select box






'''
@bot.command(brief='Bot programmer only, stops the bot program', description='dev only -_-', aliases=['shut', 'shutdown'])
@commands.has_any_role('moderator')
async def shutdownbot(ctx):
  if ctx.message.author.id == 739326255706406944 or 641422032495706170:
    message = await ctx.send("**⚠** Are you sure? **THIS PROCESS CANNOT BE CANCELLED! ⚠**")
    await message.add_reaction("✅")
    await message.add_reaction("❌")

    check = lambda r, u: u == ctx.author and str(r.emoji) in "✅❌"

    try:
      reaction, user = await ctx.bot.wait_for("reaction_add", check=check, timeout=30)
    except asyncio.TimeoutError:
      await message.edit(content="Cancelled, timed out.")
      time.sleep(5)
      await message.delete()
      return

    if str(reaction.emoji) == "✅":
        await message.edit(content= "Warning, bot turning off in 10!")
        Time = 10
        while Time > 0:
          Time = str(Time)
          await message.edit(content= "Warning, bot turning off in "+Time+"!")
          Time = int(Time)
          Time = Time - 1
          time.sleep(1)
        await message.delete()
        await bot.change_presence(status=discord.Status.dnd,activity = discord.Game(name="⚠GOING OFFLINE⚠"))
        sys.exit('bot has been stopped.')
        return

    await message.edit(content="Cancelled!")
    time.sleep(5)
    await message.delete()
  else:
    await ctx.send('Developer of the bot only, sorry >:)\n**-Glitchedcheses**')
#a remote shut down command to stop execution
'''



'''
@bot.command()
async def button(ctx):
    message = await ctx.send('press to confirm: \n', components=[Button(label='confirm', custom_id="testbutton", style=int(1))])
    interaction = await bot.wait_for(
        "button_click", check=lambda inter: inter.custom_id == "testbutton"
    )
    await interaction.respond(type=6)
    await message.delete()
    await ctx.send(content=str(ctx.author.id)+' is your user id')
    '''