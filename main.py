import discord
from discord.ext import commands
import os

#get the token
with open("token.txt", "r", encoding="utf-8") as file:
    TOKEN = file.read()

#init the bot
client = commands.Bot(command_prefix = ".", help_command=None)

#load extension
print("load extension : ")
#list file in cogs directory and load python ones
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(str("cogs."+filename[:-3])) #[:-3] -> remove ".py" to file name
        print("   " + str(filename[:-3]))
print("done !")
print("wait for the bot be ready")  


client.run(TOKEN)