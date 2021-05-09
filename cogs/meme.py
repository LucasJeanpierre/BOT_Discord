#meme extension

import discord
from discord.ext import commands
import requests

urldark="https://meme-api.glitch.me/dank"
urlmoderate="https://meme-api.glitch.me/moderate"
urllight="https://meme-api.glitch.me/light"


class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def meme(self, ctx, arg):
        print("meme",arg)
        if (arg == "dark"):
            url = urldark
        elif (arg == "moderate"):
            url = urlmoderate
        elif (arg == "light"):
            url = urllight
        else :
            url = "Null"

        if (url != "Null"):
            r = requests.get(url)
            content = r.json()
            memeurl = content['meme']
            await ctx.send(memeurl)
        else:
            await ctx.send("Argument invalide")

    @meme.error
    async def meme_error(self, ctx, error):
        if (isinstance(error, commands.NoPrivateMessage)):
            pass
        else:
            await ctx.send("Veulliez préciser le niveau d'humour")


def setup(client):
    client.add_cog(Meme(client))
    

    
