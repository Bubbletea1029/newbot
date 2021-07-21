import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="대화 "))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

@client.event
async def on_message(message):
    # 메세지를 보낸 사람이 봇일 경우 무시한다
    if message.author.bot:
        return None

    if message.content.startswith('!버블티'):
        channel = message.channel
        await channel.send('개발자')

    if message.content.startswith('!봇정보'):
        channel = message.channel
        await channel.send('```BBTEA BOT V0.2```')

    if message.content.startswith('!개발엔진'):
        channel = message.channel
        await channel.send('```Node.js(구)Python 3.9.6(현)```')
    
    if message.content.startswith('!거내뉸'):
        channel = message.channel
        await channel.send('```자가번식을 하는 생물```')

    if message.content.startswith('!니코'):
        channel = message.channel
        await channel.send('더두미 ㅋㅋ루빗봉')
    
    if message.content.startswith('!닏고'):
        channel = message.channel
        await channel.send('더두미 ㅋㅋ루빗봉')

    if message.content.startswith('!밥먹어'):
        channel = message.channel
        await channel.send('```냠냠```')

    if message.content.startswith('!밥먹기'):
        channel = message.channel
        await channel.send('```3의 허기를 채웠다!```')

    if message.content.startswith('!밥보유'):
        channel = message.channel
        await channel.send('```밥 개수는 무한대에요!```')

    if message.content.startswith('!레나'):
        channel = message.channel
        await channel.send('```해킹장인```')

    if message.content.startswith('!팤아'):
        channel = message.channel
        await channel.send('```그는 신이야!```')

    if message.content.startswith('!태움'):
        channel = message.channel
        await channel.send('```강타텔미드집공유미```')

    if message.content.startswith('!펭귄'):
        channel = message.channel
        await channel.send('```커피중독 서버장```')

    if message.content.startswith('!발로충'):
        channel = message.channel
        await channel.send('```그냥 개10악질```')

    if message.content.startswith('!토토'):
        channel = message.channel
        await channel.send('```레식장인```')

    if message.content.startswith('!대니'):
        channel = message.channel
        await channel.send('```푸른냥이```')

    if message.content.startswith('!푸른냥이'):
        channel = message.channel
        await channel.send('```대니```')

    if message.content.startswith('!프리미엄'):
        channel = message.channel
        await channel.send('```그딴건 없다```')  

    if message.content.startswith('!코드보기'):
        channel = message.channel
        await channel.send('```프리미엄 전용 기능이에요! !프리미엄 으로 정보를 확인해주세요!```') 

    if message.content.startswith('!주은'):
        channel = message.channel
        await channel.send('```좋은```')

    if message.content.startswith('!아무'):
        channel = message.channel
        await channel.send('```쿠키런 선생님```')

    if message.content.startswith('!스크립트'):
        channel = message.channel
        await channel.send('```개악질중에 악질```')

    if message.content.startswith('!안녕'):
        channel = message.channel
        await channel.send('```안녕하세요!```')

    if message.content.startswith('!명령어'):
        channel = message.channel
        await channel.send('```알아서들 탐구하세요~```')

    if message.content.startswith('!세트'):
        channel = message.channel
        await channel.send('```"강펀치"```')

    if message.content.startswith('!반가워'):
        channel = message.channel
        await channel.send('```"반가워요!"```')

    if message.content.startswith('!고루고루'):
        channel = message.channel
        await channel.send('```음...```')

    if message.content.startswith('!태피스'):
        channel = message.channel
        await channel.send('```음...```')

    if message.content.startswith('!아기 해 텔레토비'):
        channel = message.channel
        await channel.send('```대니```')

    if message.content.startswith('!더워'):
        channel = message.channel
        await channel.send('```쿨러 밑은 시원해요!```')

    if message.content.startswith('!붕카즈치'):
        channel = message.channel
        await channel.send('```로봇인가요?```')

    if message.content.startswith('!마냥'):
        channel = message.channel
        await channel.send('```선배님이에요!```')

    if message.content.startswith('!크시'):
        channel = message.channel
        await channel.send('```대선배님이세요!```')

    if message.content.startswith('!상어집'):
        channel = message.channel
        await channel.send('```좋은 서버죠!```')

    if message.content.startswith('!석현'):
        channel = message.channel
        await channel.send('```악질```')

    if message.content.startswith('!CPU'):
        channel = message.channel
        await channel.send('```여기 CPU는 너무 어둡고 더워```')

    if message.content.startswith('!토토'):
        channel = message.channel
        await channel.send('*병신*')
    


client.run(os.environ['token'])