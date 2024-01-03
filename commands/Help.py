import discord
import random
from discord.ext import commands
from discord.utils import get


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        aliases=["Help", "Helpme"],
        help="Help command to get started on using the bot!"
    )
    async def help(self, ctx, *cog):
        """Gets all cogs and commands of mine."""
        try:
            if not cog:
                """Cog listing.  What more?"""
                halp = discord.Embed()
                halp.title = "Help!"
                halp.description = "Use `>help *category*` to see all the commands!"
                halp.colour = 0x800000
                cogs_desc = ""
                for x in self.client.cogs:
                    cogs_desc += f"** {x} ** - {self.client.cogs[x].__doc__}\n"
                halp.add_field(
                    name="Categories", value=cogs_desc[0:len(cogs_desc) - 1],
                    inline=True
                )
                cmds_desc = ""
                for y in self.client.walk_commands():
                    if not y.cog_name and not y.hidden:
                        cmds_desc += ("{} - {}".format(y.name, y.help) + "\n")
                await ctx.message.add_reaction(emoji="❔")
                await ctx.send("", embed=halp)
            else:
                """Helps me remind you if you pass too many args."""
                if len(cog) > 1:
                    halp = discord.Embed(
                        title="Error!",
                        description="That is way too many cogs!",
                        color=discord.Color.red()
                    )
                    await ctx.send("", embed=halp)
                else:
                    """Command listing within a cog."""
                    found = False
                    for x in self.client.cogs:
                        for y in cog:
                            if x == y:
                                halp = discord.Embed(
                                    title=cog[0] + " Command Listing",
                                    description=self.client.cogs[
                                        cog[0]
                                    ].__doc__)
                                for c in self.client.get_cog(y).get_commands():
                                    if not c.hidden:
                                        halp.add_field(
                                            name=f"{c.name}-{c.aliases}",
                                            value=c.help,
                                            inline=False
                                        )
                                found = True
                    if not found:
                        """Reminds you if that cog doesn"t exist."""
                        halp = discord.Embed(
                            title="Error!",
                            description="How do you even use " +
                            cog[0] + "?",
                            color=discord.Color.red())
                    else:
                        await ctx.message.add_reaction(emoji="❔")
                    await ctx.send("", embed=halp)
        except Exception as err:
            await ctx.send(f"Excuse me, I can't send embeds. {err}")


def setup(client):
    client.add_cog(Help(client))
