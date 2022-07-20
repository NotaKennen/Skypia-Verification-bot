from statistics import mode
import discord
from discord.ext import commands
from discord.utils import get
import praw
from datetime import datetime

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
async def command(ctx, exhelp: str):
    if exhelp == "echo":
        await ctx.send("Command Echo: A command for admins to say things thru the bot")
        await ctx.send("usage: +echo (message)")
    elif exhelp == "ogecho":
        await ctx.send("Command Ogcho: A command for OGs to say things thru the bot")
        await ctx.send("usage: +ogecho (message)")
    elif exhelp == "reddit":
        await ctx.send("Command Reddit: A command that shows basic stats from a Reddit account")
        await ctx.send("usage: +reddit (account name)")
    elif exhelp == "verify":
        await ctx.send("Command Verify: A command that automatically verifies a user")
        await ctx.send("usage: +verify (gamertag) (age) (pingable (Y/N))")
    else:
        await ctx.send("List of commands: echo, ogecho, reddit, verify")
        await ctx.send("Type '+command (command)' for more info on a certain command")

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

    await ctx.send("The comment karma of " + redditor_name + " is : " +
      str(redditor.comment_karma))

    await ctx.send("The link karma of " + redditor_name + " is : " +
      str(redditor.link_karma))

    await ctx.send("The total karma of " + redditor_name + " is : " +
      str(reddittotalkarma))

    await ctx.send("The " + redditor_name + " account was created on : " +
      str(datetime.fromtimestamp(unix_time)))

    await ctx.send("Has " + redditor_name + " verified their email? : " +
      str(redditor.has_verified_email))    

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



bot.run('token')

# Bot made by Kju#6300 (aka Memarios)



#MIT License

#Copyright (c) 2022 Kju#6300

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
