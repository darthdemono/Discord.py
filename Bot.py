import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
from Setup import *
import sys
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client = commands.Bot(command_prefix=defprefix)
client.remove_command("help")
# removing Help

extensions = [
    "commands.Moderation",
    "commands.Covid",
    "commands.Extras",
    "commands.Help",
]



if __name__ == "__main__":
    for ext in extensions:
        client.load_extension(extensions)

keep_alive()

client.run(TOKEN)
