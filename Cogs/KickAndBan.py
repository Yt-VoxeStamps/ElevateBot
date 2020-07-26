import discord

from discord.ext import commands, tasks

class KickAndBan(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason=None):
       await member.kick(reason=reason)
       await ctx.send(f'User {member} has been kicked.')

def setup(client):
    client.add_cog(KickAndBan(client))