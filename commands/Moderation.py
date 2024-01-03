# Importing Libraries
import discord
from discord.ext import commands

# Adding Moderation to Main


class Moderation(
    commands.Cog
):
    """
    Standard moderation commands
    """

    def __init__(
        self, client
    ):
        self.client = client

        # Mute Command
    @commands.command(
        # Aliases
        aliases=[
            "Mute",
            "usermute",
            "shush"
        ],
        # Help
        help="Mute any user"
    )
    @commands.has_permissions(
        # Permission Check
        manage_roles=True
    )
    # Defining Mute
    async def mute(
        self, ctx, member, *reasons
    ):
        # Reasons
        reason = " ".join(
            reasons
        )
        for user in ctx.message.mentions:
            member = user

        if not ctx.message.mentions:
            return await ctx.channel.send(
                "❓❓ Please Choose a User to mute"
            )
        # Removing And Adding Roles
        for role in ctx.guild.roles:
            if role.name == "muted":
                muteRole = role

            if role.name == "Muted":
                muteRole = role

            if role.name == "Members":
                rRole = role

        try:
            await member.send(
                f"You've been Muted in {ctx.guild} for: {reason}"
            )
            await member.add_roles(
                muteRole
            )
            await member.remove_roles(
                rRole
            )
            await ctx.channel.send(
                f"**`✅ {member}` was successfully Muted .** {reason}"
            )
        except Exception as error:
            await ctx.channel.send(
                f"❌ `{member}` Could not be muted: {error} "
            )

    # Unmute Command
    @commands.command(
        # Aliases
        aliases=[
            "Unmute",
            "user_unmute",
            "unshush"
        ],
        # Help
        help="Unmute any user"
    )
    @commands.has_permissions(
        # Role Check
        manage_roles=True
    )
    # Defining Unmute
    async def unmute(
        self, ctx, memmber
    ):

        for user in ctx.message.mentions:
            member = user

        if not ctx.message.mentions:
            return await ctx.channel.send(
                "❓❓ Please Choose a User to unmute"
            )
        # Defining Roles
        for role in ctx.guild.roles:
            if role.name == "muted":
                muteRole = role

            if role.name == "Muted":
                muteRole = role

            if role.name == "Members":
                rRole = role
        try:
            # Adding and Removing Roles
            await member.remove_roles(
                muteRole
            )
            await member.add_roles(
                rRole
            )
            await ctx.channel.send(
                f"✅ **`{member}` was successfully Unmuted**"
            )
            # Error
        except Exception as error:
            await ctx.channel.send(
                f"❌ `{member}` Could not be unmuted: {error} "
            )
    # Command Error Permission

    @mute.error
    async def mute_handler(
        self, ctx, error
    ):
        if isinstance(
            error, commands.MissingPermissions
        ):
            await ctx.channel.send(
                "❌ **You dont have permissions to use this command!**"
            )
    # Command Error Permission

    @unmute.error
    async def unmute_handler(
        self, ctx, error
    ):

        if isinstance(
            error, commands.MissingPermissions
        ):
            await ctx.channel.send(
                "❌ **You dont have permissions to use this command!**"
            )

    # Clean Command
    @commands.command(
        # Aliases
        aliases=[
            "clean",
            "purge"
        ],
        # Help
        help="Deletes specified number of messages"
    )
    @commands.has_permissions(
        # Permission Check
        manage_messages=True
    )
    # Defining Command
    async def clear(
        self, ctx, ammount=5
    ):
        # 0 Message Error
        if ammount == 0:
            return await ctx.channel.send(
                "❌ You cant clear 0 messages"
            )
        # Clear Messages
        try:
            await ctx.channel.purge(
                limit=ammount
            )
            await ctx.channel.send(
                f"✅ Succesfully Cleared `{ammount}` messages"
            )
        # Error
        except Exception as err:
            await ctx.channel.send(
                err
            )

    # Clean Permission Error
    @clear.error
    async def clear_handler(
        self, ctx, error
    ):

        if isinstance(
            error, commands.MissingPermissions
        ):
            await ctx.channel.send(
                "❌ **You dont have permissions to use this command!**"
            )

    # Addrole Command
    @commands.command(
        # Aliases
        aliases=[
            "arole",
            "giverole"
        ],
        # Help
        help="Adds any role to a user"
    )
    @commands.has_permissions(
        # Permission Check
        manage_roles=True
    )
    async def addrole(
        self, ctx, member, *, rolename
    ):

        for user in ctx.message.mentions:
            mem = user

        for role in ctx.guild.roles:

            if role.name == rolename:
                try:
                    await mem.add_roles(
                        role
                    )
                    await ctx.channel.send(
                        f"`✅{role.name}` Was successfully given to `{user.name}`"
                    )
                except Exception as err:
                    await ctx.channel.send(
                        err
                    )

    @commands.command(
        aliases=[
            "remrole",
            "rrole",
            "takerole"
        ],
        help="Removes any role from a user"
    )
    @commands.has_permissions(
        manage_roles=True
    )
    async def removerole(
        self, ctx, member, *, rolename
    ):

        for user in ctx.message.mentions:
            mem = user

        for role in ctx.guild.roles:

            if role.name == rolename:
                try:
                    await mem.remove_roles(
                        role
                    )
                    await ctx.channel.send(
                        f"`✅ {role.name}` Was successfully removed from `{user.name}`"
                    )
                except Exception as err:
                    await ctx.channel.send(err)

    @addrole.error
    async def arole_handler(
        self, ctx, error
    ):

        if isinstance(
            error, commands.MissingPermissions
        ):
            await ctx.channel.send(
                "❌ **You dont have permissions to use this command!**"
            )

    @removerole.error
    async def rrole_handler(
        self, ctx, error
    ):

        if isinstance(
            error, commands.MissingPermissions
        ):
            await ctx.channel.send(
                "❌ **You dont have permissions to use this command!**"
            )

    @commands.command(
        aliases=[
            "kicker",
            "getout"
        ],
        help="Kicks any user from the server"
    )
    @commands.has_permissions(
        kick_members=True
    )
    async def kick(
        self, ctx, member, *, reason
    ):

        for user in ctx.message.mentions:
            member = user

        try:
            await member.send(
                f"You've been kicked in {ctx.guild} for: {reason}"
            )
            await member.kick(
                reason=reason
            )
            await ctx.channel.send(
                f"**`✅ {member}` was successfully kicked >>** {reason}"
            )
        except Exception as err:
            await ctx.channel.send(
                f"❌ {member} could not be kicked: {err}"
            )

    @commands.command(
        aliases=[
            "userban",
            "dontcomeback"
        ],
        help="Strike the BAN HAMMER"
    )
    @commands.has_permissions(
        ban_members=True
    )
    async def ban(
        self, ctx, member, *reasons
    ):

        reason = " ".join(
            reasons
        )

        for user in ctx.message.mentions:
            member = user

        try:
            try:
                await member.send(
                    f"You've been banned in {ctx.guild} for: {reason}"
                )
            except:
                pass

            await member.ban(
                reason=reason
            )
            await ctx.channel.send(
                f"**`✅ {member}` was successfully banned >>** {reason}"
            )
        except Exception as err:
            await ctx.channel.send(
                f"❌ {member} could not be banned: {err}"
            )

    @commands.command(
        aliases=[
            "user-unban",
            "docomeback"
        ],
        help="Unbans any banned user "
    )
    @commands.has_permissions(
        ban_members=True
    )
    async def unban(
        self, ctx, *, member
    ):
        try:
            for user in ctx.message.mentions:
                member = user
            await member.unban(

            )
            await ctx.channel.send(
                f"**`✅{member} was successfully unbanned**"
            )
        except Exception as err:
            await ctx.channel.send(
                f"❌ {member} could not be unbanned: {err}"
            )

    @ban.error
    async def ban_handler(
        self, ctx, error
    ):

        if isinstance(
            error, commands.MissingPermissions
        ):
            await ctx.channel.send(
                "❌ **You dont have permissions to use this command!**"
            )

    @unban.error
    async def unban_handler(
        self, ctx, error
    ):

        if isinstance(
            error, commands.MissingPermissions
        ):
            await ctx.channel.send(
                "❌ **You dont have permissions to use this command!**"
            )

    @commands.command(
        aliases=[
            "announce",
            "Announcer"
        ],
        help="Announce a Message at <#886673966700322866>"
    )
    @commands.has_permissions(
        manage_messages=True,
        manage_roles=True
    )
    async def Announcement(
        self, ctx, *, arg
    ):
        try:
            guild = ctx.guild
            Upvote = discord.utils.get(guild.emojis, name="Upvote")
            Downvote = discord.utils.get(guild.emojis, name="Downvote")

            channel = self.client.get_channel(
                886673966700322866
            )
            embed = discord.Embed(

            )
            embed.description = f"{arg}"
            embed.colour = 0x800000

            embed.set_author(
                name=f"Announcement from {self.client.user}",
                icon_url=self.client.user.avatar_url
            )

            message = await channel.send(
                "@everyone @here",
                embed=embed
            )

            await ctx.send(
                "✅**The Announcement Has been Succesfully Announced**"
            )

            await message.add_reaction(Upvote)
            await message.add_reaction(Downvote)

        except Exception as err:
            await ctx.send(
                f"Excuse me, There is an Error =  {err}"
            )

    @Announcement.error
    async def Announcement_handler(
        self, ctx, error
    ):
        if isinstance(
            error, commands.MissingPermissions
        ):
            await ctx.channel.send(
                "❌ **You dont have permissions to use this command!**"
            )

    @commands.command(
        aliases=[
            "megaclean",
            "megapurge"
        ],
        help="Deletes specified number of messages"
    )
    @commands.has_permissions(
        manage_messages=True
    )
    async def clearall(
        self, ctx,
    ):
        try:
            await ctx.channel.purge(
                limit=1000000
            )
            await ctx.channel.send(
                "✅ Succesfully Cleared all messages"
            )
        except Exception as err:
            await ctx.channel.send(
                err
            )

    @clearall.error
    async def clearall_handler(
        self, ctx, error
    ):
        if isinstance(
            error, commands.MissingPermissions
        ):
            await ctx.channel.send(
                "❌ **You dont have permissions to use this command!**"
            )

    @commands.command(
        aliases=[
            "logout",
            "Shutoff"
        ],
        help="Shutdowns This Bot"
    )
    @commands.has_permissions(
        manage_messages=True,
        administrator=True
    )
    @commands.has_any_role(
        "Owner"
    )
    async def shutdown(
        self, ctx
    ):
        try:
            await ctx.send(
                "Logging out now\N{HORIZONTAL ELLIPSIS}"
            )
            await self.client.logout(

            )
        except Exception as err:
            await ctx.channel.send(
                err
            )

    @shutdown.error
    async def shutdown_handler(
        self, ctx, error
    ):
        if isinstance(
            error, commands.MissingPermissions
        ):
            await ctx.channel.send(
                "❌ **You dont have permissions to use this command!**"
            )


def setup(
    client
):
    client.add_cog(
        Moderation(
            client
        )
    )
