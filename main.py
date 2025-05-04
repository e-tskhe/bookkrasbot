import telebot
from dotenv import load_dotenv
import os
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InputMediaPhoto

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_team = KeyboardButton('Книжные люди')
    btn_places = KeyboardButton('Книжные места')
    btn_events = KeyboardButton('Книжные мероприятия')
    btn_libs = KeyboardButton('Библиотеки')

    markup.add(btn_team, btn_places, btn_events, btn_libs)

    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}.\n\n'
                                      f'Этот бот для тех, кто хочет провести выходные в Краснодаре с книгой. '
                                      f'Люди, мероприятия и книжные локации в Краснодаре — '
                                      f'библиотекари составили это для вас. ', reply_markup=markup)



@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == 'Книжные люди':
        markup = telebot.types.InlineKeyboardMarkup()
        btn_photo1 = telebot.types.InlineKeyboardButton(text='Книжная общага Натальи Бард', callback_data='nb')
        btn_photo2 = telebot.types.InlineKeyboardButton(text='Read. Sleep. Love', callback_data='rsl')
        btn_photo3 = telebot.types.InlineKeyboardButton(text='Кира пишет', callback_data='kira')
        btn_photo4 = telebot.types.InlineKeyboardButton(text='Виктория Ратгольц', callback_data='ratholz')
        btn_photo5 = telebot.types.InlineKeyboardButton(text='Фиги в книге', callback_data='figi')
        btn_photo6 = telebot.types.InlineKeyboardButton(text='Кота почитай', callback_data='kota_pochitay')
        btn_photo7 = telebot.types.InlineKeyboardButton(text='Литературное сообщество «Бродский»', callback_data='brodskiy')
        markup.add(btn_photo1)
        markup.add(btn_photo2)
        markup.add(btn_photo3)
        markup.add(btn_photo4)
        markup.add(btn_photo5)
        markup.add(btn_photo6)
        markup.add(btn_photo7)

        bot.send_message(message.chat.id, "Выбери книжного человека:", reply_markup=markup)

    elif message.text == 'Книжные места':
        markup = telebot.types.InlineKeyboardMarkup()
        btn_place1 = telebot.types.InlineKeyboardButton(text='Кафе «Издательство»', callback_data='izd')
        btn_place3 = telebot.types.InlineKeyboardButton(text='Книжная ПолЬка', callback_data='polka')
        btn_place4 = telebot.types.InlineKeyboardButton(text='Зацепи кофе', callback_data='zac_cofe')
        btn_place5 = telebot.types.InlineKeyboardButton(text='Независимый книжный "Чарли"', callback_data='charlie')
        btn_place6 = telebot.types.InlineKeyboardButton(text='Арт-резиденция «Дом книги»', callback_data='dom_knigi')
        btn_place7 = telebot.types.InlineKeyboardButton(text='Кафе «Бабушка-ракета»', callback_data='rocket')
        btn_place8 = telebot.types.InlineKeyboardButton(text='Книжный «Кот учёный»', callback_data='cot_uch')
        btn_place9 = telebot.types.InlineKeyboardButton(text='Домик культуры', callback_data='domik_kult')
        markup.add(btn_place1)
        markup.add(btn_place3)
        markup.add(btn_place4)
        markup.add(btn_place5)
        markup.add(btn_place6)
        markup.add(btn_place7)
        markup.add(btn_place8)
        markup.add(btn_place9)



        bot.send_message(message.chat.id, "Выбери книжное место:", reply_markup=markup)

    elif message.text == 'Книжные мероприятия':
        markup = telebot.types.InlineKeyboardMarkup()
        btn_event1 = telebot.types.InlineKeyboardButton(text='Книжный клуб «Кот учёный»', callback_data='cat_uch')
        btn_event2 = telebot.types.InlineKeyboardButton(text='Клуб для психологов', callback_data='psyclub')
        btn_event3 = telebot.types.InlineKeyboardButton(text='квесты «Кативквадрате»', callback_data='kativkvadtare')
        btn_event4 = telebot.types.InlineKeyboardButton(text='Vita Nouva', callback_data='vita_nouva')
        markup.add(btn_event1)
        markup.add(btn_event2)
        markup.add(btn_event3)
        markup.add(btn_event4)

        bot.send_message(message.chat.id, "Выбери мероприятие:", reply_markup=markup)
    elif message.text == 'Библиотеки':
        markup = telebot.types.InlineKeyboardMarkup()
        btn_lib1 = telebot.types.InlineKeyboardButton(text='Центральная библиотека имени Некрасова', callback_data='nekrasova')
        btn_lib3 = telebot.types.InlineKeyboardButton(text='Краснодарская краевая детская библиотека имени братьев Игнатовых',
                                                      callback_data='ignatovyh')
        btn_lib2 = telebot.types.InlineKeyboardButton(text='Краснодарская краевая универсальная научная библиотека имени А.С. Пушкина',
                                                      callback_data='pushkina')
        markup.add(btn_lib1)
        markup.add(btn_lib2)
        markup.add(btn_lib3)

        bot.send_message(message.chat.id, "Выбери библиотеку:", reply_markup=markup)



@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    try:
        #PEOPLE
        if call.data == 'nb':
            photo_nb = [
                InputMediaPhoto(open("img/nb1.jpg", "rb"),
                    caption="Книжная общага Натальи Бард\n\n"
                            "тгк: https://t.me/book_obshaga", parse_mode='html'),
                InputMediaPhoto(open("img/nb2.jpg", "rb")),
            ]
            bot.send_media_group(call.message.chat.id, photo_nb)
        elif call.data == 'rsl':
            photo_rsl = [
                InputMediaPhoto(open("img/rsl1.jpg", "rb"),
                    caption="Read. Sleep. Love\n\n"
                            "тгк: https://t.me/readsleeplove", parse_mode='html'),
                InputMediaPhoto(open("img/rsl2.jpg", "rb")),
            ]
            bot.send_media_group(call.message.chat.id, photo_rsl)
        elif call.data == 'kira':
            photo_kira = [
                InputMediaPhoto(open("img/kira1.jpg", "rb"),
                    caption="Кира пишет\n\n"
                            "тгк: https://t.me/kira_writes", parse_mode='html'),
                InputMediaPhoto(open("img/kira2.jpg", "rb")),
            ]
            bot.send_media_group(call.message.chat.id, photo_kira)
        elif call.data == 'ratholz':
            bot.send_photo(call.message.chat.id, open("img/ratholz.jpg", "rb"),
                           caption='<b>Виктория Ратгольц, писательница и ведущая подкаста "Почти у издателя".</b>\n\n'
                                   'Прожила 10 лет в Краснодаре и душой все еще там (а с помощью электричек порой и не '
                                   'только душой). Раньше вела писательские встречи и курс в Краснодаре, а сейчас пытается '
                                   'издать художественную книгу, где действие разворачивается в Южной столице.\n\n'
                                   'тгк: https://t.me/victoria_ratgolz', parse_mode='html')
        elif call.data == 'figi':
            photo_figi = [
                InputMediaPhoto(open("img/figi1.jpg", "rb"),
                    caption="Фиги в книге\n\n"
                            "💡Канал для любителей Книг\n💡а ещё здесь мелькает (пре)Краснодар\n💡и бывает о "
                            "кино/сериалах/подкастах, да и просто о хороших Историях\n\n"
                            "тгк: https://t.me/figivknige", parse_mode='html'),
                InputMediaPhoto(open("img/figi2.jpg", "rb")),
            ]
            bot.send_media_group(call.message.chat.id, photo_figi)
        elif call.data == 'kota_pochitay':
            photo_kota_pochitay = [
                InputMediaPhoto(open("img/kota_pochitay1.jpg", "rb"),
                    caption="<b>кота почитай 🐈‍⬛ книжный блог</b> — немножко блог немножко о книжках, который ведёт "
                            "библиотекариня Полина с цветными волосами\n\n"
                            "в её вкусе практически все, от триллеров до фэнтези, и отдельное место занимает литература "
                            "от женщин для женщин про женщин\n\n"
                            "И она ждёт вас в своей библиотеке! Краснодар, ул. Красная, 87/89\n\n"
                            "тгк: https://t.me/kotapochitay", parse_mode='html'),
                InputMediaPhoto(open("img/kota_pochitay2.jpg", "rb")),
            ]
            bot.send_media_group(call.message.chat.id, photo_kota_pochitay)
        elif call.data == 'brodskiy':
            bot.send_photo(call.message.chat.id, open("img/brodskiy.jpg", "rb"),
                           caption='<b>Литературное сообщество «Бродский»</b>\n\n'
                                   'Книжный клуб, который вышел за рамки клуба и стал амбассадором книжных Сочи и Краснодара. '
                                   'Собирают вокруг себя гурманов и организовывают благотворительные распродажи.\n\n'
                                   'тгк: https://t.me/brodskiy_tvoibro', parse_mode='html')
        #PLACES
        elif call.data == 'polka':
            photo_polka = [
                InputMediaPhoto(open("img/polka1.jpg", "rb"),
                    caption="<b>Книжная ПолЬка</b>\n\n"
                            "Магазин для любителей книг, где их можно приобрести по приятным "
                            "ценам напрямую от издательств. милые стикеры, уютные гирлянды, вкусные свечки "
                            "и возможность заказать любую книгу — всё ждет вас здесь\n\n"
                            "<b>Адрес:</b> ул. Восточно-Кругликовская 48/1\n"
                            "<b>Сайт:</b> http://bookskrd.ru/\n"
                            "<b>Чат закупки в тг:</> https://t.me/+qe15T7UXxu00ZDRi", parse_mode='html'),
                InputMediaPhoto(open("img/polka2.jpg", "rb")),
            ]
            bot.send_media_group(call.message.chat.id, photo_polka)
        elif call.data == 'zac_cofe':
            photo_zac_cofe = [
                InputMediaPhoto(open("img/zac_cofe1.jpg", "rb"),
                    caption="<b>Кофейня «Зацепи кофе»</b>\n\n"
                        "Вас встретят кофе, книги и настольные игры. "
                        "Небольшая беседка с мягкими креслами и пледами под вечер. "
                        "Уютно, чтобы посидеть книжным клубом и выпить авторские чаи\n\n"
                        "<b>Адрес:</b> ул. имени 40-летия Победы, 146\n"
                        "<b>Режим работы:</b> ежедневно, 8:00-23:00\n", parse_mode='html'),
                InputMediaPhoto(open("img/zac_cofe2.jpg", "rb")),
            ]
            bot.send_media_group(call.message.chat.id, photo_zac_cofe)
        elif call.data == 'charlie':
            photo_charlie = [
                InputMediaPhoto(open("img/charlie1.jpg", "rb"),
                    caption="<b>Независимый книжный «Чарли»</b>\n\n"
                        "Вы найдете локальную культуру Краснодара в редких книгах, "
                        "открытках и постерах. очень много "
                        "книг и журналов про искусство разного рода: фото, издательства, кино... "
                        "и вообще много от независимых издательств, от детских книг до нонфикшна\n\n"
                        "<b>Адрес:</b> Красноармейская, 68\nдвор со шлагбаумом\nлевая сторона, белая дверь\nвторой "
                            "этаж, "
                            "<a href='https://t.me/charlie_krd/2658'>как пройти?</a>\n"
                        "<b>Режим работы:</b> ежедневно, 11:00-20:00\n\n"
                        "<b>тгк:</b> https://t.me/charlie_krd\n"
                        "<b>почта для сотрудничества:</b> charliebooks.krd@gmail.com", parse_mode='html'),
                InputMediaPhoto(open("img/charlie2.jpg", "rb")),
            ]
            bot.send_media_group(call.message.chat.id, photo_charlie)
        elif call.data == 'dom_knigi':
            photo_dom_knigi = [
                InputMediaPhoto(open("img/dom_knigi1.jpg", "rb"),
                    caption="<b>Арт-резиденция «Дом книги»</b>\n\n"
                        "Книжные фестивали, лекции, читки и другое творчество. "
                        "Все события и выставки бесплатные. Что-то интересное происходит каждый день. "
                        "В Доме есть небольшая библиотека, и в кресле вы можете посидеть почитать.\n\n"
                        "<b>Адрес:</b> ул. Красная 43 (центральный вход)\n"
                        "<b>Режим работы:</b> \nбудни: 9:00-19:30\nсб-вс: 10:00-19:30\n\n"
                        "<b>тгк резиденции:</b> https://t.me/domknigiart\n"
                        "<b>основной канал:</b> https://t.me/mcrl_kuban", parse_mode='html'),
                InputMediaPhoto(open("img/dom_knigi2.jpg", "rb")),
            ]
            bot.send_media_group(call.message.chat.id, photo_dom_knigi)
        elif call.data == 'rocket':
                    photo_rocket = [
                        InputMediaPhoto(open("img/rocket1.jpg", "rb"),
                            caption="<b>Кафе «Бабушка-ракета»</b>\n\n"
                                "Кафе книжный, где ваш ребёнок может посмотреть спектакль, пока вы слушаете винил с "
                                "кофе в руках. Проходят сенсорные игры и интерактивные занятия, которые помогают развивать "
                                "гибкость ума и моторные навыки.\n\n"
                                "<u>В понедельник скидка на книги 20%, а 6 книга в подарок!</u>\n\n"
                                "<b>Адрес:</b> ул. Коммунаров, 58Г\n"
                                "<b>Режим работы:</b> ежедневно, 10:00-20:00\n\n"
                                "<b>тгк:</b> https://t.me/babushka_raketa\n", parse_mode='html'),
                        InputMediaPhoto(open("img/rocket2.jpg", "rb")),
                    ]
                    bot.send_media_group(call.message.chat.id, photo_rocket)
        elif call.data == 'cot_uch':
            photo_cot_uch = [
                InputMediaPhoto(open("img/cot_uch1.jpg", "rb"),
                    caption="<b>Книжный «Кот учёный»</b>\n\n"
                        "Книжный в Чистяковской Роще на книжном рынке. Огромный ассортимент книг различных "
                        "жанров от классики до детских. Можно сделать персональный заказ, купить сертификат.  "
                        "Вас встретит ухоженный ласковый кот, который всегда рад посетителям.\n\n"
                        "<b>Адрес:</b>\n г. Краснодар, ул. 40-летия Победы 11, ст.13,\n"
                        "Книжный рынок, павильоны 150А-Б, 133-134.\n"
                        "<b>Режим работы:</b> \nБез выходных с 10:00 до 19:00\n\n"
                        "<b>сайт:</b> https://catme.shop/\n", parse_mode='html'),
                InputMediaPhoto(open("img/cot_uch2.jpg", "rb")),
            ]
            bot.send_media_group(call.message.chat.id, photo_cot_uch)
        elif call.data == 'domik_kult':
            photo_domik_kult = [
                InputMediaPhoto(open("img/domik_kult1.jpg", "rb"),
                    caption="<b>Домик культуры </b>\n\n"
                        "где вы можете купить открытки с Краснодаром и вложить в свою любимую книгу, "
                        "да ещё и вкусно пахнущие свечи\n\n"
                        "<b>Адрес:</b> ул. Коммунаров, 136\n"
                        "<b>Режим работы:</b> вт-вс, 11:00-20:00\n\n"
                        "<b>тгк художницы:</b> https://t.me/Jony_Sketching\n"
                        "<b>тгк магазина:</b> https://t.me/sofiya_baychibaeva\n", parse_mode='html'),
                InputMediaPhoto(open("img/domik_kult2.jpg", "rb")),
            ]
            bot.send_media_group(call.message.chat.id, photo_domik_kult)
        elif call.data == 'event1':
            photo_izd = [
                InputMediaPhoto(open("img/izd1.jpg", "rb"),
                    caption="<b>Кафе «Издательство»</b>\n\n"
                        "Книги, шахматы, настольные игры и латте «Вишнёвый сад». "
                        "Кстати, чек вам могут подать в томике книги.\n\n"
                        "<b>Адрес:</b> ул. Зиповская, 38/ ул. Ставропольская, 226\n"
                        "<b>Режим работы:</b> \nбудни: 8:00-23:00\nсб-вс: 9:00-23:00\n\n", parse_mode='html'),
                InputMediaPhoto(open("img/izd2.jpg", "rb")),
            ]
            bot.send_media_group(call.message.chat.id, photo_izd)

        #EVENTS
        elif call.data == 'cat_uch':
            photo_izd = [
                InputMediaPhoto(open("img/cat_uch1.jpg", "rb"),
                                caption="<b>Книжный клуб «Кот учёный»</b>\n"
                                        "🐈‍⬛Мы только по любви\n\n"
                                        "☕️Встречаются раз в месяц в уютном заведении города и обсуждают заранее "
                                        "выбранные книги\n"
                                        "💁🏼‍♀️Организатор: @dara_yara\n\n"
                                        "тгк: https://t.me/kot_uchenyi7",
                                parse_mode='html'),
                InputMediaPhoto(open("img/cat_uch2.jpg", "rb")),
            ]
            bot.send_media_group(call.message.chat.id, photo_izd)
        elif call.data == 'vita_nouva':
            photo_vita_nouva = [
                InputMediaPhoto(open("img/vita_nouva1.jpg", "rb"),
                                caption="<b>Vita Nouva</b>\n"
                                        "Новые знания — новая жизнь!\nСеминары, культурные мероприятия\n"
                                        "Для любителей литературы и не только\nИзучай афишу и регистрируйся \n\n"
                                        "тгк: https://t.me/vita_nuova",
                                parse_mode='html'),
                InputMediaPhoto(open("img/vita_nouva2.jpg", "rb")),
            ]
            bot.send_media_group(call.message.chat.id, photo_vita_nouva)
        elif call.data == 'psyclub':
            photo_psyclub = [
                InputMediaPhoto(open("img/psyclub1.jpg", "rb"),
                                caption="<b>Клуб для психологов</b>\n\n"
                                        "где-то психологи читают специализированную литературу\n\n"
                                        "тгк: https://t.me/olgarusspsy",
                                parse_mode='html'),
                InputMediaPhoto(open("img/psyclub2.jpg", "rb")),
            ]
            bot.send_media_group(call.message.chat.id, photo_psyclub)
        elif call.data == 'kativkvadtare':
            bot.send_photo(call.message.chat.id, open("img/kativkvadtare.jpg", "rb"),
                           caption='<b>квесты «Кативквадрате»</b>\n\n'
                                   'Проводят квесты для детей по мотивам литературных произведений\n\n '
                                   'тгк: https://t.me/katy_v_kvadrate', parse_mode='html')

        #LIBS
        elif call.data == 'nekrasova':
            bot.send_photo(call.message.chat.id, open("img/nekrasova.jpg", "rb"),
                           caption='<b>Центральная библиотека имени Некрасова</b>\n\n'
                                   'Это не просто библиотека, это место где происходит очень много интересных вещей и событий. '
                                   'Библионочь, киноночь, разного рода мероприятия и книжные клубы. '
                                   'Также это одно из немногих мест откуда можно получить доступ к президентской '
                                   'библиотеке.\n\n<b>Адрес:</b> ул. Красная, 87\n\n'
                                   '<b>сайт:</b> https://neklib.kubannet.ru/', parse_mode='html')
        elif call.data == 'ignatovyh':
            bot.send_photo(call.message.chat.id, open("img/ignatovyh.jpg", "rb"),
                           caption='<b>Краснодарская краевая детская библиотека имени братьев Игнатовых</b>\n\n'
                                   'Крупная, с множеством отделов и залов библиотека для детей.  Много мастер-классов, '
                                   'к примеру, по знакомству и изготовлению диафильма.\n\n'
                                   '<b>Адрес:</b>  ул. Красная, 26/1\n'
                                   '<b>сайт:</b> https://www.ignatovka.ru/', parse_mode='html')
        elif call.data == 'pushkina':
            photo_pushkina = [
                InputMediaPhoto(open("img/pushkina1.jpg", "rb"),
                    caption="<b>Краснодарская краевая универсальная научная библиотека имени А.С. Пушкина</b>\n\n"
                        "Библиотека с обширным книжным фондом, в том числе в электронном виде. При наличии читательского "
                        "билета можно бесплатно зарегистрироваться на ЛитРес и брать в удобном формате "
                        "электронные книги из фонда. Архивные фото, газеты, пластинки, помощь в подборе "
                        "литературы для научных и студенческих работ и богатый научный фонд.\n"
                        "Сюда стекаются все издания края в обязательном экземпляре.\n\n"
                        "<b>Адрес:</b> ул. Красная, 8\n"
                        "<b>Сайт:</b> http://pushkin.kubannet.ru/\n"
                        "<b>тгк:</b> https://t.me/pushkinka_krd", parse_mode='html'),
                InputMediaPhoto(open("img/pushkina2.jpg", "rb")),
            ]
            bot.send_media_group(call.message.chat.id, photo_pushkina)

        bot.answer_callback_query(call.id)
    except Exception as e:
        print(f"Error: {e}")
        bot.send_message(call.message.chat.id, "Произошла ошибка при загрузке фото")


if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=os.getenv('WEBHOOK_URL') + '/webhook')
