import discord
from discord.ext import commands
import datetime

botname = 'Bot Name'

class leave(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def leave(self, ctx: commands.Context):
        if not ctx.guild.voice_client:
            embed = discord.Embed(
                description='❎ Error! Bot is not connected to any VC',
                colour=discord.Colour.red()
            )
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{botname}')
            embed.set_author(name=ctx.author.name,
                             icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.voice_client.disconnect()
            embed = discord.Embed(
                description='✅ Successfully Left The VC',
                colour=discord.Colour.red()
            )
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{botname}')
            embed.set_author(name=ctx.author.name,
                             icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed, mention_author=False)
            await ctx.voice_client.disconnect()


def setup(client):
    client.add_cog(leave(client))
