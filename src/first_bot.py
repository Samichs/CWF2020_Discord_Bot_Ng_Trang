'''
Oct 24, 2020

Discord bot by Kyle Ng and Dennis Trang

Requires .env for bot token and server ID

To Do:
* Display current poll
* Update poll embed on reaction
* Close poll?
* Weather report (from Google Weather?)
* Kick command
* Coin flip
* Roll dice
'''
import os

from dotenv import load_dotenv

import discord
from discord.ext import commands

poll_emojis = {
    1:"1️⃣",
    2:"2️⃣",
    3:"3️⃣",
    4:"4️⃣",
    5:"5️⃣",
    6:"6️⃣",
    7:"7️⃣",
    8:"8️⃣",
    9:"9️⃣"
}

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

# @bot.command(name='create_poll', help='Create a new poll')
# async def create_poll(ctx, question: str, option_1: str, option_2: str):
#     poll_embed = discord.Embed(
#         title = question
#     )
#     poll_embed.add_field(name="1️⃣ "+option_1, value="\u200b", inline=False)
#     poll_embed.add_field(name="2️⃣ "+option_2, value="\u200b", inline=False)
#     poll_embed.set_footer(text="Choose with the reactions below!")

#     embedded = await ctx.send(embed=poll_embed)
#     await embedded.add_reaction(emoji="1️⃣")
#     await embedded.add_reaction(emoji="2️⃣")

@bot.command(name="create_big_poll", help="Create a new poll")
async def create_poll(ctx, *args):
    question = args[0]
    options = args[1:]

    if len(options) > 9:
        await ctx.send("Error: please use less than 9 options for your poll")
        return
    if len(options) < 2:
        await ctx.send("Error: please use at least two options for your poll")
        return

    poll_embed = discord.Embed(
        title = question
    )
    poll_embed.set_footer(text="Choose with the reactions below!")

    for i in range(1,len(options)+1):
        poll_embed.add_field(name=poll_emojis[i]+ " " + options[i-1], value="\u200b", inline=False)
    
    embedded = await ctx.send(embed=poll_embed)

    for i in range(1, len(options)+1):
        await embedded.add_reaction(emoji=poll_emojis[i])


bot.run(TOKEN)