<<<<<<< HEAD
from discord.ext import commands
from discord.ext.commands import Bot
import discord
import asyncio

client = discord.Client()
server = discord.Server
user = discord.Member

bot = Bot(command_prefix="?")

@bot.event
async def on_ready():
    print("Bot is oooon!")
    await bot.change_presence(game=None, status=None, afk=False)

@bot.event
async def on_member_join(member):
    await client.add_roles(member, "member")
    print("Added role member to " + member)
=======
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

bot.run("")

>>>>>>> Modfified most of the code.
