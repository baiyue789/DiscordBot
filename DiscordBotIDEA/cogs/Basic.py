import discord 
from discord.ext import commands
import random
class Basic(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Basic commands are ready")
        
    @commands.command()
    async def ping(self, ctx):
        bot_latiency = round(self.client.latency * 1000)
        await ctx.send(f'Ping {bot_latiency}')
    
    @commands.command(name='roll')
    async def roll_dice(self, ctx):
        roll = random.randint(1, 6)
        if roll == 6:
            await ctx.send(f'You rolled a {roll}! Lucky you!')
        else:
            await ctx.send(f'You rolled a {roll}.')
    
                
            
async def setup(client):
    await client.add_cog(Basic(client))