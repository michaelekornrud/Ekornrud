
import discord
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant
import youtube_dl

chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

client = discord.Client()
server = client.get_channel(id=902538622258008119)
#voice_channel = server.voice_client

load_dotenv()
TOKEN = os.getenv('TOKEN')
@client.event
async def on_connect():
    print("Apa connected to the server")
    channel = client.get_channel(id=902538865305354260)
    await channel.send("Apa just connected to the server")

@client.event
async def  on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Welcome To The Server {member}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("apa"):
        response = chatbot.request(message.content[4:])
        await message.channel.send(response)

    if message.content.startswith("/private"):
        await message.author.send("Hello there")

    if message.content.startswith("/play"):
        filename = chatbot.request(message.content[4:])
        voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeeg.exe", source=filename))

client.run(TOKEN)