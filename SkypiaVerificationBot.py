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
import json
import os

with open(os.path.expanduser('~/Downloads/Code Projects/Skypia Verification bot/config.json')) as f:
    data = json.load(f)
    token = data["TOKEN"]
    redpassword = data["redpassword"]
    redsecret = data["redsecret"]
    redclientid = data["redclientid"]

forceconfig = True

if forceconfig == True:
    logmode = 1
    botmode = 0

print("Skypia Verification Bot")
print("Coded by Memarios")
print("----------------------------------------------")
if forceconfig == False:
    print("Log all verifications?")
    logmode = input("0 = Don't make logs, 1 = Make logs - ")
    print("----------------------------------------------")

bot = commands.Bot(command_prefix='+')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------------------------------------------')

@bot.command()
async def store(ctx, *, variable):
    dictionary = {
    "name": variable,
    }
    json_object = json.dumps(dictionary, indent=4)
    with open(os.path.expanduser('~/Downloads/Code Projects/Skypia Verification bot/data.json'), "w") as outfile:
        outfile.write(json_object)

@bot.command()
async def config(ctx, config: str=None, state: str=None):
    confstatehere = "Deez"
    if config is None:
        await ctx.send("Available config options: logmode")
    elif config == "logmode":
        if state == "True":
            await ctx.send("Logmode set to true")
        elif state == "False":
            await ctx.send("Logmode set to false")
        else:
            await ctx.send("Setting Logmode has to be set to True or False")

@bot.command(pass_context=True)
@commands.has_role('Server Admin')
async def reddit(ctx, redname: str):
    client_id = redclientid
    client_secret = redsecret
    username = "SkypiaBot"
    password = redpassword
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
    embed.set_author(name=redname)
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
async def github(ctx):
    await ctx.send("https://github.com/NotaKennen/Skypia-Verification-bot")

@bot.command()
@commands.has_role('Server Admin')
async def verify(ctx, member : discord.Member, age: str=None, pingable: str=None):
    roleRealmMember = ctx.guild.get_role(862852289462534156)
    roleVerified = ctx.guild.get_role(885061510592860160)
    roleUnverified = ctx.guild.get_role(876510056051511346)
    await member.remove_roles(roleUnverified)
    await member.add_roles(roleRealmMember)
    await member.add_roles(roleVerified)
    await ctx.send("Verified!")
    if age is None:
        await ctx.send("You forgot to put the age, put it manually, I'm too lazy")
    if pingable is None:
        await ctx.send("You forgot to put the pingable, put it manually, I'm too lazy")

@bot.command()
@commands.has_role('Server Admin')
async def nick(ctx,  member : discord.Member, *, nickname: str):
    await member.edit(nick=nickname)

@bot.command()
@commands.has_role('Server Admin')
async def age(ctx, member : discord.Member, age: int):
    role18 = ctx.guild.get_role(877361391491743815)
    role1317 = ctx.guild.get_role(877361323053285436)
    if age >= 18:
        await member.add_roles(role18)
    else:
        await member.add_roles(role1317)



bot.run(token)

# Bot made by Kju#6300 (aka Memarios)
