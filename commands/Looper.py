# Importing Libraries
import discord
import random
from discord.ext import commands, tasks
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
from googleapiclient import build
import requests
import urllib.request
import json
from Setup import *

start_time = time.time(

)

# Adding Looper Extension


class Looper(
    commands.Cog
):
    # Looper Help
    """
    <#785534035442794516> Task Loop Command.
    """
# Defining __init__ file

    def __init__(
        self, client
    ):
        self.client = client

# Tasks Loop
    @tasks.loop(

    )
    async def my_task(
        self,
        hidden=True
    ):
        try:
            try:
                await self.client.change_presence(
                    activity=discord.Activity(
                        name=f"{len(self.client.users)} users|$help",
                        type=discord.ActivityType.watching
                    )
                )
            except:
                pass

            # Defining Strings inside The Task Loop.
            url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}"
            yt = f"[**Channel**](https://www.youtube.com/channel/UCZWHlAP_dcw9Rnxgao9mxuA)"
            instagram = f"[**Instagram**](https://www.instagram.com/darthdemono/)"
            subscriberCount = "subscriberCount"
            inv = f"[**Invite**](https://discord.gg/xRWYVCsw6P)"
            # Main Channel
            channel = self.client.get_channel(
                # 785534035442794516
                794179085152157710
            )
            # Main Server
            server = self.client.get_guild(
                # 785150310896107552
                794179085152157706
            )
            # Main Message
            message = await channel.fetch_message(
                # 785534302544068638
                833405096431583266
            )
            # Instagram Api String Setup
            igurl = 'https://www.instagram.com/darthdemono/'
            r = requests.get(igurl).text

            # Instagram Follower Count
            start = '"edge_followed_by":{"count":'
            end = '},"fbid":"17841431103138574"'
            followers = r[r.find(start) + len(start):r.rfind(end)]
            # Instagram Following Count
            start = '"edge_follow":{"count":'
            end = '},"follows_viewer"'
            following = r[r.find(start) + len(start):r.rfind(end)]
            # Instagram Posts Count
            start = '"edge_owner_to_timeline_media":{"count":'
            end = ',"page_info":{"has_next_page":false,"end_cursor":null},"edges":[]},"edge_saved_media"'
            post = r[r.find(start) + len(start):r.rfind(end)]

            # YouTube Api String Setup
            # YT uRl Data
            data = urllib.request.urlopen(
                url
            ).read(

            )
            # YouTube Subscriber Count
            subs = json.loads(
                data)["items"][0]["statistics"]["subscriberCount"]
            # Youtube Views Count
            views = json.loads(data)["items"][0]["statistics"]["viewCount"]
            # Youtube Video Count
            vids = json.loads(data)["items"][0]["statistics"]["videoCount"]

            # Server Roles
            roles = str(
                len(
                    server.roles
                )
            )
            # Server Roles
            emojis = str(
                len(
                    server.emojis
                )
            )
            # Current Time
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

            serverCount = len(
                self.client.guilds
            )
            memberCount = len(
                set(
                    self.client.get_all_members(

                    )
                )
            )

            # The Actual Looping Embed
            embed = discord.Embed(

            )

            embed.title = title
            embed.description = description
            embed.colour = colour

            embed.add_field(
                name="**Server info Given Below = **",
                value="** **",
                inline=False
            )

            embed.add_field(
                name="Server ID:",
                value=server.id,
                inline=False
            )
            embed.add_field(
                name="Total Users on server:",
                value=server.member_count,
                inline=True
            )
            embed.add_field(
                name="Server owner:",
                value="<@687317057640857633>",
                inline=True
            )

            embed.add_field(
                name="Server Role Count:",
                value=roles,
                inline=True
            )

            embed.add_field(
                name="**Bot info Given Below = **",
                value="** **",
                inline=False
            )

            embed.add_field(
                name='Bot Creator:',
                value="<@687317057640857633>",
                inline=True
            )
            embed.add_field(
                name='Status:',
                value=discord.Status.online,
                inline=True
            )

            embed.add_field(
                name="Help Command : ",
                value="`$help`",
                inline=True
            )

            embed.add_field(
                name="⏳Bot-Uptime",
                value=f"Ive been Running for {text}",
                inline=False
            )

            embed.add_field(
                name="YouTube Statistics = ",
                value="** **",
                inline=False
            )

            embed.add_field(
                name="Subscriber Count",
                value=f"{subs} Subscribers",
                inline=True
            )

            embed.add_field(
                name="View Count",
                value=f"{views} Views",
                inline=True
            )

            embed.add_field(
                name="Video Count",
                value=f"{vids} Videos",
                inline=True
            )

            embed.add_field(
                name="Instagram Statistics = ",
                value="** **",
                inline=False
            )

            embed.add_field(
                name="Instagram Followers",
                value=f"{followers} Followers",
                inline=True
            )

            embed.add_field(
                name="Instagram following",
                value=f"{following} following",
                inline=True
            )

            embed.add_field(
                name="Instagram Posts",
                value=f"{post} Posts",
                inline=True
            )

            embed.add_field(
                name="Instagram ID",
                value=instagram,
                inline=True
            )

            embed.add_field(
                name="Youtube Channel",
                value=yt,
                inline=True
            )

            embed.add_field(
                name="Discord Invite",
                value=inv,
                inline=True
            )

            await message.edit(
                embed=embed
            )
        except Exception as err:
            fail = self.client.get_channel(
                # 786227373418479637
                794179085152157710
            )
            await fail.send(
                f'{err}'
            )

    # Tasks Loop Start at Bot Startup
    @commands.Cog.listener(

    )
    async def on_ready(
        self
    ):
        self.my_task.start(

        )


# The Loop Setup


def setup(
    client
):
    client.add_cog(
        Looper(
            client
        )
    )
