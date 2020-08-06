from discord.ext import commands
from discord.ext import tasks
import os
import traceback
import discord
from datetime import datetime 

token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID =739463355864973342  #チャンネルID

# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')


# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    
    if now == '03:59':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:xjp_coin:739314187532107846> <:xjp_coin:739314187532107846> <:xjp_coin:739314187532107846> ') 
    
    if now == '05:26':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:xjp_coin:739314187532107846> <:xjp_coin:739314187532107846> <:xjp_coin:739314187532107846> ') 
        
    if now == '08:26':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/740511753149874266/740548333420150784/xjptop02.png')      
    
    if now == '09:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://discordapp.com/channels/698412123809644644/740511753149874266/740550705521098812') 
        
    if now == '11:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:xjp_coin:739314187532107846> <:xjp_coin:739314187532107846> <:xjp_coin:739314187532107846>  ') 

    if now == '12:11':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/740511753149874266/740548095682674749/xjp-top2.png')
    
    if now == '13:50':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/740511753149874266/740550699162664980/XJP_LOGO.png')
          
    if now == '15:48':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('🥳 <:xjp_coin:739314187532107846> ')
        
    if now == '16:48':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:xjp_coin:739314187532107846> <:xjp_coin:739314187532107846> <:xjp_coin:739314187532107846> ')
        
    if now == '19:48':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://discordapp.com/channels/698412123809644644/740511753149874266/740548333646381086')
        
    if now == '22:48':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/740511753149874266/740548095682674749/xjp-top2.png')
        
    if now == '23:59':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:xjp_coin:739314187532107846> <:xjp_coin:739314187532107846> <:xjp_coin:739314187532107846>')

  
#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(token)
