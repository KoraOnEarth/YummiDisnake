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
            to_send = f"Добро пожаловать, {member.mention}! Рады тебя видеть в нашей семье!"
            await guild.system_channel.send(to_send)


    @commands.Cog.listener()
    async def on_message(self, message):

        username = str(message.author).split('#')[0]
        user_message = str(message.content)
        channel = str(message.channel.name)
        print(f"{username}: {user_message} ({channel})")

        r_mother = ['ща мать придет', 'маам', 'ратная мать', 'miriadrin', 'маман', 'мамочка', 'меня обижают', 'мам', 'мама', 'мать']
        r_kora = ['кора, я вызываю тебя', 'кора', 'программист', 'чей бот', 'создатель бота', 'никитос']


        msg = message.content.lower()


        YummiBOT = f"<{990263560640794684}>"
        if message.author == YummiBOT:
                return


        if msg in r_kora:
            user_id = 145239961183059968
            await message.channel.send(f"<@{user_id}>, wake up, samurai!")
    
        if msg in r_mother:
            user_id = 459731062994632704
            await message.channel.send(f"<@{user_id}>, проснись, мать!")

        if ' cute' in msg:
            await message.add_reaction("<a:cute:992591736922710096>")

        if ' uwu' in msg:
            await message.add_reaction("<a:cute:992591736922710096>")

        if ' мило' in msg:
            await message.add_reaction("<a:cute:992591736922710096>")

        if ' милота' in msg:
            await message.add_reaction("<a:cute:992591736922710096>")

        if ' уву' in msg:
            await message.add_reaction("<a:cute:992591736922710096>")

        if ' увуу' in msg:
            await message.add_reaction("<a:cute:992591736922710096>")

        if ' азир' in msg:
            await message.channel.send("Какой большой император :scream_cat:")

        if ' акали' in msg:
            await message.channel.send("Йо-йо-йой! Мы ведь друзья, правда? Ты не будешь за мной гоняться? :scream_cat:")

        if ' алистар' in msg:
            await message.channel.send("Ты как из лабиринта выбрался, чудище? :joy_cat:")

        if ' амуму' in msg:
            await message.channel.send("Ну, ну, не грусти, будет тебе :smiley_cat:")

        if ' анивия' in msg:
            await message.channel.send("Птички могут летать? Ха, подумаешь! Я тоже могу! :joy_cat:")

        if ' ари' in msg:
            await message.channel.send("Какая красивая лисичка :heart_eyes_cat:")

        if ' атрокс' in msg:
            await message.channel.send("Я так полагаю, тебя хилить не надо, ты сам, да? :smile_cat:")

        if ' аурелион сол' in msg:
            await message.channel.send("Дракончик! Люблю дракончиков! :heart_eyes_cat:")

        if ' афелий' in msg:
            await message.channel.send("Хочу тебя лизнуть :heart_eyes_cat:\n/Юми лизнула Афелия/")

        if ' бард' in msg:
            await message.channel.send("О, это ты постоянно оставляешь своего адк? Я слышала о тебе.. От одного грустного адк.. <:he:986760218753003560>")

        if ' белвет' in msg:
            await message.channel.send("Приветствую, императрица! Кстати, ты не видела моего хозяина?")

        if ' бел`вет' in msg:
            await message.channel.send("Приветствую, императрица! Кстати, ты не видела моего хозяина?")

        if ' брэнд' in msg:
            await message.channel.send("О, ты тёпленький...Мне кажется, или запахло палёной шерстью?")

        if ' вай' in msg:
            await message.channel.send("О, я слышала, тебе нравится повелительница красной точки? :heart_eyes_cat:")

        if ' варвик' in msg:
            await message.channel.send("Мой мурлык громче твоего рыка, пёс.")

        if ' вейгар' in msg:
            await message.channel.send("А что ты мне сделаешь, если я пошучу про бег на короткие дистанции? ОЙ-ОЙ-ОЙ, Я ПОНЯЛА :scream_cat:")

        if ' вейн' in msg:
            await message.channel.send('Начинаем операцию "Дожить до лейта" :scream_cat:')

        if ' векс' in msg:
            await message.channel.send("Знаешь, когда моя хозяйка убирала за мной, у неё было примерно такое же лицо :smile_cat:\nА ещё она была примерно твоего роста, кстати..")

        if ' велкоз' in msg:
            await message.channel.send("Пусти зайчика, Вел'Коз! Хочу поиграть!")

        if ' виего' in msg:
            await message.channel.send('/Юми его лизнула :heart_eyes_cat:/')

        if ' виктор' in msg:
            await message.channel.send('Так это ты управляешь красной точкой? ')

        if ' волибир' in msg:
            await message.channel.send('Медведи только рычать и умеют! РРРРАУ!')

        if ' галио' in msg:
            await message.channel.send('Арррр, дурацкая большая когтеточка!')

        if ' гангпланк' in msg:
            await message.channel.send('Спорим, у тебя не сработают твои бочки? Знаешь почему? Дам подсказку - я кошка, хе-хе :smirk_cat:')

        if ' гнар' in msg:
            await message.channel.send('Ууу, милашка.. ОЙ, А ТЫ БЫСТРО РАСТЕШЬ :smile_cat:')

        if ' грагас' in msg:
            await message.channel.send('НУ ЧЕ /ик/ ПОГНАЛИ! :smirk_cat:')

        if ' грейвз' in msg:
            await message.channel.send('О, а ты, случаем, не контришь Лиллию? А то её маму вроде как законтрил дробовик <:he:986760218753003560>')

        if ' зайра' in msg:
            await message.channel.send('Я пожую твою листья, а потом выплюну! :smirk_cat:')

        if ' маокай' in msg:
            await message.channel.send('Я пожую твою листья, а потом выплюну! :smirk_cat:')

        if ' иверн' in msg:
            await message.channel.send('Я пожую твою листья, а потом выплюну! :smirk_cat:')

        if ' нами' in msg:
            await message.channel.send('Рыбка, рыбка! Мяу!~ <:he:986760218753003560>')

        if ' физз' in msg:
            await message.channel.send('Рыбка, рыбка! Мяу!~ <:he:986760218753003560>')

        if ' киндред' in msg:
            await message.channel.send('Умелая охотница неслышно подкрадывается к добыче.')

        if ' когмао' in msg:
            await message.channel.send("Смотри, Ког'Мао! Я тоже так умею! /отхаркивает шерсть/")

        if ' мордекайзер' in msg:
            await message.channel.send('Ты не получишь книгу, большой железный кот!')

        if ' насус' in msg:
            await message.channel.send('Книга, ты что-то напутала. Насус не бог, а рассадник блох!')

        if ' пайк' in msg:
            await message.channel.send('Ух ты! У тебя есть крючок! Ты точно умеешь ловить рыбу!')

        if ' ренгар' in msg:
            await message.channel.send('Слушай, Ренгар, как ты вылизываешь столько меха?')

        if ' твич' in msg:
            await message.channel.send('Крысы мерзкие. Ненавижу их!')

        if ' тимо' in msg:
            await message.channel.send('Тимо? Я его сцапаю! Точно сцапаю!')

        if ' кейтлин' in msg:
            await message.channel.send('Это ты – повелительница красной точки?')

        if ' джин' in msg:
            await message.channel.send('Джин, сыграешь мне колыбельную после боя?')

        if ' джинкс' in msg:
            await message.channel.send('А твоя Скелетница не была Рыбницей?')

        if ' люциан' in msg:
            await message.channel.send('Не волнуйся. Волшебные кошки сильнее призраков!')

        if ' мальфит' in msg:
            await message.channel.send('Фырк на тебя, куча камней! Фырк!')

        if ' нидали' in msg:
            await message.channel.send('Две кошки вышли погулять!')

        if ' райз' in msg:
            await message.channel.send('Книга, знакомься: гигантский свиток!')

        if ' шен' in msg:
            await message.channel.send('Мир духов, мы идём!')

        if ' сайлас' in msg:
            await message.channel.send('Ищи себе другую книгу!')



def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))
    print(f"> Extension {__name__} is ready")