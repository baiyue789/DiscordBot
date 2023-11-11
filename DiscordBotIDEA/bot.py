import discord
import Responses
from discord.ext import commands
import os
import Apkey
import asyncio
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
TOKEN = Apkey.TOKEN
CHANNEL = Apkey.CHANNEL
async def send_message(message, user_message, is_private):
    try:
        response = Responses.messsrespond(user_message)
        if response:
            if is_private:
                await message.author.send(response)  
            else:
                await message.channel.send(response)
    except Exception as e:
        print(e)
        
@client.event 
async def on_ready():
    print("\nready for use")
    print("----------------------------")
async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith(".py"):
            await client.load_extension(f'cogs.{filename[:-3]}')
            print(f'{filename[:-3]} has loaded')
    
@client.event
async def on_message(message):
    try:
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said "{user_message}" ({channel})')
        if user_message.startswith('?'):
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            try:
                if Responses.messsrespond(user_message) == True:
                    await message.delete()
                    await message.channel.send("No")
                else:
                    await send_message(message, user_message, is_private=False)
            except Exception as e:
                print(e)
        await client.process_commands(message)
    except Exception as e:
        print(e)

async def main():
    async with client:
        await load()
        await client.start(TOKEN)
asyncio.run(main())