#private extension

import discord
from discord.ext import commands

async def is_me(ctx):
    return ctx.author.id == 0

class Private(commands.Cog):
    def __init__(self, client):
        self.client = client

    #send message from the bot to a channel
    @commands.command()
    @commands.check(is_me)
    async def message(self, ctx, message, channel):
        channel = self.client.get_channel(int(channel))
        await channel.send(message)


    @commands.command()
    @commands.check(is_me)
    async def test(self, ctx):
        print("test")




def setup(client):
    client.add_cog(Private(client))
    

    
