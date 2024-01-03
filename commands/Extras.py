import discord
import random
from discord.ext import commands
from discord.utils import get
import time
import datetime
import psutil
from itertools import cycle
import typing
import operator

start_time = time.time()

clientid = "890284361176449066"

blink = "<https://discordapp.com/oauth2/authorize?&client_id=YOUR_CLIENTID_HERE&scope=bot&permissions=YOUR_VALUE_HERE>"

boturl = f"[Click me!](https://discord.com/api/oauth2/authorize?client_id={clientid}&permissions=8&scope=bot)"


class Extras(commands.Cog):
    """
    Extra Miscellaneous Commands
    """

    def __init__(self, client):
        self.client = client

    @commands.command(
        aliases=["Baselink", "Blink", "base_url"],
        help="Gives Baselink"
    )
    async def baselink(self, ctx):
        try:
            await ctx.send(blink)
        except Exception as err:
            await ctx.send(f"Excuse me, There is an Error =  {err}")

    @commands.command(
        aliases=["Embed"],
        help="Gives an Embed"
    )
    async def embed(
        self, ctx
    ):
        try:
            embed = discord.Embed()
            embed.title = "Here"
            embed.description = "This is an Embed"
            await ctx.send(embed=embed)
        except Exception as err:
            await ctx.send(
                f"Excuse me, There is an Error =  {err}"
            )

    @commands.command(
        aliases=["hello", "HelloThere"],
        help="Responds to Hello There"
    )
    async def hellothere(self, ctx):
        try:
            await ctx.send("General Kenobi")
        except Exception as err:
            await ctx.send(f"Excuse me, There is an Error =  {err}")

    @commands.command(
        aliases=["liquid", "99bottles"],
        help="99 bottles of liquid"
    )
    async def bottles(self, ctx, amount: typing.Optional[int] = 99, *, liquid="beer"):
        try:
            await ctx.send("{} bottles of {} on the wall!".format(amount, liquid))
        except Exception as err:
            await ctx.send(f"Excuse me, There is an Error =  {err}")

    @commands.command(
        aliases=["Reply"],
        help="Send the Same Stuff that You Said"
    )
    async def reply(self, ctx, *, arg):
        try:
            await ctx.send(f"{arg}")
        except Exception as err:
            await ctx.send(f"Excuse me, There is an Error =  {err}")

    @commands.command(
        aliases=["Multiply", "Multiplication"],
        help="Does Multiplication"
    )
    async def multiply(self, ctx, a: int, b: int):
        try:
            await ctx.send(a * b)
        except Exception as err:
            await ctx.send(f"Excuse me, There is an Error =  {err}")

    @commands.command(
        aliases=["subtract", "Subtraction"],
        help="Does Subtraction"
    )
    async def sub(self, ctx, a: int, b: int):
        try:
            await ctx.send(a - b)
        except Exception as err:
            await ctx.send(f"Excuse me, There is an Error =  {err}")

    @commands.command(
        aliases=["Divide", "Division"],
        help="Does Division"
    )
    async def divide(self, ctx, a: int, b: int):
        try:
            await ctx.send(a / b)
        except Exception as err:
            await ctx.send(f"Excuse me, There is an Error =  {err}")

    @commands.command(
        aliases=["Addition", "Add"],
        help="Does Addition"
    )
    async def add(self, ctx, a: int, b: int):
        try:
            await ctx.send(a + b)
        except Exception as err:
            await ctx.send(f"Excuse me, There is an Error =  {err}")

    @commands.command(
        aliases=["uinfo", "whois", "profile"],
        help="Gathers and Displays user info"
    )
    async def userinfo(self, ctx):
        try:
            perms = []
            for user in ctx.message.mentions:
                member = user
            if not ctx.message.mentions:
                member = ctx.author
            for perm in ctx.channel.permissions_for(member):
                if perm[1]:
                    name = perm[0]
                    perms.append(name)
                else:
                    pass
            permsd = list(dict.fromkeys(perms))
            roles = []
            for role in member.roles:
                roles.append(role.name)

            def joinpos(user, guild):
                try:
                    joins = tuple(
                        sorted(guild.members, key=operator.attrgetter("joined_at")))
                    if None in joins:
                        return None
                    for key, elem in enumerate(joins):
                        if elem == user:
                            return key + 1, len(joins)
                    return None
                except Exception as error:
                    print(error)
                    return None

            joined = joinpos(member, ctx.guild)

            def checkfornitro(user):
                if user.is_avatar_animated():
                    return True
                else:
                    return False

            isnitro = checkfornitro(member)

            embed = discord.Embed(
                title=f"{member.name}",
                colour=member.colour
            )
            embed.add_field(
                name="joined server",
                value=f"{member.joined_at}",
                inline=True
            )
            embed.add_field(
                name="joined discord",
                value=f"{member.created_at}",
                inline=True
            )
            embed.add_field(
                name=f"Roles({len(roles)})",
                value=", @".join(roles),
                inline=False
            )
            embed.add_field(
                name="permissions",
                value=", ".join(permsd),
                inline=False
            )
            embed.add_field(
                name="Nickname",
                value=f"{member.display_name}"
            )
            embed.add_field(
                name="Tag",
                value=f"#{member.discriminator}",
                inline=True
            )
            embed.add_field(
                name="nitro?",
                value=f"{isnitro}"
            )
            embed.add_field(
                name="id",
                value=f"{member.id}"
            )

            embed.set_thumbnail(
                url=member.avatar_url
            )

            await ctx.channel.send(
                embed=embed
            )
        except Exception as err:
            await ctx.send(f"I can't Send Userdata because {err}")


def setup(client):
    client.add_cog(Extras(client))
