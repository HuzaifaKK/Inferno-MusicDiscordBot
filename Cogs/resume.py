import discord
from discord.ext import commands
import datetime

botname = 'Bot Name'


class resume(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='resume')
    async def resume(self, ctx: commands.Context):
        embed = discord.Embed(
            description='▶️ Resumed!',
            colour=discord.Colour.red()
        )
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{botname}')
        embed.set_author(name=ctx.author.name,
                         icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed, mention_author=False)
        await ctx.voice_client.resume()


def setup(client):
    client.add_cog(resume(client))
