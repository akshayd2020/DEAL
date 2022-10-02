import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')

    description = '''Bot to emote based on command text'''
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='/', description=description, intents=intents)
    # client = discord.Client(intents=discord.Intents.all())

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
    @bot.event
    async def on_message(message):
        print(f'{message.content}\n')
        await bot.process_commands(message)

    @bot.command()
    async def emote(ctx, *, arg):
        await ctx.send(arg)

    bot.run(TOKEN)

if __name__ == '__main__':
    main()