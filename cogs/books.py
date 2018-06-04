""" Tomes! """
# unused import subprocess
# unused import sys
import random
import config as c

# unused import discord
from discord.ext import commands


class Books:
    """ Every Knight starts on the first Page """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def startstudies(self, ctx):
        """ Begin your journey to knighthood!
            >startstudies
        """
        userid = ctx.message.author.id
        if userid == c.owner_id or userid in str(c.dev_id):
            await self.bot.say('*Goodbye.*')
            await self.bot.logout()
        else:
            await self.bot.say('*Insufficient privileges*')


def setup(bot):
    """ defines setup """
    bot.add_cog(Books(bot))