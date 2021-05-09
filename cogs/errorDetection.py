#error detection extension

import discord
from discord.ext import commands

class ErrorDetection(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send ('Commande invalide')


def setup(client):
    client.add_cog(ErrorDetection(client))
    

    
