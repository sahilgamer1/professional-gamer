main.py

import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools


Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = commands.Bot(description="MultiVerse Official Bot", command_prefix=commands.when_mentioned_or("pg!"), pm_help = True)
client.remove_command('help')

async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='for pg!help'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='with '+str(len(set(client.get_all_members())))+' users'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='in '+str(len(client.servers))+' servers'))
        await asyncio.sleep(5)

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started Our BOT')
    print('Created by Utkarsh')
    client.loop.create_task(status_task())


def is_dark(ctx):
    return ctx.message.author.id == "420525168381657090"

def is_shreyas(ctx):
    return ctx.message.author.id == "376602841625919488"

@client.event
async def on_message(message):
    channel = client.get_channel('518710986799316992')
    if message.server is None and message.author != client.user:
        await client.send_message(channel, '{} : <@{}> : '.format(message.author.name, message.author.id) + message.content)
    await client.process_commands(message)

@client.event
async def on_reaction_add(reaction, user):
  if reaction.message.server is None:
      if reaction.emoji == '🇬':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name = 'pg!donate',value ='Sends donation link',inline = False)
        embed.add_field(name = 'pg!invite or pg!authlink',value ='Use it to invite our bot to your server',inline = False)
        embed.add_field(name = 'pg!upvote',value ='Use this command to upvote our bot(Link will be in dm)',inline = False)
        embed.add_field(name = 'pg!rolldice',value ='Use it like ``pg!rolldice <1-6 any number that you want to guess in dice>``',inline = False)
        embed.add_field(name = 'pg!avatar',value ='Use it like ``pg!avatar or mv!avatar @user``',inline = False)
        embed.add_field(name = 'pg!flipcoin',value ='Use it like ``pg!rolldice <Your prediction>`` prediction = heads, tails or coin self destructed)``',inline = False)
        embed.add_field(name = 'pg!enterme',value ='Use it like ``pg!enterme <giveaway channel>`` to enter in a giveaway running in a particular channel',inline = False)
        embed.add_field(name = 'pg!poll ',value ='Use it like ``pg!poll "Question" "Option1" "Option2" ..... "Option9"``.',inline = False)
        embed.add_field(name = 'mv!guess ',value ='To play guess game use ``pg!guess <number> and number should be between 1-10``',inline = False)
        embed.add_field(name = 'pg!github ',value ='Use it like- ``pg!github uksoftworld/DarkBot``',inline = False)
        embed.add_field(name = 'pg!bottutorial ',value ='Use it like ``pg!bottutorial <tutorial name by darklegend>``',inline = False)
        embed.add_field(name = 'pg!dyno ',value ='Use it like ``mv!dyno <dyno command name>``',inline = False)
        embed.add_field(name = 'pg!happybirthday @user ',value ='To wish someone happy birthday',inline = False)
        embed.add_field(name = 'pg!verify ',value ='Use it to get verified role. Note- It needs proper setup.',inline = False)
        await client.send_message(user,embed=embed)
      if reaction.emoji == '🇲':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Moderation Commands Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'pg!dm(Admin permission required) ',value ='Use it like ``pg!dm @user <text>`` to dm user from bot',inline = False)
        embed.add_field(name = 'pg!say(Admin permission required) ',value ='Use it like ``pg!say <text>``',inline = False)
        embed.add_field(name = 'pg!showme(Requires a role named Giveaways)',value ='To see how many people are taking part in giveaway',inline = False)
        embed.add_field(name = 'pg!pickwinner(Requires a role named Giveaways)',value ='To pick winner',inline = False)
        embed.add_field(name = 'pg!embed(Admin permission required) ',value ='Use it like ``pg!embed <text>``',inline = False)
        embed.add_field(name = 'pg!membercount(Kick members Permission Required) ',value ='Use it like ``mv!membercount`` to get membercount',inline = False)
        embed.add_field(name = 'pg!removemod(Admin Permission Required)',value ='Use it like ``pg!removemod @user`` to remove him from mod. Note-You need Moderator role in your server below bot to use it.',inline = False)
        embed.add_field(name = 'pg!makemod(Admin Permission Required)',value ='Use it like ``pg!makemod @user`` to make him mod. Note-You need Moderator role in your server below darkbot to use it.',inline = False)
        embed.add_field(name = 'pg!friend(Admin Permission Required) ',value ='Use it like ``pg!friend @user`` to give anyone Friend of Owner role',inline = False)
        embed.add_field(name = 'pg!role(Manage Roles Permission Required)',value ='Use it like ``pg!role @user <rolename>``.',inline = False)
        embed.add_field(name = 'pg!setnick(Manage nickname permission required)',value ='Use it like ``pg!setnick @user <New nickname>`` to change the nickname of tagged user.',inline = False)
        embed.add_field(name = 'pg!english(Kick members Permission Required)',value ='Use it like ``pg!english @user`` when someone speaks languages other than English.',inline = False)
        embed.add_field(name = 'pg!serverinfo(Kick members Permission Required) ',value ='Use it like ``pg!serverinfo`` to get server info',inline = False)
        embed.add_field(name = 'pg!userinfo(Kick members Permission Required) ',value ='Use it like ``pg!userinfo @user`` to get some basic info of tagged user',inline = False)
        react_message = await client.send_message(user,embed=embed)
        reaction = '⏭'
        await client.add_reaction(react_message, reaction)
    
      if reaction.emoji == '⏭':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Moderation Commands Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'pg!unbanall(Unban members Permission Required)',value ='Use it like ``pg!unbanall`` to unban all members',inline = False)
        embed.add_field(name = 'pg!kick(Kick members Permission Required)',value ='Use it like ``pg!kick @user`` to kick any user',inline = False)
        embed.add_field(name = 'pg!roles(Kick members Permission Required) ',value ='Use it to check roles present in server',inline = False)
        embed.add_field(name = 'pg!clear(Manage Messages Permission Required)',value ='Use it like ``pg!purge <number>`` to clear any message',inline = False)
        embed.add_field(name = 'pg!mute(Mute members Permission Required)',value ='Use it like ``pg!mute @user <time>`` to mute any user',inline = False)
        embed.add_field(name = 'pg!unmute(Mute members Permission Required) ',value ='Use it like ``pg!unmute @user`` to unmute anyone',inline = False)
        embed.add_field(name = 'pg!ban(Ban members Permission Required) ',value ='Use it like ``pg!ban @user`` to ban any user',inline = False)
        embed.add_field(name = 'pg!rules(Kick members Permission Required)',value ='Use it like ``pg!rules @user <violation type>`` to warn user',inline = False)
        embed.add_field(name = 'pg!warn(Kick members Permission Required)',value ='Use it like ``pg!warn @user <violation type>`` to warn any user',inline = False)    
        embed.add_field(name = 'pg!norole(Kick members Permission Required) ',value ='Use it like ``pg!norole @user`` to warn anyone if he/she asks for promotion',inline = False)
        embed.add_field(name = 'pg!getuser(Kick members Permission Required) ',value ='Use it like ``pg!getuser @rolename`` to get list of all users having a particular role',inline = False)
        react_message = await client.send_message(user,embed=embed)
        reaction = '⏮'
        await client.add_reaction(react_message, reaction)
    
      if reaction.emoji == '⏮':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Moderation Commands Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'pg!setupwelcomer(Admin Permission required) ',value ='Simply use it to make a channel named ★彡-welcome-彡★ so that bot will send welcome and leaves logs in that channel.',inline = False)
        embed.add_field(name = 'pg!say(Admin permission required) ',value ='Use it like ``mv!say <text>``',inline = False)
        embed.add_field(name = 'pg!embed(Admin permission required) ',value ='Use it like ``pg!embed <text>``',inline = False)
        embed.add_field(name = 'pg!membercount(Kick members Permission Required) ',value ='Use it like ``pg!membercount`` to get membercount',inline = False)
        embed.add_field(name = 'pg!removemod(Admin Permission Required)',value ='Use it like ``pg!removemod @user`` to remove him from mod. Note-You need Moderator role in your server below bot to use it.',inline = False)
        embed.add_field(name = 'pg!makemod(Admin Permission Required)',value ='Use it like ``pg!makemod @user`` to make him mod. Note-You need Moderator role in your server below darkbot to use it.',inline = False)
        embed.add_field(name = 'pg!friend(Admin Permission Required) ',value ='Use it like ``pg!friend @user`` to give anyone Friend of Owner role',inline = False)
        embed.add_field(name = 'pg!role(Manage Roles Permission Required)',value ='Use it like ``pg!role @user <rolename>``.',inline = False)
        embed.add_field(name = 'pg!setnick(Manage nickname permission required)',value ='Use it like ``pg!setnick @user <New nickname>`` to change the nickname of tagged user.',inline = False)
        embed.add_field(name = 'pg!english(Kick members Permission Required)',value ='Use it like ``pg!english @user`` when someone speaks languages other than English.',inline = False)
        embed.add_field(name = 'pg!serverinfo(Kick members Permission Required) ',value ='Use it like ``pg!serverinfo`` to get server info',inline = False)
        embed.add_field(name = 'pg!userinfo(Kick members Permission Required) ',value ='Use it like ``pg!userinfo @user`` to get some basic info of tagged user',inline = False)
        react_message = await client.send_message(user,embed=embed)
        reaction = '⏭'
        await client.add_reaction(react_message, reaction)
      if reaction.emoji == '🏵':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Setup Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'Setting up Welcomer log(Admin Permission required) ',value ='Use pg!setupwelcomer. It will add a welcome channel. Just put that channel in your desired category and it will send all logs there.',inline = False)
        embed.add_field(name = 'Setting up Giveaway feature(Manage roles permission required) ',value ='Just add a role named ``Giveaways`` and give that role to user who wanna be giveaway manager. Then use ``pg!help`` and check giveaway commands.',inline = False)
        embed.add_field(name = 'Setting up Reaction Verification(Admin Permission required) ',value ='Just add a role named ``Verified`` then remove permission from everyone to send message in all channels. Also add permission of verified role to send message in chatting channels. Then use ``pg!setreactionverify`` it will automatically add a channel and post information about verification. **__Note__** **Sometimes it does not sends message in channel named #verify-for-chatting when this command is used so reuse that command in such case**',inline = False)
        embed.add_field(name = 'Setting up Multiverse bot log(Admin Permission required) ',value ='Use ``pg!setuplog`` and it will automatically add a log channel and log all stuffs there.',inline = False)
        await client.send_message(user,embed=embed)

      if reaction.emoji == '🎦':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Emoji Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'mv!wow',value ='WOW emoji <a:WOW:515854429485006848>',inline = False)
        embed.add_field(name = 'pg!cat',value ='Cat emoji <a:agooglecat:516174312294842389>',inline = False)
        embed.add_field(name = 'pv!surprised',value ='Surprised emoji <a:eyebigger:516174315058626560>',inline = False)
        embed.add_field(name = 'pg!angry',value ='Angry emoji <a:angear:516174316950388772>',inline = False)
        embed.add_field(name = 'pg!fearfromme',value ='Scary emoji <a:shiroeglassespush:516174320532193289>',inline = False)
        embed.add_field(name = 'pg!dank',value ='DankMemer emoji <a:OnThaCoco:515853700682743809>',inline = False)
        embed.add_field(name = 'pg!thinking1',value ='Think emoji1 <a:thinking:516183328613990400>',inline = False)
        embed.add_field(name = 'pg!thinking2',value ='Think emoji2 <a:thinking2:516183323127709699>',inline = False)
        embed.add_field(name = 'pg!happy',value ='Happy emoji <a:happy:516183323052212236>',inline = False)
        embed.add_field(name = 'pg!santa',value ='Santa emoji <a:santa:517232271678504970>',inline = False)
        embed.add_field(name = 'pg!lol',value ='LoL emoji <a:lol:517232283670020096>',inline = False)
        embed.add_field(name = 'pg!love',value ='Love emoji <a:love:517232300912672774>',inline = False)
        embed.add_field(name = 'pg!mad',value ='Mad emoji <a:mad:517232301176913951>',inline = False)
        embed.add_field(name = 'pg!alien',value ='Alien emoji <a:alien:517232332663422986>',inline = False)
        embed.add_field(name = 'pg!hi',value ='Saying Hi emoji <a:hi:517232279148429313>',inline = False)
        await client.send_message(user,embed=embed)

  else:
      for reaction.message.channel in reaction.message.server.channels:
        if reaction.message.channel.name == '★verify-for-chatting★' and reaction.emoji == '🇻':
            role = discord.utils.get(reaction.message.server.roles, name='Verified')
            await client.add_roles(member, role)
        
@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == '★彡-welcome-彡★':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check rules and never try to break any one of them', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__Thanks for joining__', value='**Hope you will be active here.**', inline=True)
            embed.set_thumbnail(url='https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif') 
            embed.set_image(url = member.avatar_url)
            embed.add_field(name='__Join position__', value='{}'.format(str(member.server.member_count)), inline=True)
            embed.add_field(name='Time of joining', value=member.joined_at)
            await client.send_message(channel, embed=embed) 

@client.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == '★彡-welcome-彡★':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'{member.name} just left {member.server.name}', description='Bye bye 👋! We will miss you 😢', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__User left__', value='**Hope you will be back soon 😕.**', inline=True)
            embed.add_field(name='Your join position was', value=member.joined_at)
            embed.set_thumbnail(url=member.avatar_url)
            await client.send_message(channel, embed=embed)

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
async def mute(ctx, member: discord.Member):
    if member.server_permissions.kick_members:
        await client.say('**He is mod/admin and i am unable to mute him/her**')
        return
    if ctx.message.author.bot:
      return
    else:
      role = discord.utils.get(member.server.roles, name='Muted')
      await client.add_roles(member, role)
      await client.say("Muted **{}**".format(member))
      for channel in member.server.channels:
        if channel.name == '╰☆☆-professional-log-☆☆╮':
            embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0x37F60A)
            await client.send_message(channel, embed=embed)

@client.command(pass_context = True)
async def avatar(ctx, user: discord.Member=None):
    if user is None:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar', description='Avatar is profile picture of a user in discord', color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name='User: {}'.format(ctx.message.author.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/icons/489333893988745217/eb022a7023d013bec656cd7b94d6d6c1.png') 
        embed.set_image(url = ctx.message.author.avatar_url)
        await client.say(embed=embed)
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar', description='Avatar is profile picture of a user in discord', color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name='User: {}'.format(user.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/icons/489333893988745217/eb022a7023d013bec656cd7b94d6d6c1.png') 
        embed.set_image(url = user.avatar_url)
        await client.say(embed=embed)
@client.command(pass_context=True)
@commands.check(is_dark)
async def botdm(ctx, user: discord.Member, *, msg: str):
    await client.send_message(user, msg)
    	
@client.command(pass_context = True)
async def rolldice(ctx):
    choices = ['1', '2', '3', '4', '5', '6']
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Rolled! (1 6-sided die)', description=random.choice(choices))
    await client.say(embed=em)

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def dm(ctx, user: discord.Member, *, msg: str):
    try:
        await client.send_message(user, msg)
        await client.delete_message(ctx.message)          
        await client.say("Success! Your DM has made it! :white_check_mark: ")
    except discord.ext.commands.MissingPermissions:
        await client.say("Aw, come on! You thought you could get away with DM'ing people without permissions.")
    except:
        await client.say("Error :x:. Make sure your message is shaped in this way: mv!dm [tag person] [msg]")

@client.command(pass_context = True)
async def flipcoin(ctx):
    choices = ['Heads', 'Tails', 'Coin self-destructed']
    color = discord.Color(value=0x00ff00)
    em=discord.Embed(color=color, title='Flipped a coin!')
    em.description = random.choice(choices)
    await client.say(embed=em)


@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
async def unmute(ctx, member: discord.Member):
    if ctx.message.author.bot:
      return
    else:
      role = discord.utils.get(member.server.roles, name='Muted')
      await client.remove_roles(member, role)
      await client.say("Unmuted **{}**".format(member))
      for channel in member.server.channels:
        if channel.name == '╰☆☆-professional-log-☆☆╮':
            embed=discord.Embed(title="User unmuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xFD1600)
            await client.send_message(channel, embed=embed)
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
@commands.cooldown(rate=5,per=86400,type=BucketType.user) 
async def access(ctx, member: discord.Member):
    if ctx.message.author.bot:
      return
    else:
      role = discord.utils.get(member.server.roles, name='Access')
      await client.add_roles(member, role)
      await client.say("Gave access to {}".format(member))
      for channel in member.server.channels:
        if channel.name == '╰☆☆-professional-log-☆☆╮':
            embed=discord.Embed(title="User Got Access!", description="**{0}** got access from **{1}**!".format(member, ctx.message.author), color=0x020202)
            await client.send_message(channel, embed=embed)
            await asyncio.sleep(45*60)
            await client.remove_roles(member, role)
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setupwelcomer(ctx):
    if ctx.message.author.bot:
      return
    else:
      author = ctx.message.author
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, '★彡-welcome-彡★',everyone)

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setuplog(ctx):
    if ctx.message.author.bot:
      return
    else:
      author = ctx.message.author
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, '╰☆☆-professional-log-☆☆╮',everyone)
@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)
async def getuser(ctx, role: discord.Role = None):
    if role is None:
        await client.say('There is no "STAFF" role on this server!')
        return
    empty = True
    for member in ctx.message.server.members:
        if role in member.roles:
            await client.say("{0.name}: {0.id}".format(member))
            empty = False
    if empty:
        await client.say("Nobody has the role {}".format(role.mention))

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)     
async def userinfo(ctx, user: discord.Member):
    if ctx.message.author.bot:
      return
    else:
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
      embed.add_field(name="Name", value=user.name, inline=True)
      embed.add_field(name="ID", value=user.id, inline=True)
      embed.add_field(name="Status", value=user.status, inline=True)
      embed.add_field(name="Highest role", value=user.top_role)
      embed.add_field(name="Joined", value=user.joined_at)
      embed.set_thumbnail(url=user.avatar_url)
      await client.say(embed=embed)

@client.command(pass_context = True)
@commands.check(is_dark)
async def iamdark(ctx):
    author = ctx.message.author
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='sahil solanki')
    await client.add_roles(ctx.message.author, role)
    print('Added sahil role in ' + (ctx.message.author.name))
    await client.send_message(author, embed=embed)

@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def unbanall(ctx):
    if ctx.message.author.bot:
      return
    else:
      server=ctx.message.server
      ban_list=await client.get_bans(server)
      await client.say('Unbanning {} members'.format(len(ban_list)))
      for channel in ctx.message.author.server.channels:
        if channel.name == '╰☆☆-professional-log-☆☆╮':
            embed=discord.Embed(title="All users are unbanned!", description="Members were unbanned by **{}**!".format(ctx.message.author), color=0x05F6E0)
            await client.send_message(channel, embed=embed)
      for member in ban_list:
          await client.unban(server,member)
@client.command(pass_context = True)
@commands.check(is_shreyas)
async def iamshreyas(ctx):
    author = ctx.message.author
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='ShreyasMF')
    await client.add_roles(ctx.message.author, role)
    print('Added SHREYAS role in ' + (ctx.message.author.name))
    await client.send_message(author, embed=embed)

@client.command(pass_context=True)
async def iamcoder(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="Successfully added", description="Programmer role", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Enjoy! ", value="Happy Coding :-). Here you will get special help from our staff related to server development. ", inline=True)
    
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Programmer')
    await client.add_roles(ctx.message.author, role)
    print('Added codies role in ' + (ctx.message.author.name))
    await client.send_message(author, embed=embed)
    
@client.command(pass_context=True)
async def iamnotcoder(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="Successfully removed", description="Programmer role", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Enjoy! ", value="Hope you will try our other features as well", inline=True)
    
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Programmer')
    await client.remove_roles(ctx.message.author, role)
    print('Removed codies role from ' + (ctx.message.author.name))
    await client.send_message(author, embed=embed)
 
@client.command(pass_context=True)
async def iamnotserverdeveloper(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="Successfully removed", description="Server developer role", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Enjoy! ", value="Hope you will try our other features as well", inline=True)
    
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Server Developer')
    await client.remove_roles(ctx.message.author, role)
    print('Removed server developer role from ' + (ctx.message.author.name))
    await client.send_message(author, embed=embed)
    

@client.command(pass_context=True)
async def iamserverdeveloper(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="Successfully added", description="Server Developer role", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Enjoy! ", value="Happy Server Development. Here you will get special support from our support team related to server development", inline=True)
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Server Developer')
    await client.add_roles(ctx.message.author, role)
    print('Added codies role in ' + (ctx.message.author.name))
    await client.send_message(author, embed=embed)
 

@client.command(pass_context = True)

@commands.has_permissions(manage_roles=True)     
async def role(ctx, user: discord.Member, *, role: discord.Role = None):
        if role is None:
            return await client.say("You haven't specified a role! ")

        if role not in user.roles:
            await client.add_roles(user, role)
            return await client.say("{} role has been added to {}.".format(role, user))

        if role in user.roles:
            await client.remove_roles(user, role)
            return await client.say("{} role has been removed from {}.".format(role, user))
 
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User, *, message:str): 
    if userName.server_permissions.kick_members:
        await client.say('**He is mod/admin and i am unable to warn him/her**')
        return
    else:
      await client.send_message(userName, "You have been warned for: **{}**".format(message))
      await client.say(":warning: __**{0} Has Been Warned!**__ :warning: ** Reason:{1}** ".format(userName,message))
      pass

@client.command(pass_context = True)
@commands.has_permissions(manage_nicknames=True)     
async def setnick(ctx, user: discord.Member, *, nickname):
    await client.change_nickname(user, nickname)
    await client.delete_message(ctx.message)
    for channel in user.server.channels:
      if channel.name == '╰☆☆-professional-log-☆☆╮':
          embed=discord.Embed(title="Changed Nickname of User!", description="**{0}** nickname was changed by **{1}**!".format(member, ctx.message.author), color=0x0521F6)
          await client.send_message(channel, embed=embed)
@client.command(pass_context=True)
async def poll(ctx, question, *options: str):
        if len(options) <= 1:
            await client.say('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await client.say('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['👍', '👎']
        else:
            reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=question, description=''.join(description), color = discord.Color((r << 16) + (g << 8) + b))
        react_message = await client.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await client.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await client.edit_message(react_message, embed=embed)
        
@client.command(pass_context = True)
async def help(ctx):
    if ctx.message.author.bot:
      return
    else:
      author = ctx.message.author
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
      embed.set_author(name='Help')
      embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
      embed.add_field(name = 'Having doubts? Join our server and clear your doubts. Server link:',value ='https://discord.gg/FrRtyS6',inline = False)
      embed.add_field(name = 'React with 🇲 ',value ='Explaines all the commands which are only usable by Those who has moderation permissions. Like- Manage Nicknames, Manage Messages, Kick/Ban Members,etc.',inline = False)
      embed.add_field(name = 'React with 🇬 ',value ='Explaines all the commands which are usable by everyone.',inline = False)
      embed.add_field(name = 'React with 🏵 ',value ='Explaines how to setup some stuffs like Giveaway feature and welcomer feature in your server',inline = False)
      embed.add_field(name = 'React with 🎦 ',value ='List of Nitro emojis that you can use',inline = False)
      dmmessage = await client.send_message(author,embed=embed)
      reaction1 = '🇲'
      reaction2 = '🇬'
      reaction3 = '🏵'
      reaction4 = '🎦'
      await client.add_reaction(dmmessage, reaction1)
      await client.add_reaction(dmmessage, reaction2)
      await client.add_reaction(dmmessage, reaction3)
      await client.add_reaction(dmmessage, reaction4)
      await client.say('📨 Check DMs For Information')

@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def kick(ctx,user:discord.Member):
    if user.server_permissions.kick_members:
      await client.say('**He is mod/admin and i am unable to kick him/her**')
      return
    else:
      await client.kick(user)
      await client.say(user.name+' was kicked. Good bye '+user.name+'!')
      await client.delete_message(ctx.message)
      for channel in user.server.channels:
        if channel.name == '╰☆☆-professional-log-☆☆╮':
            embed=discord.Embed(title="User kicked!", description="**{0}** is kicked by **{1}**!".format(user, ctx.message.author), color=0xFDE112)
            await client.send_message(channel, embed=embed)
@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)  
async def purge(ctx, number):
    number = int(number) #Converting the amount of messages to delete to an integer
    counter = 0
    async for x in client.logs_from(ctx.message.channel, limit = number+1):
        if counter < number:
            await client.delete_message(x)
            counter += 1
 
@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)      
async def ban(ctx,user:discord.Member):
    if user.server_permissions.ban_members:
      await client.say('**He is mod/admin and i am unable to ban him/her**')
      return
    else:
      await client.ban(user)
      await client.say(user.name+' was banned. Good bye '+user.name+'!')
      for channel in member.server.channels:
        if channel.name == '╰☆☆-professional-log-☆☆╮':
            embed=discord.Embed(title="User banned!", description="**{0}** banned by **{1}**!".format(member, ctx.message.author), color=0x38761D)
            await client.send_message(channel, embed=embed)
@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     
async def unban(ctx):
    ban_list = await client.get_bans(ctx.message.server)

    # Show banned users
    await client.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

    # Unban last banned user
    if not ban_list:
      await client.say('Ban list is empty.')
      return
    else:
      await client.unban(ctx.message.server, ban_list[-1])
      await client.say('Unbanned user: `{}`'.format(ban_list[-1].name))
      for channel in member.server.channels:
        if channel.name == '╰☆☆-professional-log-☆☆╮':
            embed=discord.Embed(title="User unbanned!", description="**{0}** unbanned by **{1}**!".format(ban_list[-1].name, ctx.message.author), color=0x38761D)
            await client.send_message(channel, embed=embed)
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def say(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if ctx.message.author.bot:
      return
    else:
      if not msg: await client.say("Please specify a message to send")
      else: await client.say(msg)
      
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def emojiids(ctx):
  for emoji in ctx.message.author.server.emojis:
    print(f"<:{emoji.name}:{emoji.id}>")
    print(" ")    

@client.command(pass_context = True)
async def wow(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:WOW:515854429485006848>')

@client.command(pass_context = True)
async def dank(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:OnThaCoco:515853700682743809>')

@client.command(pass_context = True)
async def santa(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:santa:517232271678504970>')

@client.command(pass_context = True)
async def hi(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:hi:517232279148429313>')

@client.command(pass_context = True)
async def lol(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:lol:517232283670020096>')

@client.command(pass_context = True)
async def love(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:love:517232300912672774>')

@client.command(pass_context = True)
async def mad(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:mad:517232301176913951>')

@client.command(pass_context = True)
async def alien(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:alien:517232332663422986>')

@client.command(pass_context = True)
async def fearfromme(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:shiroeglassespush:516174320532193289>')

@client.command(pass_context = True)
async def angry(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:angear:516174316950388772>')

@client.command(pass_context = True)
async def surprised(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:eyebigger:516174315058626560>')

@client.command(pass_context = True)
async def cat(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:agooglecat:516174312294842389>')

@client.command(pass_context = True)
async def thinking1(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:thinking:516183328613990400>')

@client.command(pass_context = True)
async def thinking2(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:thinking2:516183323127709699>')

@client.command(pass_context = True)
async def upvote(ctx):
    if ctx.message.author.bot:
      return
    else:
      await client.send_message(ctx.message.author, 'Upvote us: https://discordbots.org/bot/515403515217313795')
      await client.say('Check your dm for link')

@client.command(pass_context = True)
async def happy(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:happy:516183323052212236>')

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def rules(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Please specify a user to warn")
    else: await client.say(msg + ', Please Read Rules again and never break any one of them again otherwise i will mute/kick/ban you next time.')
    return

@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def bans(ctx):
    '''Gets A List Of Users Who Are No Longer With us'''
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of The Banned Idiots", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)

@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     

async def serverinfo(ctx):
    '''Displays Info About The Server!'''

    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))

    roles = ', '.join(roles);
    channelz = len(server.channels);
    time = str(server.created_at); time = time.split(' '); time= time[0];
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', color = discord.Color((r << 16) + (g << 8) + b));
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = '__ID__', value = str(server.id))
    join.add_field(name = '__Member Count__', value = str(server.member_count));
    join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='Created: %s'%time);

    return await client.say(embed = join);

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def norole(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Please specify a user to warn")
    else: await client.say(msg + ', Please Do not ask for promotions check Rules again.')
    return

@client.command(pass_context = True)
async def happybirthday(ctx, *, msg = None):
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Please specify a user to wish")
    await client.say('Happy birthday ' + msg + ' \nhttps://asset.holidaycardsapp.com/assets/card/b_day399-22d0564f899cecd0375ba593a891e1b9.png')
    return


@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def english(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Please specify a user to warn")
    else: await client.say(msg + ', Please do not use language other than **English.**')
    return


@client.command(pass_context = True) 
async def htmltutorial(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Please specify a user")
    else: await client.say('Welcome' + msg +  ', Please check http://uksoft.000webhostapp.com/Programming-Tutorials/index.html')
    return
   
@client.command(pass_context = True)
async def github(ctx, *, msg = None):
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Please specify respo. ``Format- https://github.com/uksoftworld/DarkBot``")
    else: await client.say('https://github.com/' + msg)
    return

@client.command(pass_context = True)
async def reactionroles(ctx, *, msg = None):
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Check this video to setup YAGPDB BOT- https://www.youtube.com/watch?v=icAqiw6txRQ")
    else: await client.say('Check this video to setup YAGPDB BOT- https://www.youtube.com/watch?v=icAqiw6txRQ ' + msg)
    return

@client.command(pass_context = True)
async def invite(ctx):
    if ctx.message.author.bot:
      return
    else:
      await client.say("Thanks for adding our bot.")
      embed=discord.Embed(title="Click on this link to invite:", description="https://discordapp.com/api/oauth2/authorize?client_id=518706448008478732&permissions=8&scope=bot" , color=0x00fd1b)
      await client.say(embed=embed)
@client.command(pass_context = True)
async def authlink(ctx):
    if ctx.message.author.bot:
      return
    else:
      await client.say("Thanks for adding our bot.")
      embed=discord.Embed(title="Click on this link to invite:", description="https://discordapp.com/api/oauth2/authorize?client_id=518706448008478732&permissions=8&scope=bot"" , color=0x00fd1b)
      await client.say(embed=embed)
@client.command(pass_context = True)
async def bottutorial(ctx, *, msg = None):
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Tutorial not found or maybe you have mistyped it")
    else: await client.say('https://github.com/uksoftworld/discord.py-tutorial/blob/master/' + msg + '.py')
    return

@client.command(pass_context = True)
async def dyno(ctx, *, msg = None):
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Command name not found or maybe you have mistyped it")
    else: await client.say('https://github.com/uksoftworld/dynoCC/blob/master/' + msg)
    return

@client.command(pass_context=True)
async def unverify(ctx):
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Unverified')
    await client.add_roles(ctx.message.author, role)
    
@client.command(pass_context=True)
async def verify(ctx):
    if ctx.message.author.bot:
      return
    else:
      await client.delete_message(ctx.message)
      role = discord.utils.get(ctx.message.server.roles, name='Verified')
      await client.add_roles(ctx.message.author, role)
    
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def friend(ctx, user:discord.Member,):
    if ctx.message.author.bot:
      return
    else:
      await client.delete_message(ctx.message)
      role = discord.utils.get(ctx.message.server.roles, name='Friend of Owner')
      await client.add_roles(ctx.message.mentions[0], role)

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def makemod(ctx, user: discord.Member):
    nickname = '♏' + user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    await client.add_roles(user, role)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Congratulations Message')
    embed.add_field(name = '__Congratulations__',value ='**Congratulations for mod.Hope you will be more active here. Thanks for your help and support.**',inline = False)
    embed.set_image(url = 'https://preview.ibb.co/i1izTz/ezgif_5_e20b665628.gif')
    await client.send_message(user,embed=embed)
    await client.delete_message(ctx.message)
    
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def removemod(ctx, user: discord.Member):
    nickname = user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    await client.remove_roles(user, role)
    await client.delete_message(ctx.message)

@client.command(pass_context = True)
async def botwarncode(ctx):
    await client.say('https://hastebin.com/ibogudoxot.py')
    return

@client.command(pass_context=True)
async def guess(ctx, number):
    try:
        arg = random.randint(1, 10)
    except ValueError:
        await client.say("Invalid number")
    else:
        await client.say('The correct answer is ' + str(arg))

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True) 
async def roles(context):
	"""Displays all of the roles with their ids"""
	roles = context.message.server.roles
	result = "The roles are "
	for role in roles:
		result += '``' + role.name + '``' + ": " + '``' + role.id + '``' + "\n "
	await client.say(result)
    
@client.command(pass_context=True, aliases=['server'])
@commands.has_permissions(kick_members=True)
async def membercount(ctx, *args):
    """
    Shows stats and information about current guild.
    ATTENTION: Please only use this on your own guilds or with explicit
    permissions of the guilds administrators!
    """
    if ctx.message.channel.is_private:
        await bot.delete_message(ctx.message)
        return

    g = ctx.message.server

    gid = g.id
    membs = str(len(g.members))
    membs_on = str(len([m for m in g.members if not m.status == Status.offline]))
    users = str(len([m for m in g.members if not m.bot]))
    users_on = str(len([m for m in g.members if not m.bot and not m.status == Status.offline]))
    bots = str(len([m for m in g.members if m.bot]))
    bots_on = str(len([m for m in g.members if m.bot and not m.status == Status.offline]))
    created = str(g.created_at)
    
    em = Embed(title="Membercount")
    em.description =    "```\n" \
                        "Members:   %s (%s)\n" \
                        "  Users:   %s (%s)\n" \
                        "  Bots:    %s (%s)\n" \
                        "Created:   %s\n" \
                        "```" % (membs, membs_on, users, users_on, bots, bots_on, created)

    await client.send_message(ctx.message.channel, embed=em)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def embed(ctx, *args):
    if ctx.message.author.bot:
      return
    else:
      argstr = " ".join(args)
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      text = argstr
      color = discord.Color((r << 16) + (g << 8) + b)
      await client.send_message(ctx.message.channel, embed=Embed(color = color, description=text))
      await client.delete_message(ctx.message)    

client.run(os.getenv('NTE4NzA2NDQ4MDA4NDc4NzMy.DvKdWg.ePUyZU_wwU0GbKWki7qup3KA8a8''))
