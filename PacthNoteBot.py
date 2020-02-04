import discord
import datetime
import asyncio

client = discord.Client()

now = datetime.datetime.now()
nowDate = now.strftime('%Y-%m-%d')

@client.event
async def on_ready():
    print('Bot start')
    game = discord.Game(nowDate)
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith('.공지'):
        embed = discord.Embed(title="공지", description="지성과 함께 찾아온 디스코드 공지, 패치노트를 알려주는 로봇입니다. 잘부탁드려요!", color=0x555555)
        await message.channel.send(embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
