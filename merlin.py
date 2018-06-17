""" Merlin """
import os
import atexit
import discord
from discord.ext import commands
import config as c
import random
import asyncio
import math

STARTUP_EXTENSIONS = [
					  'cogs.charms',
                      'cogs.sorcery',
                      ]

bot = commands.Bot(command_prefix=c.prefix, description=c.description, pm_help=True)
bot.remove_command('help')

@bot.event
async def on_ready():
    """ Returns true if bot is ready.
    """
    clear = lambda: os.system('cls')
    clear()
    print('-' * len(bot.user.id))
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print(' ')
    print('Bot currently running on {} servers:'.format(len(bot.servers)))
    for s in bot.servers:
        print(' - ' + s.name + ' :: ' + s.id)
    print('-' * len(bot.user.id))
    print(' ')

    await bot.change_presence(game=discord.Game(name=c.game))

    file = open('config.py', 'r')
    cont = file.read()
    if 'token' not in cont:
        file = open('config.py', 'w')
        file.write('# merlin.py config \ntoken = \'\'')
    else:
        file.close()


@bot.command()
async def help():
        embed = discord.Embed(title="General Aid", description="How might I help you?", colour=0x1abc9c)

        embed.add_field(name="//help", value="Well that's a tad redundant.", inline=False)
        embed.add_field(name="//info", value="A bit of general information about myself.", inline=False)
        embed.add_field(name="//sorcery", value="Shows a list of higher magics.", inline=False)
        embed.add_field(name="//charms", value="Shows a list of basic charms useable by many.", inline=False)
        embed.add_field(name="//books", value="Books are invaluable to a Page's studies.", inline=False)
        embed.add_field(name="//training", value="All Squires ought to train diligently.", inline=False)

        await bot.say(embed=embed)

@bot.command()
async def info():
    embed = discord.Embed(title="General Information", description="Let me tell you a bit about myself.", colour=0x1abc9c)

    embed.add_field(name="Prefix:", value="All of my magic is called upon using the prefix /'//./' "
                                          "As for that little hoodlum Pirrip, I haven't a clue.", inline=False)
    embed.add_field(name="About Me, Merlin:", value="Well that's a tad redundant.", inline=False)

@bot.command()
async def sorcery():
    embed = discord.Embed(title="Sorcery", description="The higher magics", colour=0x1abc9c)

    embed.add_field(name="//exorcise", value="Casts out the spirits in Relics.", inline=False)
    embed.add_field(name="//hosuekeeping [int]", value="Clutter is always inexcuseable", inline=False)

    await bot.say(embed=embed)

@bot.command()
async def charms():
    embed = discord.Embed(title="Charms", description="A touch of Magic", colour=0x1abc9c)

    embed.add_field(name="//poke *<@user>*", value="If you truly must...", inline=False)
    embed.add_field(name="//hug ", value="*Clutter is always inexcuseable*", inline=False)

    await bot.say(embed=embed)

@bot.command()
async def initiate(extension_name: str):
    """ Loads an extension.
        >load <extension_name>
    """
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as exopt:
        await bot.say('```py\n{}: {}\n```'.format(type(exopt).__name__, str(exopt)))
        return
    await bot.say('I have rerouted the EME to include {}.'.format(extension_name))


@bot.command()
async def drain(extension_name: str):
    """ Unloads an extension.
        >unload <extension_name>
    """
    bot.unload_extension(extension_name)
    await bot.say('I have rerouted the EME away from {}.'.format(extension_name))


@bot.command()
async def reload(extension_name: str):
    """ Loads an extension.
        >reload <extension_name>
    """
    try:
        bot.unload_extension(extension_name)
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as exopt:
        await bot.say('```py\n{}: {}\n```'.format(type(exopt).__name__, str(exopt)))
        return
    await bot.say('I have rerouted the EME to send an extra surge to {}.'.format(extension_name))

"""
@bot.event
async def on_message(message):
    \""" No swear words please.
    \"""
    try:
        if message.author == bot.user:
            return
        if any(word in message.content for word in c.swears):
            await bot.send_file(message.channel, 'img/christ.jpg')
        wordsls = ['meme review']
        if any(word in message.content for word in wordsls):
            await bot.say(':clap: :clap:')
        if any(word in message.content for word in c.mention):
            print(message.author.name + ' ' + message.author.mention + ' :: ' + message.server.name + ' :: ' + message.content)
    except:
        pass
    finally:
        if '>>' in message.content[:2]:
            return
        elif c.prefix in message.content[:1]:
            print(message.author.name + ' ' + message.author.mention + ' :: ' + message.server.name + ' :: ' + message.content)
    await bot.process_commands(message)
    """

if __name__ == '__main__':
    for extension in STARTUP_EXTENSIONS:
        try:
            bot.load_extension(extension)
        except Exception as exopt:
            exc = '{}: {}'.format(type(exopt).__name__, exopt)
            print('The EME is not responding to {}\n{}'.format(extension, exc))

    bot.run(c.token)


def exit_handler():
    """ What to do on exit.
    """
    print(' ')
    print('exiting...')


atexit.register(exit_handler)