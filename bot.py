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