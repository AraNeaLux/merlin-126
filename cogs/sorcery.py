""" Sorcery! """
# unused import subprocess
# unused import sys
import os
import random
import config as c

# unused import discord
from discord.ext import commands


class Sorcery:
    """ Of the Highest Order """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def exorcise(self, ctx):
        """ Casts out the spirits in Relics.
            >exorcise
        """
        userid = ctx.message.author.id
        if userid == c.owner_id:
            await self.bot.say('*Goodbye.*')
            await self.bot.logout()
        else:
            resp = ['*You try to cast this spell, yet the magic eludes your grasp.*',
                    'Your petty machinations are powerless against me!',
                    'Pardon, I didn\'t quite catch that',
                    '*No effect*',
                    'Did you say something?']
            srandom = random.SystemRandom()
            await self.bot.say(srandom.choice(resp))

    @commands.command(pass_context=True)
    async def housekeeping(self, ctx, amount: str):
        """ Clutter is always inexcuseable.
            >housekeeping <@user | amount_integer | 'all'>
        """
        userid = ctx.message.author.id
        usid = int(amount.replace('<@', '').replace('>', ''))
        if userid == c.owner_id or userid in str(c.dev_id):
            await self.bot.delete_message(ctx.message)
            if '<@' in amount and '>' in amount:
                async for amount in self.bot.logs_from(ctx.message.channel):
                    if amount not in self.bot.logs_from(ctx.message.channel):
                        return
                    else:
                        await self.bot.delete_message(ctx.message.id == usid)
            elif amount == str('all'):
                deleted = await self.bot.purge_from(ctx.message.channel, limit=750)
                await self.bot.say('Bulk purged **{}** Messages'.format(len(deleted)))
                async for msg in self.bot.logs_from(ctx.message.channel):
                    await self.bot.delete_message(msg)
            elif int(amount) > 0:
                counter = 0
                for counter in range(int(amount)):
                    async for msg in self.bot.logs_from(ctx.message.channel):
                        if int(counter) >= int(amount):
                            return
                        else:
                            await self.bot.delete_message(msg)
                        counter += 1
            else:
                print('purge error on else')
        else:
            await self.bot.say('*Insufficient privileges*')
#    @commands.command(pass_context=True)
#    async def startstudies(self, ctx):
def setup(bot):
    """ defines setup """
    bot.add_cog(Sorcery(bot))