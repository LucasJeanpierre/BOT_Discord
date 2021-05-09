#base extension

import discord
from discord.ext import commands

#get bot prefix
prefix = "."

class Base(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('the bot is ready')

    @commands.command()
    @commands.guild_only()
    async def ping(self, ctx):
        print("ping")
        await ctx.send("pong | latency : " + str(round(self.client.latency * 1000)) + "ms")


    @commands.command(pass_context=True)
    @commands.guild_only()
    async def help(self, ctx):
        message = "```"
        message += "Liste des commandes : \n"
        message += "   " + prefix + "ping" + "\n"
        message += "   " + prefix + "meme" + "\n"
        message += "   " + prefix + "poll_simple" + "\n"        
        message += "   " + prefix + "poll" + "\n"
        message += "   " + prefix + "poll_list" + "\n"
        message += "```"
        await ctx.send(message)

        

def setup(client):
    client.add_cog(Base(client))
    

    
