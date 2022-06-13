import json

import settings


class order_manager:

    def test_create_json(self):
        # data = {
        #     "president": {
        #         "name": "Zaphod Beeblebrox",
        #         "species": "Betelgeusian"
        #     }
        # }
        # with open("data_file.json", "w") as write_file:
        #     json.dump(data, write_file)

        with open(settings.PATH_MAIN_MENU, "r") as read_file:
            data = json.load(read_file)

        for view_drinks in data:
            for type_drinks in view_drinks:
                print(type_drinks)
            # print(i)
        # print(data[])
        # json_string = data
        # data = json.load(json_string)
        # print(data)


if __name__ == '__main__':
    order_manager.test_create_json(self='')