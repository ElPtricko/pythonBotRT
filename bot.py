# AutoRole by elptricko#1234

import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="+")

user = discord.Member
server = discord.Server
client = discord.Client

@bot.event
async def on_ready():
    print ("Le bot is oooon!")

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Members')
    await bot.add_roles(member, role)
    print ("Added role Member to user: " + str(member))

@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    async for msg in bot.logs_from(channel, limit=int(amount+1)):
        await bot.delete_message(msg)
    await bot.say("I'm awesome so I deleted %d messages for you, YAY!" % amount)

@bot.command(pass_context=True)
async def warn(ctx, usr, *msg):
    channel = ctx.message.channel
    async for message in bot.logs_from(channel, limit=int(1)):
        await bot.delete_message(message)
    stringForYou = ""
    for word in msg:
        stringForYou += " " + word    
    await bot.say("%s, %s" % (usr, stringForYou))

bot.run("TOKEN")