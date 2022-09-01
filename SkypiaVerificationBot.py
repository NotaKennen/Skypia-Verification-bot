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

with open(os.path.expanduser('~/Downloads/Code Projects/Skypia Verification bot/data.json')) as f:
    data = json.load(f)
    token = data["TOKEN"]
    redpassword = data["redpassword"]
    redsecret = data["redsecret"]
    redclientid = data["redclientid"]

data = None

with open(os.path.expanduser('~/Downloads/Code Projects/Skypia Verification bot/config.json')) as f:
    data = json.load(f)
    logmode = data["logmodeconfig"]

print("Skypia Verification Bot")
print("Coded by Memarios")
print("----------------------------------------------")

bot = commands.Bot(command_prefix='+')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------------------------------------------')

@bot.command()
@commands.has_role('Server Admin')
async def config(ctx, config: str=None, state: str=None):
    if config is None:
        await ctx.send("Available config options: logmode")
    elif config == "logmode":
        if state == "True":
            await ctx.send("Logmode set to True")
            dictionary = {
            "logmodeconfig": "True"
            }
            json_object = json.dumps(dictionary, indent=1)
            with open(os.path.expanduser('~/Downloads/Code Projects/Skypia Verification bot/config.json'), "w") as outfile:
                outfile.write(json_object)

        elif state == "False":
            await ctx.send("Logmode set to False")
            dictionary = {
            "logmodeconfig": "False"
            }
            json_object = json.dumps(dictionary, indent=1)
            with open(os.path.expanduser('~/Downloads/Code Projects/Skypia Verification bot/config.json'), "w") as outfile:
                outfile.write(json_object)

        else:
            await ctx.send("Setting Logmode has to be set to True or False")
    else:
        await ctx.send("Invalid config option")

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
    with open(os.path.expanduser('~/Downloads/Code Projects/Skypia Verification bot/config.json')) as f:
        data = json.load(f)
        logmode = data["logmodeconfig"]
    if logmode == "True":
        channel = bot.get_channel(878180311148662814)
        await channel.send(f"{ctx.author} verified {member}")


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

# Moderation
#-------------------------------------------
# Fun/minigames

@bot.command()
async def register(ctx):
    person = {
    "Money": "0",
    "Card1": "0",
    "Card2": "0",
    "Card3": "0"
    }
    json_object = json.dumps(person, indent=1)
    with open(os.path.expanduser(f'~/Downloads/Code Projects/Skypia Verification bot/Card game/People/{ctx.author}.json'), "w") as outfile:
        outfile.write(json_object)
    await ctx.send("You have been registered!")

@bot.command()
async def inv(ctx, member: discord.member = None):
    if member is None:
        member = ctx.author
    with open(os.path.expanduser(f'~/Downloads/Code Projects/Skypia Verification bot/Card game/People/{ctx.author}.json')) as f:
        data = json.load(f)
        Card1 = data["Card1"]
        Card2 = data["Card2"]
        Card3 = data["Card3"]
    embed=discord.Embed(title=" ", color=0xee4f4f)
    embed.set_author(name=f"{ctx.author}'s inventory")
    embed.add_field(name="Card1", value=Card1, inline=False)
    embed.add_field(name="Card2", value=Card2, inline=True)
    embed.add_field(name="Card3", value=Card3, inline=False)
    await ctx.send(embed=embed)
    
@bot.command()
async def buy(ctx, cardname: str = None):
    if cardname is None:
        await ctx.send("Available cards: Card1")
    if cardname == "card1":
        await ctx.send("Command not yet done -Memarios")
    else: 
        await ctx.send("Not a card! Usage: +buy (card name)")

@bot.command()
async def bal(ctx, member: discord.member = None):
    member = ctx.author
    with open(os.path.expanduser(f'~/Downloads/Code Projects/Skypia Verification bot/Card game/People/{ctx.author}.json')) as f:
        data = json.load(f)
        Cardmoney = data["Money"]
    await ctx.send(f"You have {Cardmoney}$")

bot.run(token)

# Bot made by Kju#6300 (aka Memarios)
