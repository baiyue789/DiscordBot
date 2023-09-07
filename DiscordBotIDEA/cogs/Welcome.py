import discord 
from discord.ext import commands
CHANNEL = 1101565279558959208
class Welcome(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Welcome commands are ready")
    
       
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(CHANNEL)
        g = str(member)
        
        await channel.send(f'Greetings, {g[0:-5]}.')
        await member.send(f'Welcome to bot channel')
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member.name} has left the server.")

        channel = self.client.get_channel(CHANNEL)
        if channel:
            try:
                await channel.send(f"Goodbye {member.name}!")
            except discord.Forbidden:
                print("The bot doesn't have permission to send messages in the channel.")
        else:
            print("The channel could not be found.")
        
                
            
async def setup(client):
    await client.add_cog(Welcome(client))