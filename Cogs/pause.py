import discord
from discord.ext import commands
import datetime

botname = 'Bot Name'


class pause(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='pause')
    async def pause(self, ctx: commands.Context):
        embed = discord.Embed(
            description='⏸️ Paused!',
            colour=discord.Colour.red()
        )
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{botname}')
        embed.set_author(name=ctx.author.name,
                         icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed, mention_author=False)
        await ctx.voice_client.pause()


def setup(client):
    client.add_cog(pause(client))