import discord
import datetime
from discord.ext import commands

botname = 'Bot Name'


class join(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx: commands.Context):
        destination = ctx.message.author.voice.channel
        if ctx.voice_client is None:
            embed = discord.Embed(
                description='✅ Successfully Joined The VC',
                colour=discord.Colour.red()
            )
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{botname}')
            embed.set_author(name=ctx.author.name,
                             icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed, mention_author=False)
            await destination.connect()
        else:
            embed = discord.Embed(
                description='❎ Error! Bot is already in a VC',
                colour=discord.Colour.red()
            )
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{botname}')
            embed.set_author(name=ctx.author.name,
                             icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed, mention_author=False)

    @join.before_invoke
    async def ensure_voice_state(self, ctx: commands.Context):
        if not ctx.author.voice or not ctx.author.voice.channel:
            embed = discord.Embed(
                description='❎ Error! You are not connected to any VC',
                colour=discord.Colour.red()
            )
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{botname}')
            embed.set_author(name=ctx.author.name,
                             icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed, mention_author=False)


def setup(client):
    client.add_cog(join(client))
