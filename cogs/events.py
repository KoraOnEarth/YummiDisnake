import disnake
from disnake.ext import commands



class Events(commands.Cog):
    def __init__(self, bot = commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Юми проснулась!")


    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f"Welcome {member.mention} to {guild.name}!"
            await guild.system_channel.send(to_send)


    @commands.Cog.listener()
    async def on_message(self, message):

        username = str(message.author).split('#')[0]
        user_message = str(message.content)
        channel = str(message.channel.name)
        print(f"{username}: {user_message} ({channel})")

        r_mother = ['ща мать придет', 'маам', 'ратная мать', 'miriadrin', 'маман', 'мамочка', 'меня обижают', 'мам', 'мама', 'мать']
        r_kora = ['кора, я вызываю тебя', 'кора', 'программист', 'чей бот', 'создатель бота', 'никитос']

        if message.author == disnake.user:
                return

        msg = message.content.lower()

        if msg in r_kora:
            user_id = 145239961183059968
            await message.channel.send(f"<@{user_id}>, wake up, samurai!")
    
        if msg in r_mother:
            user_id = 459731062994632704
            await message.channel.send(f"<@{user_id}>, проснись, мать!")


def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))
    print(f"> Extension {__name__} is ready")