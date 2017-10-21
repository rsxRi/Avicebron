#!/usr/bin/env/python3

import discord

from discord.ext import commands


class Moderation:

    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, member, *, reason=""):
        """Kick the specified member"""
        try:
            member = ctx.message.mentions[0]
            if ctx.message.author.top_role < member.top_role:
                await ctx.send("You cannot kick {}".format(member))
                return
            try:
                await member.send("You have been kicked from SSSv4stro! Reason: {}".format(reason if reason else "No reason provided"))
            except discord.errors.Forbidden:
                print("DMing user failed")
            await member.kick(reason=reason)
            await ctx.send("{} has been kicked".format(member))
        except IndexError:
            await ctx.send("Please mention a member")
        except discord.errors.Forbidden:
            await ctx.send("That member cannot be kicked")

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member, *, reason=""):
        """Ban the specified member"""
        try:
            member = ctx.message.mentions[0]
            if ctx.message.author.top_role < member.top_role:
                await ctx.send("You cannot ban {}".format(member))
                return
            try:
                await member.send("You have been banned from SSSv4stro! Reason: {}".format(reason if reason else "No reason provided"))
            except discord.errors.Forbidden:
                print("DMing user failed.")
            await member.ban(reason=reason, delete_message_days=0)
            await ctx.send("{} has been banned".format(member))
        except IndexError:
            await ctx.send("Please mention a member")
        except discord.errors.Forbidden:
            await ctx.send("That member cannot be banned")

def setup(bot):
    bot.add_cog(Moderation(bot))
