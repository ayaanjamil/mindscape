import discord
from discord.ext import commands
import asyncio

global pounce
pounce = 1

global buzz
buzz = 1

bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready():
    print('online')
    await bot.change_presence(status=discord.Status.online,
                                 activity=discord.Activity(type=discord.ActivityType.playing, name='Quiz'))


@bot.command()
async def ps(ctx):
    if ctx.author.id == ayaan:
        global pounce
        pounce = 0
        await ctx.send('Pounce open')
    else:
        return


@bot.command()
async def p(ctx):
    global pounce
    if pounce == 0:
        pouncer = str(ctx.author.id)
        msg = str('<@'+pouncer+'> has pounced.')
        await ctx.send(msg)

    elif pounce == 1:
        await ctx.send('pounce closed')


@bot.command()
async def pe(ctx):
    if ctx.author.id == ayaan:
        global pounce
        pounce = 1
        await ctx.send('pounce closed')


@bot.command()
async def bs(ctx):
    if ctx.author.id == ayaan:
        global buzz
        buzz = 0
        await ctx.send('buzzer open')
    else:
        return


@bot.command()
async def b(ctx):
    global buzz
    if buzz == 0:
        buzz = 1
        buzzer = str(ctx.author.id)
        msg = str('<@'+buzzer+'> has buzzed.')
        message = await ctx.send(msg)
        await asyncio.sleep(1)
        await message.edit(content="<@"+buzzer+">, tell the answer within 10 seconds.")

    elif buzz == 1:
        await ctx.send('cant buzz now')


@bot.command(pass_context=True)
async def nick(ctx, member: discord.Member, *, newnick):
    if ctx.message.author.id == ayaan:
        await member.edit(nick=newnick)
        await ctx.send(f'Nickname was changed for {member.mention}.')
    else:
        await ctx.send('Only organizers can use this command.')


bot.run(TOKEN)
