import discord
import random, os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='%', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
list1 = ["glass to the green bin","plastic to the yellow bin","non-recyclable materials to the orange bin","banana and orange peel to the brown bin","paper to the blue bin"]
@bot.command()
async def bio(ctx):
    fact = random.choice(list1)
    await ctx.send(fact)


@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')
@bot.command()
async def grin(ctx):
    await ctx.send('😁')
@bot.command()
async def slightly_smiling_face(ctx):
    await ctx.send('🙂')
@bot.command()
async def neutral_face(ctx):
    await ctx.send('😐')
@bot.command()
async def white_frowning_face(ctx):
    await ctx.send('☹')
@bot.command()
async def sob(ctx):
    await ctx.send('😭')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def mem(ctx):
    meme = random.choice(os.listdir('memes'))
    with open(f'memes/{meme}','rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    

bot.run('MTAyMDk4NzEzMzQzNzE2MTU1Mg.GvEe5J.4XR7Irk-5HPef4nkM9Hf2REXkQLLh-mgyMsEtg')