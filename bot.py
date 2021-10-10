import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '&')

@client.event
async def on_ready():

  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="대화 "))
  
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith('&봇'):
        channel = message.channel
        await channel.send('**Bot**')


@client.event
async def on_message(message):
    msg = message.content
    if(msg == '&핑' or msg == '&ping'):
        embed = discord.Embed(title = ':ping_pong: 퐁!', description = str(client.latency) + 'ms', color = 0x00ff00)
        await message.channel.send(embed=embed)

@client.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@client.event
async def on_member_join(member):
    fmt = '{1.name} 에 오신것을 환영합니다., {0.mention} 님'
    channel = member.server.get_channel("channel_id_here")
    await client.send_message(channel, fmt.format(member, member.server))
 
@client.event
async def on_member_remove(member):
    channel = member.server.get_channel("channel_id_here")
    fmt = '{0.mention} 님이 서버에서 나가셨습니다.'
    await client.send_message(channel, fmt.format(member, member.server))

@client.event
async def on_member_join(member):
	if member.bot:
		embed = discord.Embed(title="Welcome!", description=member.mention + "님은 디스코드봇 입니다.", color=0x00aaaa)
		await member.add_roles(client.get_guild(863258651233615922).get_role(863261155312926791), reason="디스코드봇 자동부여")

@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)






client.run(os.environ['token'])