import disnake
from disnake.ext import commands
import os


bot = commands.Bot(command_prefix='!', intents=disnake.Intents.all(), activity=disnake.Streaming(
    platform="YouTube",
    name="игру в клубочек", 
    url="https://www.youtube.com/watch?v=5qap5aO4i9A"))

bot.remove_command('help')


bot.load_extension("cogs.slash_commands")
bot.load_extension("cogs.weather")
bot.load_extension("cogs.events")



token = os.getenv('token')
bot.run(token)