import discord
from discord.ext import commands

# sounds like this is the how to tell it's a command ( eg: .gimmeMoney )
client = commands.Bot( command_prefix = '.' )

@client.event
async def on_ready():
    print( "Bot is ready" )

# @client.command()


with open("bot_Token.txt","r") as f:
    string = f.read()
    token = str( string )

client.run( token )