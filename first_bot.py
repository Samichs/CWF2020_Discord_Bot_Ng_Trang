import os

from dotenv import load_dotenv

import discord
from discord.ext import commands

#Load in bot auth and server tokens
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#Define command prefix
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send("heyo!")

@bot.command(name='create_poll', help='Create a new poll')
async def create_poll(ctx, question: str, option_1: str, option_2: str):
    # response = question + "\n"
    # response += ":one: " + option_1 + "\n"
    # response += ":two: " + option_2 + "\n"

    # poll_message = await ctx.send(response)
    # await poll_message.add_reaction(emoji="1️⃣")
    # await poll_message.add_reaction(emoji="2️⃣")
    print("new poll created!")

    poll_embed = discord.Embed(
        title = question
    )
    poll_embed.add_field(name="1️⃣ "+option_1, value="\u200b", inline=False)
    poll_embed.add_field(name="2️⃣ "+option_2, value="\u200b", inline=False)

    embedded = await ctx.send(embed=poll_embed)
    await embedded.add_reaction(emoji="1️⃣")
    await embedded.add_reaction(emoji="2️⃣")


bot.run(TOKEN)