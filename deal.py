import os
import discord

from emojize import Emojize

from dotenv import load_dotenv

from discord.ext import commands

def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')


    description = '''Bot to emote based on command text'''
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='/', description=description, intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')

        for guild in bot.guilds:
            if guild.name == GUILD:
                break

        print(
            f'{bot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

    @bot.command()
    async def emote(ctx, *, arg):
        await ctx.send(emojizer.emojize(arg))

    bot.run(TOKEN)

if __name__ == '__main__':
    emojizer = Emojize("cardiffnlp/twitter-roberta-base-emoji")
    main()