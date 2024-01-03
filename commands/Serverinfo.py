import discord
import random
from discord.ext import commands
from discord.utils import get
import time
import datetime
from itertools import cycle
import ast
import platform
import humanize as h
import psutil
import os
import cpuinfo
import speedtest

start_time = time.time(

)

title = "Bot Stats"
description = 'This Bot Is created By Dark Terra/Darth Demono'
colour = 0x800000


class Serverinfo(
    commands.Cog
):
    """
    Shows Server info
    """

    def __init__(
        self, client
    ):

        self.client = client

    @commands.command(
        aliases=[
            'Serverinfo',
            'Server'
        ],
        help='Shows Server info'
    )
    async def server(
        self, ctx
    ):
        try:
            server = ctx.message.guild

            roles = str(
                len(
                    server.roles
                )
            )
            emojis = str(
                len(
                    server.emojis
                )
            )
            channels = str(
                len(
                    server.channels
                )
            )

            embeded = discord.Embed(

            )

            embeded.title = "Darth Demono"
            embeded.description = "Server Info"
            embeded.color = 0xEE8700

            embeded.add_field(
                name="Created on:",
                value=server.created_at.strftime('%d %B %Y at %H:%M UTC+3'),
                inline=False
            )
            embeded.add_field(
                name="Server ID:",
                value=server.id,
                inline=False
            )
            embeded.add_field(
                name="Users on server:",
                value=server.member_count,
                inline=True
            )
            embeded.add_field(
                name="Server owner:",
                value=server.owner,
                inline=True
            )

            embeded.add_field(
                name="Server Region:",
                value=server.region,
                inline=True
            )
            embeded.add_field(
                name="Verification Level:",
                value=server.verification_level,
                inline=True
            )

            embeded.add_field(
                name="Role Count:",
                value=roles,
                inline=True
            )
            embeded.add_field(
                name="Emoji Count:",
                value=emojis,
                inline=True
            )
            embeded.add_field(
                name="Channel Count:",
                value=channels,
                inline=True
            )
            await ctx.send(
                embed=embeded
            )
        except Exception as err:
            await ctx.send(
                f"Excuse me, There is an Error =  {err}"
            )

    @commands.command(
        aliases=[
            'Uptime',
            'Bot-time'
        ],
        help='Shows bot uptime'
    )
    async def uptime(
        self, ctx
    ):
        try:
            current_time = time.time(

            )
            difference = int(
                round(
                    current_time - start_time
                )
            )
            text = str(
                datetime.timedelta(
                    seconds=difference
                )
            )
            embed = discord.Embed(

            )

            embed.colour = ctx.message.author.colour
            embed.add_field(
                name="⏳Uptime",
                value=text
            )
            embed.set_author(
                name=f'{self.client.user}',
                icon_url=self.client.user.avatar_url
            )
            try:
                await ctx.channel.send(
                    embed=embed
                )
            except discord.HTTPException:
                await ctx.channel.send(
                    f'⏳ Ive Been up for: `{text}`'
                )
        except Exception as err:
            await ctx.send(
                f"Excuse me, There is an Error =  {err}"
            )

    @commands.command(
        aliases=[
            'Ping',
            'latency'
        ],
        help='Shows Client Latency'
    )
    async def ping(
        self, ctx
    ):
        try:
            embed = discord.Embed(

            )
            embed.colour = 0x800000
            embed.add_field(
                name="⏳Bot-Ping",
                value=f'My ping is {self.client.latency}ms!'
            )
            await ctx.send(
                embed=embed
            )
        except Exception as err:
            await ctx.send(
                f"Excuse me, There is an Error =  {err}"
            )

    @commands.command(
        aliases=[
            'Binfo',
            'Bot-info'
        ],
        help='Gathers and displays Bot info'
    )
    async def botinfo(
        self, ctx
    ):
        try:
            current_time = time.time(

            )
            ping = f'My ping is {self.client.latency}!'

            difference = int(
                round(
                    current_time - start_time
                )
            )
            text = str(
                datetime.timedelta(
                    seconds=difference
                )
            )
            pythonVersion = platform.python_version(

            )
            clientVersion = '1.8.4'
            dpyVersion = discord.__version__
            serverCount = len(
                self.client.guilds
            )
            memberCount = len(
                set(
                    self.client.get_all_members(

                    )
                )
            )
            embed = discord.Embed(

            )

            embed.title = title
            embed.description = description
            embed.colour = colour

            embed.add_field(
                name='Bot Version:',
                value=clientVersion
            )
            embed.add_field(
                name='Python Version:',
                value=pythonVersion
            )
            embed.add_field(
                name='Discord.Py Version',
                value=dpyVersion
            )
            embed.add_field(
                name='Total Guilds:',
                value=serverCount
            )
            embed.add_field(
                name='Total Users:',
                value=memberCount
            )
            embed.add_field(
                name='Bot Creator:',
                value="<@687317057640857633>"
            )
            embed.add_field(
                name='Status:',
                value=discord.Status.online
            )
            embed.add_field(
                name="⏳Bot-Ping",
                value=ping,
                inline=False
            )
            embed.add_field(
                name="⏳Bot-Uptime",
                value=text,
                inline=False
            )
            await ctx.send(
                embed=embed
            )
        except Exception as err:
            await ctx.send(
                f"Excuse me, There is an Error =  {err}"
            )


def setup(
    client
):
    client.add_cog(
        Serverinfo(
            client
        )
    )
