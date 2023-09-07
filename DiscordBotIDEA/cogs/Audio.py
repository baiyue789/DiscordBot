import discord 
from discord.ext import commands
import random
from discord import FFmpegPCMAudio
import os
class Audio(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Audio commands ready")
        
    @commands.command(pass_context = True)
    async def join(self, ctx):
        if (ctx.author.voice):
            channel = ctx.author.voice.channel
            voice = await channel.connect()
        else:
            await ctx.send("You must be in a voice channel to run this command.")
    @commands.command(pass_context = True)
    async def leave(self, ctx):
        if (ctx.guild.voice_client): # Check if the bot is connected to a voice channel
            await ctx.guild.voice_client.disconnect()
            await ctx.send("Left the voice channel")
        else:
            await ctx.send("I'm not connected to a voice channel")
    @commands.command(pass_context = True)
    async def pause(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("no audio playing")
    @commands.command(pass_context = True)
    async def resume(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("No song is paused")
    @commands.command(pass_context = True)
    async def stop(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        voice.stop()
    """Sound playing parts of the code"""
    @commands.command(pass_context = True)
    async def playAudio(self,ctx, filename):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        path = os.path.join(os.getcwd(), "Music", filename)  # join the filename with the path to the "music" folder
        if not os.path.isfile(path):
            await ctx.send(f"File '{filename}' not found.")
            return
        source = FFmpegPCMAudio(path)
        player = voice.play(source)
                
            
async def setup(client):
    await client.add_cog(Audio(client))