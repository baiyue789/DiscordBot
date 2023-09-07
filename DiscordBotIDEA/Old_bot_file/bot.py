import discord
import Responses
from discord.ext import commands
import Apkey
import random

async def send_message(message, user_message, is_private):
    try:
        response = Responses.messsrespond(user_message)
        if response:
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
def run_discord_bot():
    TOKEN = Apkey.TOKEN
    intents = discord.Intents.default()
    intents.message_content = True

    client = commands.Bot(command_prefix = '!',intents=intents)
    
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
    @client.command()
    async def hello(ctx):
        await ctx.channel.send("Hello I have spawned")
    @client.command()
    async def byebye(ctx):
        username = str(ctx.author)
        for x in range(len(username)):
            if username[x] == "#":
                await ctx.send(f"Bye bye {username[0:x]}")
    @client.command(name='roll')
    async def roll_dice(ctx):
        roll = random.randint(1, 6)
        if roll == 6:
            await ctx.send(f'You rolled a {roll}! Lucky you!')
        else:
            await ctx.send(f'You rolled a {roll}.')

    
#what happens when I start the server
    @client.event
    async def on_member_join(member):
        channel = client.get_channel(1101565279558959208)
        g = str(member)
        for x in range(len(g)):
            if g[x] == "#":
                await channel.send(f'Hello {g[0:x]}')
        await member.send(f'I know where u live')
    @client.event
    async def on_member_remove(member):
        channel = client.get_channel(1101565279558959208)
        g = str(member)
        for x in range(len(g)):
            if g[x] == "#":
                await channel.send(f'Goodbye {g[0:x]}')
        await member.send(f'I know where u live')
        
    @client.event
    async def on_message(message):

        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content) 
        channel = str(message.channel)

        print(f'{username} said "{user_message}" ({channel})')
        #Message that gets printed everytime a message runs


        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
        await client.process_commands(message)

    
    

    client.run(TOKEN)