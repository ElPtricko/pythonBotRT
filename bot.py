import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is oooon!")
    await client.change_presence(game=None, status=None, afk=False)

@client.event 
async def on_member_join(member):
    await client.add_roles(member, "member")
    print("Added role member to " + member)

client.run()