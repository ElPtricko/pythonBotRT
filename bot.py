# AutoRole by elptricko#1234

import discord
from discord.ext import commands
from discord.ext.commands import Bot
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

bot.run("TOKEN")