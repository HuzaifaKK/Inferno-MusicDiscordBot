import discord
import time
import os
import youtube_dl
from pathlib import Path
from discord.ext import commands

token = "Your Bot Token Here"
youtube_dl.utils.bug_reports_message = lambda: ''

ltime = time.asctime(time.localtime())
intents = discord.Intents.default()
# ================================================================================================================


client = commands.Bot(intents=intents, command_prefix='?')
cwd = Path(__file__).parents[0]
cwd = str(cwd)
extensions = ['join', 'leave', 'pause', 'resume', 'summon', 'stop', 'play']
client.remove_command('help')

for file in os.listdir(cwd + '/Cogs'):
    if file.endswith(".py"):
        extensions.append("Cogs." + file[:-3])

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('Loading. [{}]'.format(extension, error))


@client.event
async def on_ready():
    print(f'[INFO {ltime}]: Logged in as {client.user.name}!')

# <--- Bot Run --->
client.run(token)
