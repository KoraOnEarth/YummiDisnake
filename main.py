import disnake
from disnake.ext import commands


bot = commands.Bot(command_prefix='!', intents= disnake.Intents.all(), activity = disnake.Game('клубочек', status = disnake.Status.online))
bot.remove_command('help')


bot.load_extension("cogs.slash_commands")
bot.load_extension("cogs.weather")
bot.load_extension("cogs.events")


token = open('token.txt', 'r').readline()
bot.run(token)