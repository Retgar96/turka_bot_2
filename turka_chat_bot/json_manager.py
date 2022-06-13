import json
import pickle
import pandas as pd
import settings

def read_json():
    with open(settings.PATH_MAIN_MENU) as json_file:
        data = json.load(json_file)
    return data

def record_json(data):
    with open(settings.PATH_MAIN_MENU, 'w') as outfile:
        json.dump(data, outfile)

def get_menu(type_info):
    menu = read_json()
    return menu[type_info]




