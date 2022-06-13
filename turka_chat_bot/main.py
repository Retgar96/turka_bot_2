import telebot
from telebot import types
from order import order
import settings
import json_manager
import status_menu
import re


from data import аvailability as avai
bot = telebot.TeleBot(settings.bot_token)

type_cofe = avai.type_cofe
size_cofe = avai.size_cofe
syrop_cofe = avai.syrop_cofe
stat_menu = status_menu
second_time=[1,5,10]

ord = order()

@bot.message_handler(commands=['start'])
def start(message):

    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='Да', callback_data='Да')
    markup_inline.add(item_yes)
    bot.send_message(message.chat.id,
                     text=f"Привет, {message.from_user.first_name}! Добро пожаловать в TurkaBot\nХотите заказать кофе?",
                     reply_markup=markup_inline)
    print(ord.get_type())


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    menu = json_manager.read_json()

    if call.data == 'Да':
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
        menu_change_time(call)

    elif call.data == 'main_menu':
        menu_main(call)

    elif call.data == 'whithout_topping':
        ord.reload_time()
        ord.set_topping(call.data)
        menu_change_time(call)

    # Дописать регекс
    elif call.data == 'input_timer':
        menu_input_timer(call)



def menu_main(call):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='Да', callback_data='Да')
    markup_inline.add(item_yes)
    bot.send_message(call.message.chat.id,
                     text=f"Привет, {call.message.from_user.first_name}! Добро пожаловать в TurkaBot\nХотите заказать кофе?",
                     reply_markup=markup_inline)

def menu_input_timer(call):
    markup_inline = types.InlineKeyboardMarkup()

    back = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data='main_menu')
    markup_inline.add(back)
    try:
        bot.send_message(call.message.chat.id, text="\nВ данный момент функция в стадии разработки", reply_markup=markup_inline)
    except:
        bot.send_message(call.chat.id, text="\nВ данный момент функция в стадии разработки", reply_markup=markup_inline)

def menu_change_type_drinks(call):
    markup_inline = types.InlineKeyboardMarkup()
    menu = json_manager.read_json()

    for type in menu['drinks']:
        type = types.InlineKeyboardButton(text=type, callback_data=type)
        markup_inline.add(type)

    back = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data='main_menu')
    markup_inline.add(back)
    try:
        bot.send_message(call.message.chat.id, text="\nСегодня в нашем меню", reply_markup=markup_inline)
    except:
        bot.send_message(call.chat.id, text="\nСегодня в нашем меню", reply_markup=markup_inline)


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
        bot.send_message(call.message.chat.id, text="\nСегодня в нашем меню", reply_markup=markup_inline)
    except:
        bot.send_message(call.chat.id, text="\nСегодня в нашем меню", reply_markup=markup_inline)


def menu_change_size(call):
    markup_inline = types.InlineKeyboardMarkup()
    menu = json_manager.read_json()

    for type in menu['drinks'][ord.get_type_drink()][ord.get_type()]:
        type = types.InlineKeyboardButton(text=type, callback_data=type)
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
        type = types.InlineKeyboardButton(text=type, callback_data=type)
        markup_inline.add(type)

    net = types.InlineKeyboardButton(text="Нет", callback_data='whithout_topping')
    back = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data='main_menu')
    markup_inline.add(net,back)
    try:
        bot.send_message(call.message.chat.id, text=f"\nОтличный выбор!\nХотите ли добавить топпинг?)", reply_markup=markup_inline)
    except:
        bot.send_message(call.chat.id, text=f"\nОтличный выбор!\nХотите ли добавить топпинг?", reply_markup=markup_inline)



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



bot.enable_save_next_step_handlers(delay=2)
bot.polling(none_stop=True)