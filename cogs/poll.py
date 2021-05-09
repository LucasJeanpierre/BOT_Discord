#sondage extension

import discord
from discord.ext import commands

list_number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
list_emoji = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
botname = "BOT_TEST#3918"


class Poll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_any_role("Pro")
    async def poll_simple(self, ctx, *args):
        print("poll simple")
        if (len(args) == 0):
            await ctx.send("wrong arguments")
        elif len(args) < 12:
            #build message
            content = "**" + args[0] + "**" + "\n"
            for i in range(1,len(args)):
                content += ":" + list_number[i-1] + ":" + " " + args[i] + "\n"
            message = await ctx.send(content)

            #add reactions
            for i in range(len(args)-1):
                await message.add_reaction(list_emoji[i])
        else:
            await ctx.send("Too many arguments")

    @commands.command()
    @commands.has_any_role("Pro")
    async def poll(self, ctx, *args):
        print("poll")
        if (len(args) == 0):
            await ctx.send("wrong arguments")
        elif len(args) < 12:
            #build message
            embed=discord.Embed(title="*"+args[0]+"*", color=0x622567)
            for i in range(1,len(args)):
                #embed.add_field(name=args[i], value=":" + list_number[i-1] + ":", inline=False)    #chiffre en dessous du message
                embed.add_field(name=":" + list_number[i-1] + ":", value=args[i], inline=False)     #chiffre au dessus du message
            message = await ctx.send(embed=embed)

            #add reactions
            for i in range(len(args)-1):
                await message.add_reaction(list_emoji[i])
        else:
            await ctx.send("Too many arguments")

    #user list who react to poll
    #1 arg if your on the channel where the poll was send. arg will be the message id
    #2 arg if your on an other channel, first is message id and second is channel id where the poll was send
    @commands.command()
    @commands.has_any_role("Pro")
    async def poll_list(self, ctx, *args):
        print("poll list")
        if (len(args) == 0):
            await ctx.send("wrong arguments")
        elif (len(args) == 1):
            msg = await ctx.fetch_message(args[0])
            content = "```"
            for reaction in msg.reactions:
                content += str(reaction) + "\n"
                async for user in reaction.users():
                    if (str(user) != botname):
                        content += "    " + str(user) + "\n"
                content += "\n"
            content += "```"
            if (content != "``````"):
                await ctx.send(content)
            else:
                await ctx.send("wrong arguments")

        elif (len(args) == 2):
            channel = self.client.get_channel(int(args[1]))
            msg = await channel.fetch_message(args[0])
            content = "```"
            for reaction in msg.reactions:
                content += str(reaction) + "\n"
                async for user in reaction.users():
                    if (str(user) != botname):
                        content += "    " + str(user) + "\n"
                content += "\n"
            content += "```"
            if (content != "``````"):
                await ctx.send(content)
            else:
                await ctx.send("wrong arguments")
        else:
            await ctx.send("wrong arguments")



        #error managment

        @poll.error
        async def poll_error(self, ctx, error):
            if (isinstance(error, commands.NoPrivateMessage)):
                pass
            else:
                await ctx.send("wrong arguments")

        @poll_list.error
        async def poll_list_error(self, ctx, error):
            if (isinstance(error, commands.NoPrivateMessage)):
                pass
            else:
                await ctx.send("wrong arguments")

        @poll_simple.error
        async def poll_simple_error(self, ctx, error):
            if (isinstance(error, commands.NoPrivateMessage)):
                pass
            else:
                await ctx.send("wrong arguments")





def setup(client):
    client.add_cog(Poll(client))


    
