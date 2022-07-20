#    Skypia verification bot, made for Skypia to automatically verify people
#    Copyright (C) 2022  Kju#6300
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

from statistics import mode
import discord
from discord.ext import commands
from discord.utils import get
import praw
from datetime import datetime
from secrets import secrets

forceconfig = True

if forceconfig == True:
    logmode = 0
    botmode = 0

print("Skypia Verification Bot")
print("Coded by Memarios")
print("----------------------------------------------")
if forceconfig == False:
    print("Botmode: (not coded yet, doesnt matter)")
    botmode = input("0 = Semiauto, 1 = automatic - ")
    print("Make logs: (not coded yet, doesnt matter)")
    logmode = input("0 = Don't make logs, 1 = Make logs - ")
    print("----------------------------------------------")

bot = commands.Bot(command_prefix='+')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------------------------------------------')


@bot.command(pass_context=True)
async def reddit(ctx, redname: str):
    client_id = "leQG__oE7-L2YtNIiZB6Cg"
    client_secret = "jQNqmALaS2DFvo9fWTbOpNrhdVUJOQ"
    username = "SkypiaBot"
    password = "SkypiaMemmy"
    user_agent = "SkypiaBot"
  
    # creating an authorized reddit instance
    reddit = praw.Reddit(client_id = client_id, 
                     client_secret = client_secret, 
                     username = username, 
                     password = password,
                     user_agent = user_agent) 
  
    # the name of the redditor
    redditor_name = redname
  
    # instantiating the Redditor class
    redditor = reddit.redditor(redditor_name)

    # fetching the Unix time of creation
    unix_time = redditor.created_utc

    reddittotalkarma = redditor.comment_karma + redditor.link_karma

    embed=discord.Embed(title="----------------------------------", color=0xffcd42)
    embed.set_author(name="Reddit checker")
    embed.add_field(name="Comment karma", value=redditor.comment_karma, inline=True)
    embed.add_field(name="Link karma", value=redditor.link_karma, inline=True)
    embed.add_field(name="Total karma", value=reddittotalkarma, inline=True)
    embed.add_field(name="Account creation", value=str(datetime.fromtimestamp(unix_time)), inline=True)
    embed.add_field(name="Verified email", value=redditor.has_verified_email, inline=True)
    embed.add_field(name="Account name", value=redname, inline=True)
    await ctx.send(embed=embed) 

@bot.command(pass_context=True)
@commands.has_role('Server Admin')
async def echo(ctx, *, echos: str):
    await ctx.send(echos)
    await ctx.message.delete()

@bot.command(pass_context=True)
@commands.has_role("OG'S")
async def ogecho(ctx, *, echos: str):
    await ctx.send(echos)
    await ctx.message.delete()

@bot.command(pass_context=True)
@commands.has_role('Non Realm Member')
async def verify(ctx, nickname: str, age: int, pingable: str):
    await ctx.send("Verifying")
    await ctx.author.edit(nick=nickname)
    role18 = ctx.guild.get_role(877361391491743815)
    role1317 = ctx.guild.get_role(877361323053285436)
    if age >= 18:
        await ctx.author.add_roles(role18)
    else:
        await ctx.author.add_roles(role1317)
    rolePingable = ctx.guild.get_role(878112584761495562)
    wantspings = "Yes"
    if pingable == "n":
        await ctx.author.remove_roles(rolePingable)
        wantspings = "No"
    if pingable == "N":
        await ctx.author.remove_roles(rolePingable)
        wantspings = "No"
    
    # send embed
    embed=discord.Embed(title="Verification Process", description="Verification info:", color=0x73ff4d)
    embed.add_field(name="Gamertag", value=nickname, inline=True)
    embed.add_field(name="Age", value=age, inline=True)
    embed.add_field(name="Pingable", value=wantspings, inline=True)
    embed.set_footer(text="Verification bot made by Memarios")
    await ctx.send(embed=embed)

    if logmode == 1:
        channel = ctx.client.get_channel(990888240422723634)
        await channel.send('New verification Log')
        await channel.send(embed=embed)

    if botmode == 1:
        #give roles
        roleRealmMember = ctx.guild.get_role(862852289462534156)
        roleVerified = ctx.guild.get_role(885061510592860160)
        roleUnverified = ctx.guild.get_role(876510056051511346)
        await ctx.author.remove_roles(roleUnverified)
        await ctx.author.add_roles(roleRealmMember)
        await ctx.author.add_roles(roleVerified)

    print(ctx.author, "has been verified")

@bot.command(pass_context=True)
async def github(ctx):
    await ctx.send("https://github.com/NotaKennen/Skypia-Verification-bot")



bot.run(secrets.get('dtoken'))

# Bot made by Kju#6300 (aka Memarios)
