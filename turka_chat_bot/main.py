import telebot
from telebot import types
from order import order
import settings
import json_manager
import status_menu
import re
import admin_actions

from data import аvailability as avai
bot = telebot.TeleBot(settings.bot_token)

type_cofe = avai.type_cofe
size_cofe = avai.size_cofe
syrop_cofe = avai.syrop_cofe
stat_menu = status_menu
second_time=[1,5,10]
ord = order()
admin = admin_actions.admin_actions()

@bot.message_handler(commands=['start'])
def start(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='Да', callback_data='standart_user')
    markup_inline.add(item_yes)
    bot.send_message(message.chat.id,
                     text=f"Привет, {message.from_user.first_name}! TurkaBot готов вас обслужить\nХотите заказать кофе?",
                     reply_markup=markup_inline)


@bot.message_handler(commands=['start_admin'])
def start_admin(message):

    if f'{message.from_user.id}' in settings.ADMIN_ID:
        markup_inline = types.InlineKeyboardMarkup()
        item_yes = types.InlineKeyboardButton(text='Удалить чат бота?', callback_data=f'{settings.ADMIN_KEY}')
        markup_inline.add(item_yes)
        bot.send_message(message.chat.id,
                         text=f"Привет, {message.from_user.first_name}! Вы админ и можете управлять здесь всем)",
                         reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda x: True)
def callback_inline(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    menu = json_manager.read_json()


    if call.data == f'standart_user':
        menu_change_type_drinks(call)

    elif call.data == '+1 час':
        ord.plus_1_hour()
        menu_change_time(call)

    elif call.data == '+30 минут':
        ord.plus_30_min()
        menu_change_time(call)

    elif call.data == '+5 минут':
        ord.plus_5_min()
        menu_change_time(call)

    elif call.data == '+1 минуту':
        ord.plus_1_min()
        menu_change_time(call)

    elif call.data == 'Подтвердить заказ':
        bot.send_message(call.message.chat.id, text=f"\nВаш заказ:\n {ord.get_full_order()}")
        menu_main(call)

    elif call.data == 'Сброс':
        ord.reload_time()
        menu_change_time(call)

    elif call.data in menu['drinks']:
        ord.set_type_drink(call.data)
        menu_change_type(call)

    elif call.data in menu['drinks'][ord.get_type_drink()]:
        ord.set_type(call.data)
        menu_change_size(call)

    elif call.data in menu['drinks'][ord.get_type_drink()][ord.get_type()]:
        ord.set_size(call.data)
        menu_change_syrop(call)

    elif call.data in menu['topping']:
        ord.reload_time()
        ord.set_topping(call.data)
        menu_change_milk(call)

    elif call.data in menu['milk']:
        ord.set_milk(call.data)
        menu_change_time(call)

    elif call.data == 'main_menu':
        menu_main(call)

    elif call.data == 'whithout_topping':
        ord.reload_time()
        ord.set_topping(call.data)
        menu_change_time(call)

    elif call.data == 'input_timer':
        menu_input_timer(call)



    # Admin menu main
    elif call.data == f'{settings.ADMIN_KEY}':
        admin_menu(call)

    # elif call.data in f'{settings.ADMIN_KEY}change_menu':
    #     admin_menu_action_change(call)
    #
    #
    # # Admin menu type actions
    # elif call.data in f'{settings.ADMIN_KEY}add':
    #     admin_menu_add(call)
    #
    # elif call.data in f'{settings.ADMIN_KEY}del':
    #     admin_menu_del(call)
    #
    # elif call.data in f'{settings.ADMIN_KEY}change':
    #     admin_menu_change(call)
    #
    #
    # # Admin menu type product actions
    #
    #
    # # delete products
    # elif call.data == f'{settings.ADMIN_KEY}del_drinks':
    #     admin_del_drink(call)
    #
    # elif call.data == f'{settings.ADMIN_KEY}del_topping':
    #     admin_del_topping(call)
    #
    # elif call.data == f'{settings.ADMIN_KEY}del_milk':
    #     admin_del_milk(call)
    #
    #
    # # Add products
    # elif call.data == f'{settings.ADMIN_KEY}add_drinks':
    #     admin_add_drink(call)
    #
    # elif call.data == f'{settings.ADMIN_KEY}add_topping':
    #     admin_add_topping(call)
    #
    # elif call.data == f'{settings.ADMIN_KEY}add_milk':
    #     admin_add_milk(call)
    #
    #
    # # Change products
    #
    #
    # elif call.data == f'{settings.ADMIN_KEY}change_drinks':
    #     admin_change_drink(call)
    #
    # elif call.data == f'{settings.ADMIN_KEY}change{menu["drinks"]}':
    #     admin.type_category = call.data
    #     admin_type_product(call)
    #
    # elif call.data == f'{settings.ADMIN_KEY}change{menu_change_type_drinks()}':
    #     admin.type_category = call.data
    #
    #
    # elif call.data == f'{settings.ADMIN_KEY}change_topping':
    #     admin_change_topping(call)
    #
    # elif call.data == f'{settings.ADMIN_KEY}change_milk':
    #     admin_change_milk(call)






@bot.message_handler(content_types=['text'])
def hand_timer(message):

    if re.findall(settings.PATTERN_TIMER, message.text):
        ord.set_time(message.text)
        bot.send_message(message.chat.id, text=f"\nВаш заказ:\n {ord.get_full_order_hand_input()}")
        menu_main(message)

    else:
        bot.send_message(message.chat.id,
                         text=f"Попробуйте ещё раз или напишите команду /start для того что бы начать сначала")



def admin_drink(call):
    markup_inline = types.InlineKeyboardMarkup()
    menu = json_manager.read_json()

    for type in menu['drinks']:
        type = types.InlineKeyboardButton(text=type, callback_data=type)
        markup_inline.add(type)

    back = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data='main_menu')
    markup_inline.add(back)
    try:
        bot.send_message(call.message.chat.id, text="\nВыбирите тип напитка", reply_markup=markup_inline)
    except:
        bot.send_message(call.chat.id, text="\nВыбирите тип напитка", reply_markup=markup_inline)



def admin_topping(call):
    markup_inline = types.InlineKeyboardMarkup()
    menu = json_manager.read_json()

    for type in menu['topping']:
        type = types.InlineKeyboardButton(text=f"{type} \n"
                                               f"price: {menu['topping'][f'{type}']['price']}р",
                                          callback_data=type)
        markup_inline.add(type)

    net = types.InlineKeyboardButton(text="Нет", callback_data='whithout_topping')
    back = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data='main_menu')
    markup_inline.add(net, back)
    try:
        bot.send_message(call.message.chat.id, text=f"\nОтличный выбор!\nХотите ли добавить топпинг?)",
                         reply_markup=markup_inline)
    except:
        bot.send_message(call.chat.id, text=f"\nОтличный выбор!\nХотите ли добавить топпинг?",
                         reply_markup=markup_inline)

def admin_milk(call):
    markup_inline = types.InlineKeyboardMarkup()
    menu = json_manager.read_json()

    for type in menu['milk']:
        type = types.InlineKeyboardButton(text=f"{type} \n"
                                               f"price: {menu['milk'][f'{type}']['price']}р",
                                          callback_data=type)
        markup_inline.add(type)

    # net = types.InlineKeyboardButton(text="Нет", callback_data='whithout_topping')
    back = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data='main_menu')
    markup_inline.add(back)
    try:
        bot.send_message(call.message.chat.id, text=f"\nВыбирите молоко: ",
                         reply_markup=markup_inline)
    except:
        bot.send_message(call.chat.id, text=f"\nВыбирите молоко: ", reply_markup=markup_inline)


def admin_menu(call):
    markup_inline = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(text="admins", callback_data=f'{settings.ADMIN_KEY}admins')
    btn2 = types.InlineKeyboardButton(text="settings", callback_data=f'{settings.ADMIN_KEY}settings')
    btn3 = types.InlineKeyboardButton(text="add_admin", callback_data=f'{settings.ADMIN_KEY}add_admin')
    btn4 = types.InlineKeyboardButton(text="change menu", callback_data=f'{settings.ADMIN_KEY}change_menu')

    markup_inline.add(btn1, btn2, btn3, btn4)

    try:
        bot.send_message(call.message.chat.id, text=f"\nЧто бы вы хотели сделать?",
                         reply_markup=markup_inline)
    except:
        bot.send_message(call.chat.id, text=f"\nЧто бы вы хотели сделать?", reply_markup=markup_inline)

def admin_menu_action(call):
    markup_inline = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(text="Добавить", callback_data=f'{settings.ADMIN_KEY}add')
    btn2 = types.InlineKeyboardButton(text="Удалить", callback_data=f'{settings.ADMIN_KEY}del')
    btn3 = types.InlineKeyboardButton(text="Изменить", callback_data=f'{settings.ADMIN_KEY}change')

    markup_inline.add(btn1, btn2, btn3)

    try:
        bot.send_message(call.message.chat.id, text=f"\nЧто бы вы хотели сделать?",
                         reply_markup=markup_inline)
    except:
        bot.send_message(call.chat.id, text=f"\nЧто бы вы хотели сделать?", reply_markup=markup_inline)


def admin_menu_type(call):
    markup_inline = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(text="Напитков", callback_data=f'{settings.ADMIN_KEY}drinks1')
    btn2 = types.InlineKeyboardButton(text="Сиропов", callback_data=f'{settings.ADMIN_KEY}topping')
    btn3 = types.InlineKeyboardButton(text="Молока", callback_data= f'{settings.ADMIN_KEY}milk')

    markup_inline.add(btn1, btn2, btn3)
    try:
        bot.send_message(call.message.chat.id, text=f"\nНастройки:",
                         reply_markup=markup_inline)
    except:
        bot.send_message(call.chat.id, text=f"\nНастройки:", reply_markup=markup_inline)

def admin_menu_type_drinks(call):
    markup_inline = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(text="Напитков", callback_data=f'{settings.ADMIN_KEY}drinks1')
    btn2 = types.InlineKeyboardButton(text="Сиропов", callback_data=f'{settings.ADMIN_KEY}topping')
    btn3 = types.InlineKeyboardButton(text="Молока", callback_data= f'{settings.ADMIN_KEY}milk')

    markup_inline.add(btn1, btn2, btn3)
    try:
        bot.send_message(call.message.chat.id, text=f"\nНастройки:",
                         reply_markup=markup_inline)
    except:
        bot.send_message(call.chat.id, text=f"\nНастройки:", reply_markup=markup_inline)

def admin_menu_type_topping(call):
    markup_inline = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(text="Напитков", callback_data=f'{settings.ADMIN_KEY}drinks1')
    btn2 = types.InlineKeyboardButton(text="Сиропов", callback_data=f'{settings.ADMIN_KEY}topping')
    btn3 = types.InlineKeyboardButton(text="Молока", callback_data= f'{settings.ADMIN_KEY}milk')

    markup_inline.add(btn1, btn2, btn3)
    try:
        bot.send_message(call.message.chat.id, text=f"\nНастройки:",
                         reply_markup=markup_inline)
    except:
        bot.send_message(call.chat.id, text=f"\nНастройки:", reply_markup=markup_inline)


def admin_menu_type_milk(call):
    markup_inline = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(text="Напитков", callback_data=f'{settings.ADMIN_KEY}drinks1')
    btn2 = types.InlineKeyboardButton(text="Сиропов", callback_data=f'{settings.ADMIN_KEY}topping')
    btn3 = types.InlineKeyboardButton(text="Молока", callback_data= f'{settings.ADMIN_KEY}milk')

    markup_inline.add(btn1, btn2, btn3)
    try:
        bot.send_message(call.message.chat.id, text=f"\nНастройки:",
                         reply_markup=markup_inline)
    except:
        bot.send_message(call.chat.id, text=f"\nНастройки:", reply_markup=markup_inline)

def menu_main(call):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='Да', callback_data='standart_user')
    markup_inline.add(item_yes)
    try:
        bot.send_message(call.message.chat.id,
                         text=f"{call.from_user.first_name}, может быть ещё кофе?",
                         reply_markup=markup_inline)
    except:
        bot.send_message(call.chat.id,
                         text=f"{call.from_user.first_name}, может быть ещё кофе?",
                         reply_markup=markup_inline)



def menu_input_timer(call):
    markup_inline = types.InlineKeyboardMarkup()

    back = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data='main_menu')
    markup_inline.add(back)
    try:
        msg = bot.send_message(call.message.chat.id, text="\nВведите время в формате ЧЧ:ММ", reply_markup=markup_inline)
    except:
        msg = bot.send_message(call.chat.id, text="\nВ данный момент функция в стадии разработки", reply_markup=markup_inline)
    bot.register_next_step_handler(msg,hand_timer)

def menu_change_type_drinks(call):
    markup_inline = types.InlineKeyboardMarkup()
    menu = json_manager.read_json()

    for type in menu['drinks']:
        type = types.InlineKeyboardButton(text=type, callback_data=type)
        markup_inline.add(type)

    back = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data='main_menu')
    markup_inline.add(back)
    try:
        bot.send_message(call.message.chat.id, text="\nСделайте1 ваш выбор", reply_markup=markup_inline)
    except:
        bot.send_message(call.chat.id, text="\nСделайте1 ваш выбор", reply_markup=markup_inline)


def menu_change_type(call):
    markup_inline = types.InlineKeyboardMarkup()
    menu = json_manager.read_json()
    items = ord.get_type_drink()
    for type in menu['drinks'][items]:

        type = types.InlineKeyboardButton(text=type, callback_data=type)
        markup_inline.add(type)

    back = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data='main_menu')
    markup_inline.add(back)
    try:
        bot.send_message(call.message.chat.id, text="\nСделайте ваш выбор", reply_markup=markup_inline)
    except:
        bot.send_message(call.chat.id, text="\nССделайте ваш выбор", reply_markup=markup_inline)


def menu_change_size(call):
    markup_inline = types.InlineKeyboardMarkup()
    menu = json_manager.read_json()

    for type in menu['drinks'][ord.get_type_drink()][ord.get_type()]:
        type = types.InlineKeyboardButton(text=f"{type} \n"
                                                    f"ml: {menu['drinks'][ord.get_type_drink()][ord.get_type()][f'{type}']['ml']}\n"  
                                                    f"price: {menu['drinks'][ord.get_type_drink()][ord.get_type()][f'{type}']['price']}р", callback_data=type)
        markup_inline.add(type)

    back = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data='main_menu')
    markup_inline.add(back)
    try:
        bot.send_message(call.message.chat.id, text=f"\nОтличный выбор!\nВыберите размер",
                               reply_markup=markup_inline)
    except:
        bot.send_message(call.chat.id, text=f"\nОтличный выбор!\nВыберите размер",
                               reply_markup=markup_inline)


def menu_change_syrop(call):
    markup_inline = types.InlineKeyboardMarkup()
    menu = json_manager.read_json()

    for type in menu['topping']:
        type = types.InlineKeyboardButton(text=f"{type} \n"
                                               f"price: {menu['topping'][f'{type}']['price']}р",
                                          callback_data=type)
        markup_inline.add(type)

    net = types.InlineKeyboardButton(text="Нет", callback_data='whithout_topping')
    back = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data='main_menu')
    markup_inline.add(net,back)
    try:
        bot.send_message(call.message.chat.id, text=f"\nОтличный выбор!\nХотите ли добавить топпинг?)", reply_markup=markup_inline)
    except:
        bot.send_message(call.chat.id, text=f"\nОтличный выбор!\nХотите ли добавить топпинг?", reply_markup=markup_inline)


def menu_change_milk(call):
    markup_inline = types.InlineKeyboardMarkup()
    menu = json_manager.read_json()

    for type in menu['milk']:
        type = types.InlineKeyboardButton(text=f"{type} \n"
                                               f"price: {menu['milk'][f'{type}']['price']}р",
                                          callback_data=type)
        markup_inline.add(type)

    # net = types.InlineKeyboardButton(text="Нет", callback_data='whithout_topping')
    back = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data='main_menu')
    markup_inline.add(back)
    try:
        bot.send_message(call.message.chat.id, text=f"\nНа каком молоке вы хотели бы ваш кофе?", reply_markup=markup_inline)
    except:
        bot.send_message(call.chat.id, text=f"\nНа каком молоке вы хотели бы ваш кофе?", reply_markup=markup_inline)


def menu_change_time(call):
    markup_inline = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(text="+1 час", callback_data='+1 час')
    btn2 = types.InlineKeyboardButton(text="+30 минут", callback_data='+30 минут')
    btn3 = types.InlineKeyboardButton(text="+5 минут", callback_data='+5 минут')
    btn5 = types.InlineKeyboardButton(text="+1 минуту", callback_data = '+1 минуту')
    btn4 = types.InlineKeyboardButton(text="Сброс", callback_data='Сброс')
    back = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data='main_menu')
    btn6 = types.InlineKeyboardButton(text="Подтвердить заказ", callback_data='Подтвердить заказ')
    btn7 = types.InlineKeyboardButton(text="Ввести вручную в формате 'ЧЧ:ММ'", callback_data='input_timer')
    markup_inline.add(btn1, btn2, btn3,btn4,btn5,btn6, btn7, back)
    hrs = ord.get_filing_hours()
    min = ord.get_filing_min()

    if hrs == 24:
        hrs = '00'
    elif hrs in [1,2,3,4,5,6,7,8,9,0]:
        hrs = '0'+str(hrs)
    if min in [1,2,3,4,5,6,7,8,9,0]:
        min = '0'+str(min)

    try:
        bot.send_message(call.message.chat.id, text=f"\nВремя подачи вашего кофе: {hrs}:{min}", reply_markup=markup_inline)
    except:
        bot.send_message(call.chat.id, text=f"\nВремя подачи вашего кофе:{hrs}:{min}", reply_markup=markup_inline)



def final_order():
    pass


bot.enable_save_next_step_handlers(delay=2)
bot.polling(none_stop=True)