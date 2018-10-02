# import the discord.py and datetime module
from discord.ext import commands
import discord
import datetime


# creating the class BaseCommands that will be a cog of the bot
class BaseCommands:
    def __init__(self, bot):
        # enabling us to use the class bot inside this cog
        self.bot = bot

    # creating the command 'ping'
    @commands.command(name="ping")
    async def ping(self, ctx):
        """View the bots ping"""
        # getting the time that the message that called this command was created at
        message_time = ctx.message.created_at
        # getting the current time and then calculating the difference
        localtime = datetime.datetime.utcnow()
        lag_time = (localtime - message_time) / 2
        # sending a plain message back showing the latency of the command and the websocket
        return await ctx.send(f"Command Latency: **{lag_time.microseconds/1000}ms**."
                              f"\nWebsocket Latency: **{(ctx.bot.latency*1000):.2f}ms**.")

    # creating the command 'ban' and listing that you have to use it in the format of:
    # ban <member> [and optionally reason]
    @commands.command(name="ban", usage="<member> [reason]")
    # checks if the user that calls this command is allowed to ban people in the server
    @commands.has_permissions(ban_members=True)
    # aside from self and the ctx object, this command also takes
    # the member argument that gets automatically converted to a discord.User
    # and converts the rest of the message that called it into the reason for the ban
    async def ban(self, ctx, member: discord.User, *, reason):
        try:
            # from the guild that the command got called in, we ban the member,
            # but delete none of his past messages
            await ctx.guild.ban(member, reason=reason, delete_message_days=0)
        # oh no, we do not have permission to ban someone
        except discord.Forbidden:
            # creating a fancy red embed that has as its description that we failed to ban the member
            em = discord.Embed(
                description=f"I do not have permission to ban {member}",
                colour=discord.Colour.red()
            )
            # sending the embed
            return await ctx.send(embed=em)

        # creating a fancy green embed saying that we succeeded in banning the member and lets add an image to it
        em = discord.Embed(
            description=f"Succesfully banned {member}",
            colour=discord.Colour.green()
        )
        em.set_image(url="https://imgur.com/a/BRCvPNr")
        # then lets send it
        return await ctx.send(embed=em)


# defining the setup command and then adding this cog (BaseCommands) to the bot itself
def setup(bot):
    bot.add_cog(BaseCommands(bot))
