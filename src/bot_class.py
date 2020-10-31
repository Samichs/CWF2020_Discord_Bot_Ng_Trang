'''
Oct 24, 2020

Discord bot by Kyle Ng and Dennis Trang

Requires .env for bot token and server ID

To Do:
* Create a poll
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
    1:"1️⃣",    2:"2️⃣",    3:"3️⃣",    4:"4️⃣",    5:"5️⃣",    6:"6️⃣",    7:"7️⃣",    8:"8️⃣",    9:"9️⃣"
}

class MyBot:

    def __init__(self):
        self.bot = commands.Bot(command_prefix='!')
        self.load_commands()

        self.TOKEN = None
        self.GUILD = None
        self.load_env()

        self.current_poll = None


    def load_env(self):
        load_dotenv()
        self.TOKEN = os.getenv('DISCORD_TOKEN')
        self.GUILD = os.getenv('DISCORD_GUILD')

    def clear_poll(self):
        self.current_poll = None

    def load_commands(self):
        @self.bot.event
        async def on_ready():
            print(f'{self.bot.user.name} has connected to Discord!')

        @self.bot.command(name='hello', help="Say hello!")
        async def hello(ctx):
            await ctx.send("heyo!")

        @self.bot.command(name="create_poll", help="Create a new poll")
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
            self.current_poll = embedded

            for i in range(1, len(options)+1):
                await embedded.add_reaction(emoji=poll_emojis[i])
        
        @self.bot.command(name="current_poll", help="Show the current poll")
        async def current_poll(ctx):
            if self.current_poll == None:
                await ctx.send("There is no poll currently open.")
                return

            poll_message = await ctx.fetch_message(self.current_poll.id)
            poll_reactions = poll_message.reactions
            
            await poll_message.delete()
            new_poll = await ctx.send(embed=poll_message.embeds[0])
            self.current_poll = new_poll

            for react in poll_reactions:
                    await new_poll.add_reaction(emoji=react.emoji)

        @self.bot.command(name="close_poll", help="Close the current poll")
        async def close_poll(ctx):
            if self.current_poll == None:
                await ctx.send("There is no poll currently open.")
                return

            self.current_poll = None
            await ctx.send("Current poll has been closed.")


    
if __name__ == "__main__":
    my_bot = MyBot()
    my_bot.bot.run(my_bot.TOKEN)