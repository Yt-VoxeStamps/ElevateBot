import discord
import json
import os
from discord.ext import commands, tasks
import asyncio
from itertools import cycle
from discord.utils import get

client = commands.Bot(command_prefix= '!')
Clientdiscord = discord.Client()
status = cycle([' Bot made by Stamps', 'Bot made by Stamps'])

TOKEN = 'NzA1NDg2OTM5NjI0NTcwOTcz.XqsZ6Q.7U56wbwH9wqiZHrZt4dlkthDzEw'




@client.event
async def on_ready():
    print('Uprise Bot Is Online')


@client.command()
async def ping(ctx):
    await ctx.send('Pong')





    #Mute
@client.command()
@commands.has_permissions(mute_members=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    await member.mute(reason=reason)
    await ctx.send(f'User {member} has been muted.')



    #Ban
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)



    #ClearMessages
@client.command()
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)
    await ctx.send("All Messages have been cleared")
    await ctx.channel.purge(limit=amount)




    #AvatarPic
@client.command()
async def Profile(ctx, *, member: discord.Member=None): # set the member object to None
    if not member: # if member is no mentioned
        member = ctx.message.author # set member as the author
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)




    #UserInfo
@client.command()
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]

    embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Guild name:", value=member.display_name)

    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Created at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Top role:", value=member.top_role.mention)

    embed.add_field(name="Bot?", value=member.bot)

    await ctx.send(embed=embed)





    #Change Status
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('bot made by stamps'))

@client.event
async def on_ready():
    change_status.start()

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))





@client.command()
async def Hello(ctx):
     await ctx.send(f"{ctx.message.author.mention} Hello")







    #LoadOtherFiles

@client.command()
async def load(ctx, extension):
    client.load_extension(f'Cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extensionn(f'Cogs.{extension}')

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'Cogs.{filename[:-3]}')



client.run('NzA1NDg2OTM5NjI0NTcwOTcz.XqsZ6Q.7U56wbwH9wqiZHrZt4dlkthDzEw')
