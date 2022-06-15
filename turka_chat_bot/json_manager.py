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


def delete_type(type_main,type):
    menu = read_json()
    del menu[f"{type_main}"][f"{type}"]
    record_json(menu)
    print(f'элемент {type_main} {type} был удален')


def created_rest(type_main, new_type, price):
    menu = read_json()
    menu[f'{type_main}'][f'{new_type}'] = {}
    menu[f'{type_main}'][f'{new_type}']['price'] = price
    record_json(menu)


def created_product_drinks(type_main, new_type, arr_size):
    menu = read_json()
    menu[f'{type_main}'][f'{new_type}'] = {}
    for size in arr_size:
        menu[f'{type_main}'][f'{new_type}'][f'{size}'] = {'price': '0', 'ml': '0'}
        menu[f'{type_main}'][f'{new_type}'][f'{size}']['price'] = arr_size[f'{size}']['price']
        menu[f'{type_main}'][f'{new_type}'][f'{size}']['ml'] = arr_size[f'{size}']['ml']

    record_json(menu)


def overwrite_product_size(type_main, new_type, arr_size):
    menu = read_json()
    menu[type_main][new_type][arr_size['name']]['price'] = arr_size['price']
    menu[type_main][new_type][arr_size['name']]['ml'] = arr_size['ml']
    record_json(menu)

def overwrite_rest(type_main, new_type, price):
    menu = read_json()
    menu[f'{type_main}'][f'{new_type}']['price'] = price
    record_json(menu)
