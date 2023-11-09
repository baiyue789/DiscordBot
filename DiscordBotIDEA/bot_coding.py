import discord
import Responses
from discord.ext import commands
from discord import FFmpegPCMAudio
import random
import Apkey
import os
import asyncio

class MyHelpCommand(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        # This will send a message to the user with a list of all available commands.
        # The list will be sorted alphabetically.
        embed = discord.Embed(title='List of Commands', color=discord.Color.blue())
        for cog, commands in mapping.items():
            command_list = [command.name for command in commands]
            if command_list:
                cog_name = getattr(cog, 'qualified_name', 'Other')
                embed.add_field(name=cog_name, value='\n'.join(command_list), inline=False)
        await self.get_destination().send(embed=embed)

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '//', intents=intents)

TOKEN = Apkey.TOKEN

async def send_message(message, user_message, is_private):
    try:
        response = Responses.messsrespond(user_message)
        if response:
            if is_private:
                await message.author.send(response)  
            else:
                try:
                    if Responses.messsrespond(user_message) == True:
                        await message.delete()
                        await message.channel.send("No")
                    else:
                        await send_message(message, user_message, is_private=False)
                except Exception as e:
                    print(e)
    except Exception as e:
        print(e)


@client.event
async def on_ready():
    print("ready for use")
    print("----------------------------")
@client.command()
async def Byebye(ctx):
    username = str(ctx.author)
    await ctx.send(f"Farewell, {username[0:-5]}.")
@client.command(name='roll')
async def roll_dice(ctx):
    roll = random.randint(1, 6)
    if roll == 6:
        await ctx.send(f'You rolled a {roll}! Lucky you!')
    else:
        await ctx.send(f'You rolled a {roll}.')
@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        voice = await channel.connect()
    else:
        await ctx.send("You must be in a voice channel to run this command.")
@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.guild.voice_client): # Check if the bot is connected to a voice channel
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Left the voice channel")
    else:
        await ctx.send("I'm not connected to a voice channel")
@client.command(pass_context = True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("no audio playing")
@client.command(pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("No song is paused")
@client.command(pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
"""Sound playing parts of the code"""
@client.command(pass_context = True)
async def playAudio(ctx, filename):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    path = os.path.join(os.getcwd(), "Music", filename)  # join the filename with the path to the "music" folder
    if not os.path.isfile(path):
        await ctx.send(f"File '{filename}' not found.")
        return
    source = FFmpegPCMAudio(path)
    player = voice.play(source)
    


# End of commands

@client.event
async def on_member_join(member):
    channel = client.get_channel(1101565279558959208)
    g = str(member)
    
    await channel.send(f'Greetings, {g[0:-5]}.')
    await member.send(f'I know where u live')

@client.event
async def on_member_remove(member):
    channel = client.get_channel(1101565279558959208)
    g = str(member)
    await channel.send(f'Goodbye {g[0:-5]}')
    await member.send(f'I know where u live')

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
            await send_message(message, user_message, is_private=False)

        await client.process_commands(message)

    except Exception as e:
        print(e)

async def main():
    async with client:
    
        await client.start(TOKEN)

asyncio.run(main())