import discord
from discord.ext import commands
import datetime

botname = 'Bot Name'


class stop(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='stop')
    async def _stop(self, ctx: commands.Context):
        embed = discord.Embed(
            description=f'✅ Stopped the song', colour=discord.Colour.red())
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{botname}')
        embed.set_author(name=ctx.author.name,
                         icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed, mention_author=False)
        ctx.voice_client.stop()


def setup(client):
    client.add_cog(stop(client))
