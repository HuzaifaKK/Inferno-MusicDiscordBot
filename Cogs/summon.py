import discord
from discord.ext import commands
import datetime

botname = 'Bot Name'


class summon(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='summon')
    async def summon(self, ctx: commands.Context):
        destination = ctx.message.author.voice.channel
        if ctx.voice_client is None:
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
            await ctx.voice_client.move_to(destination)
            embed = discord.Embed(
                description='✅ Bot summoned to your VC',
                colour=discord.Colour.red()
            )
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{botname}')
            embed.set_author(name=ctx.author.name,
                             icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed, mention_author=False)

    @summon
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
    client.add_cog(summon(client))
