# import telebot
# from telebot import types
# import settings
# import time
# import json_manager
#
# bot = telebot.TeleBot(settings.bot_token)
#
#
#
# @bot.message_handler(content_types=['text'])
# def start(message):
#     if message.text == '/reg':
#         bot.send_message(message.from_user.id, "Как тебя зовут?");
#         bot.register_next_step_handler(message, menu_change_type);  # следующий шаг – функция get_name
#     else:
#         bot.send_message(message.from_user.id, 'Напиши /reg')
#
# def menu_change_type(message):
#     markup_inline = types.InlineKeyboardMarkup()
#
#     for type in json_manager.read_json():
#         type = types.InlineKeyboardButton(text=type, callback_data=type)
#         markup_inline.add(type)
#
#     bot.send_message(message.chat.id, text="\neeeeee", reply_markup=markup_inline)
#
#     # try:
#     #     bot.send_message(message.chat.id, text="\nСегодня в нашем меню", reply_markup=markup_inline)
#     # except:
#     #     bot.send_message(message.chat.id, text="\nСегодня в нашем меню", reply_markup=markup_inline)
#
#     if message.text == 'drinks':
#         bot.send_message(message.chat.id, text="\nyyyyyyeeeeee", reply_markup=markup_inline)
#         bot.register_next_step_handler(message, menu_main)
#
#
#
#
#
#
#
# def menu_main(message):
#         markup_inline = types.InlineKeyboardMarkup()
#         item_yes = types.InlineKeyboardButton(text='Да', callback_data='Да')
#         markup_inline.add(item_yes)
#         bot.send_message(message.chat.id,
#                          text=f"Привет, {message.from_user.first_name}! Добро пожаловать в TurkaBot\nХотите заказать кофе?",
#                          reply_markup=markup_inline)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# def menu_change_size(self, call):
#         markup_inline = types.InlineKeyboardMarkup()
#
#         btn1 = types.InlineKeyboardButton(text="Большой - 300ml", callback_data='big')
#         btn2 = types.InlineKeyboardButton(text="Средний - 200ml", callback_data='midle')
#         btn3 = types.InlineKeyboardButton(text="Маленький - 100ml", callback_data='small')
#         back = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data='main_menu')
#
#         markup_inline.add(btn1, btn2, btn3, back)
#         try:
#             msg = self.bot.send_message(call.message.chat.id, text=f"\nОтличный выбор!\nВыберите сироп",
#                                    reply_markup=markup_inline)
#         except:
#             msg = self.bot.send_message(call.chat.id, text=f"\nОтличный выбор!\nВыберите сироп",
#                                    reply_markup=markup_inline)
#
#
# def menu_change_syrop(self, call):
#         # bot.delete_message(call.message.chat.id, call.message.message_id)
#         markup_inline = types.InlineKeyboardMarkup()
#
#         btn1 = types.InlineKeyboardButton(text="Апельсиновым", callback_data='Апельсиновым')
#         btn2 = types.InlineKeyboardButton(text="Шоколадным", callback_data='Шоколадным')
#         btn3 = types.InlineKeyboardButton(text="Ванильным", callback_data='Ванильным')
#         btn4 = types.InlineKeyboardButton(text="Без сиропа", callback_data='Без сиропа')
#         back = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data='main_menu')
#
#         markup_inline.add(btn1, btn2, btn3, btn4, back)
#         try:
#             msg = self.bot.send_message(call.message.chat.id, text=f"\nОтличный выбор!\nХе хе хе)",
#                                    reply_markup=markup_inline)
#         except:
#             msg = self.bot.send_message(call.chat.id, text=f"\nОтличный выбор!\nВыберите Хе хе хе",
#                                    reply_markup=markup_inline)
#
#
# def menu_change_time(self, call, time_counter=time.localtime(time.time())):
#         # bot.delete_message(call.message.chat.id, call.message.message_id)
#         markup_inline = types.InlineKeyboardMarkup()
#
#         btn1 = types.InlineKeyboardButton(text="+1 час", callback_data='+1 час')
#         btn2 = types.InlineKeyboardButton(text="+30 минут", callback_data='+30 минут')
#         btn3 = types.InlineKeyboardButton(text="+5 минут", callback_data='+5 минут')
#         btn5 = types.InlineKeyboardButton(text="+1 минуту", callback_data='+1 минуту')
#         btn4 = types.InlineKeyboardButton(text="Сброс", callback_data='Сброс')
#         back = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data='main_menu')
#         btn6 = types.InlineKeyboardButton(text="Подтвердить заказ", callback_data='Подтвердить заказ')
#         markup_inline.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
#         hrs = ord.get_filing_hours()
#         min = ord.get_filing_min()
#
#         if hrs == 24:
#             hrs = '00'
#         elif hrs in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
#             hrs = '0' + str(hrs)
#         if min in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
#             min = '0' + str(min)
#
#         try:
#             msg = self.bot.send_message(call.message.chat.id, text=f"\nВремя подачи вашего кофе: {hrs}:{min}",
#                                    reply_markup=markup_inline)
#         except:
#             msg = self.bot.send_message(call.chat.id, text=f"\nВремя подачи вашего кофе:{hrs}:{min}",
#                                    reply_markup=markup_inline)
#
#
#
#
# class menu_type:
#
#
#     @bot.callback_query_handler(func=lambda call: True)
#     def callback_inline(self, call):
#         self.bot.delete_message(call.message.chat.id, call.message.message_id)
#
#         if call.data == 'Да':
#             self.menu_change_type(call)
#
#         elif call.data == '+1 час':
#             ord.plus_1_hour()
#             self.menu_change_time(call)
#
#         elif call.data == '+30 минут':
#             ord.plus_30_min()
#             self.menu_change_time(call)
#
#         elif call.data == '+5 минут':
#             ord.plus_5_min()
#             self.menu_change_time(call)
#
#         elif call.data == '+1 минуту':
#             ord.plus_1_min()
#             self.menu_change_time(call)
#
#         elif call.data == 'Подтвердить заказ':
#             self.bot.send_message(call.message.chat.id, text=f"\nВаш заказ:\n {ord.get_full_order()}")
#             self.menu_main(call)
#
#         elif call.data == 'Сброс':
#             ord.reload_time()
#             self.menu_change_time(call)
#
#         elif call.data in self.type_cofe:
#             ord.set_type(call.data)
#             self.menu_change_size(call)
#
#
#         elif call.data in self.size_cofe:
#             ord.set_size(call.data)
#             self.menu_change_syrop(call)
#
#         elif call.data in self.syrop_cofe:
#             ord.reload_time()
#             ord.set_topping(call.data)
#             self.menu_change_time(call)
#
#         elif call.data == 'main_menu':
#             self.menu_main(call)
#
#
# bot.enable_save_next_step_handlers(delay=2)
# bot.polling(none_stop=True)
#
#
#
#
#
