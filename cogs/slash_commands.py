import disnake
from disnake.ext import commands


class SlashCommand(commands.Cog):
    def __init__(self, bot = commands.Bot):
        self.bot = bot


    @commands.slash_command(description="Сообщить о баге")
    async def bug(self, inter: disnake.ApplicationCommandInteraction):
        user_id = 145239961183059968
        msg = (f'YummiBOT. ver. 1.1\n\n\
Приветик ^^. Вижу, кто-то воспользовался этой командой. Значит, были найдены какие-то ошибки. Это отлично! Ведь я люблю находить ошибки, а благодаря тебе, {inter.author.mention}, я \
могу сделать бота ещё лучше!\n\nИтак, как же со мной связаться?\n1.  Discord: <@{user_id}>\n2. VK: https://vk.com/koraonearth\n3. \
Можешь прописать в любом из чатов (лучше всего в чате "берлога-бота") "кора", и тогда ты призовешь меня с корректором в лапках ^^. \n\nСпасибо, что помогаешь становиться боту лучше :3')


        embed = disnake.Embed(title="Заявка о баге", description= msg, color= disnake.Colour.green())
        embed.set_image(url="https://i.ibb.co/341ZX0b/zhuk.png")


        await inter.send(embed=embed)


    @commands.slash_command(description="Позвать тех, кто онлайн. Amount - количество свободных слотов.")
    async def here(self, inter:disnake.AppCommandInteraction, amount:int):
        await inter.response.defer()
        if amount == 1:
            await inter.edit_original_message(f"@here, общий подъем! Есть сексуальный слот! Присоединяйся!)")
        elif 2 <= amount <=4:
            await inter.edit_original_message(f"@here, общий подъем! Есть сексуальные {amount} слота! Присоединяйтесь!)")
        else:
            await inter.edit_original_message(f"@here, общий подъем! Есть сексуальные {amount} слотов! Присоединяйтесь!)")

        
        
#     @commands.slash_command(name= "happy_birthday", description="День Рождения")
#     async def birthday(self, inter: disnake.ApplicationCommandInteraction):
#         msg = "У нас сегодня именинник! <@459731062994632704>, с Днём Рождения! \n\n\
# Пусть я не так давно появилась на свет, но была впечатлена твоей проницательностью, дружелюбием, жизнерадостностью, умением радоваться за других, любви\
#  к приключениям и вечной тягой к участию во всём интересном!\n В этот радостный для всех день я.. я.. не знаю даже.. ХОЧУ ОБЪЯВИТЬ КАКОЙ-НИБУДЬ КОНКУРС, УАХАХХАХААААПЧХИ\
#  /чихнула от возбуждения/! \nВы можете прислать в специальный канал какую-нибудь работу, причем неважно какую! Это может быть видеозапись поздравления, \
# какой-нибудь Ваш рисунок на тему этого Дня Рождения, что угодно! Я буду коллекционировать это в течении дня, а потом.. потом.. НЕ ЗНАЮ! \nНЕ СМОТРИТЕ ТАК НА МЕНЯ! \
# МНЕ МЕНЬШЕ ДВУХ МЕСЯЦЕВ, Я ПОКА НЕ УМЕЮ ПРОДУМЫВАТЬ ПЛАНЫ ><\n\nВ-общем, давайте хорошенько порадуем Олю сегодня, потому что ей плохое настроение не очень подходит,\
#  она, как-никак, не Векс! А уж особенно сегодня! \nА по поводу наград, и как они будут выдаваться - давайте решим позже. Все-таки, я надеюсь, Вы это будете делать не ради них)) \
# Ну а сейчас празднуем, поздравляем, спим.. Ой, не то слово.. Какое же там слово должно быть.. АААА, ВСПОМНИЛА! И ВЕСЕЛИМСЯ!!!"
#         embed = disnake.Embed(title="С днем рождения, Оля!", description = msg, color= disnake.Colour.green())
#         await inter.send(embed = embed)


    @commands.slash_command(description="Чистка сообщений")
    @commands.has_permissions(administrator = True)
    async def clear(self, inter: disnake.ApplicationCommandInteraction, amount : int):
            await inter.channel.purge(limit = amount)
            await inter.response.defer()
            await inter.edit_original_message(f'Было удалено {amount} сообщений(-я)')
            await inter.channel.purge(limit = 1)

    @clear.error
    async def clear_error(self, inter: disnake.ApplicationCommandInteraction, error):
        if isinstance(error, commands.MissingPermissions):
            await inter.send(f'{inter.author.mention}, прости, но прав у тебя недостаточно :с')


    @commands.slash_command(description="Поздороваться")
    async def hello(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(f"Привет, {inter.author.mention}!")


    @commands.slash_command(name = "обнять", description="Обнять кого-нибудь")
    async def hug(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member = None):
        YummiBOTid = 990263560640794684
        if member == None:
            await inter.response.defer()
            await inter.edit_original_message(f"{inter.author.mention}, друг, а кого мне обнять? ^^")

        elif member.id == YummiBOTid:
            await inter.response.defer()
            await inter.edit_original_message(f"{inter.author.mention}, это очень мило, но мне сложно саму себя обнять :с. Но я разрешаю тебе меня обнять ^^ ")

        else: 
            await inter.response.defer()
            await inter.edit_original_message(f"{inter.author.mention} обнимает {member.mention}")   


    @commands.slash_command(name = "обнять_всех", description="Вы можете обнять всех!")
    async def hugall(self, inter: disnake.ApplicationCommandInteraction):
            await inter.response.defer()
            await inter.edit_original_message(f"{inter.author.mention} обнимает всех!! ^^")


    @commands.slash_command(name = "лизнуть", description="Лизнуть кого-то")
    async def lick(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member = None):
        YummiBOTid = 990263560640794684

        if member == None:
            await inter.response.defer()
            await inter.edit_original_message(f"{inter.author.mention}, ооо, да, я обожаю кого-то вылизывать :heart_eyes_cat:! Только скажи кого, и я сразу же на него брошусь!\
 Ну, чтобы облизать, разумеется ><. Meow ^^")

        elif member.id == YummiBOTid:
            await inter.response.defer()
            await inter.edit_original_message(f"{inter.author.mention}, о, себя вылизывать я люблю.. Ой, я проговорилась! Но только не при свидетелях!\
Извини, давай ты забудешь то, что я тебе сказала, пожалуйста ><? А я взамен.. Лизну тебя в щечку.. Договорились?")

        else:
            await inter.response.defer()
            await inter.edit_original_message(f'/Юми лизнула {member.mention}/')


    @commands.slash_command(name = "похвалить", description="Похвалить кого-нибудь")
    async def patpat(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member = None):
        YummiBOTid = 990263560640794684
        if member == None:
            await inter.response.defer()
            await inter.edit_original_message(f"{inter.author.mention}, кто тут такой молодец и отличился? Подскажи мне! ^^")

        elif member.id == YummiBOTid:
            await inter.response.defer()
            await inter.edit_original_message(f"{inter.author.mention}, UwU, спасибо, я рада стараться!")
        
        else:
            await inter.response.defer()
            await inter.edit_original_message(f"{inter.author.mention} похвалил(-а) {member.mention}")


    @commands.slash_command(name = "погладить", description="Погладить кого-нибудь")
    async def pet(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member = None):
        YummiBOTid = 990263560640794684
        if member == None:
            await inter.response.defer()
            await inter.edit_original_message(f"{inter.author.mention}, кто тут заслуживает того, чтобы его погладили? Подскажи ^^")

        elif member.id == YummiBOTid:
            await inter.response.defer()
            await inter.edit_original_message(f"{inter.author.mention}, UwU, спасибо, это очень мило!")
        
        else:
            await inter.response.defer()
            await inter.edit_original_message(f"{inter.author.mention} погладила {member.mention}")


    @commands.slash_command(description="Проверка пинга")
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(f"Pong!\n-----------------------------\nPing is: {round(self.bot.latency * 1000)} ms")


    @commands.slash_command(name = "поцарапать", description="Поцарапать кого-нибудь")
    async def scratch(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member = None):
        YummiBOTid = 990263560640794684
        if member == None:
            await inter.response.defer()
            await inter.edit_original_message(f"{inter.author.mention}, а кого мне цапнуть? Кто вел себя плохо? :smirk_cat:")

        elif member.id == YummiBOTid:
            await inter.response.defer()
            await inter.edit_original_message(f"{inter.author.mention}, неее, я не мазохистка! Я кошечка! Meow!")
        
        else:
            await inter.response.defer()
            await inter.edit_original_message(f"/Юми царапнула {member.mention}")


    @commands.slash_command(description="Общая информация о сервере")
    async def server(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(f"Название сервера: {inter.guild.name}\nУчастников: {inter.guild.member_count}\nСоздан: {inter.guild.created_at}")


    @commands.slash_command(name = "спокойной_ночи", description="Можно пожелать сладких снов")
    async def sleep(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member = None):
        YummiBOTid = 990263560640794684
        if member == None:
            await inter.response.defer()
            await inter.edit_original_message(f"{inter.author.mention}, хехе, и кто у нас идёт спать?")

        elif member.id == YummiBOTid:
            await inter.response.defer()
            await inter.edit_original_message(f"{inter.author.mention}, нет, спасибо, я на дежурстве! :smile_cat:")
        
        else:
            await inter.response.defer()
            await inter.edit_original_message(f"{inter.author.mention} желает сладких снов {member.mention}")
            


def setup(bot: commands.Bot):
    bot.add_cog(SlashCommand(bot))
    print(f"> Extension {__name__} is ready")