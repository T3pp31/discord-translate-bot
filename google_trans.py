import json

import discord
from deep_translator import GoogleTranslator
from langdetect import detect

config = open("google_settings.json")
config = json.load(config)

#Discordトークン
Discord_Token = config['token']

#動作指定チャンネル
Discord_channel_ID = config['discord_id']

Intents = discord.Intents.default()
Intents.message_content = True

client = discord.Client(intents=Intents)

#言語判定
def language(text):
    lang = detect(text)
    return lang

#起動時動作
@client.event
async def on_ready():
    print("起動しました")

#翻訳動作
@client.event
async def on_message(message):
    #指定チャンネル以外は無視．チャンネル指定が特にない場合はコメントアウトしてください
    #if message.channel.id != Discord_channel_ID:
    #    return

    #botのメッセージは無視
    if message.author == client.user:
        return

    #Bot終了
    if message.content.startswith("おやすみ"):
        await message.channel.send("おやすみ，また今度")
        await client.close()
        exit()
    print(message.content)
    #言語自動判定
    source_lang = language(message.content)

    if source_lang == "ja":
        target_lang = "en"
    elif source_lang = "en":
        target_lang = "ja"
    else:
        target_lang = "ja"
        source_lang = "zh-TW"

    translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(message.content)
    print(translated_text)
    await message.channel.send(translated_text)

client.run(Discord_Token)
