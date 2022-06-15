import re
bot_token = '5347764327:AAHiA9j-HipQfEdvBuWyc72cLv7j6lhuR3Y'
PATH_MAIN_MENU = '/home/retgar/PycharmProjects/turka_chat_bot/data/main_menu_en.json'
PATH_TEMPORAL_MENU = "/home/retgar/PycharmProjects/turka_chat_bot/data"
PATH_JSON_MENU = '/home/retgar/PycharmProjects/turka_chat_bot/data/main_menu'
ADMIN_KEY = 'gowefqe;rjgqern3f34fmrco43fk0[qjv'
ADMIN_ID = ['1297710219']

PATTERN_TIMER = r'\d+\W\d+'


ADMIN_TYPE_ACTIONS = ['admins','settings','add_admin','change_menu']


# test regex
# print(re.findall(PATTERN_TIMER,'10:30'))