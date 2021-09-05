'''
Задача 3. Криптовалюта

При работе с API (application programming interface)
сайта биржи по криптовалюте вы получили вот такие данные в виде словаря:


data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },

            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}





Теперь вам предстоит немного обработать эти данные.
Напишите программу, которая выполняет следующий алгоритм действий:

Вывести списки ключей и значений словаря.
В “ETH” добавить ключ “total_diff” со значением 100.
Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.
Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.
Внутри "sec_token_info" изменить название ключа “price” на “total_price”.
'''

import pprint


data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },

    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

def show_keys_and_values():
    '''Вывести списки ключей и значений словаря.'''
    key_list = []
    value_list = []
    for key, value in data.items():
        key_list.append(key)
        value_list.append(value)
    print('Список ключей \n {}'.format(key_list))
    print('Список значений \n {}'.format(value_list))


def add_key_to_ETH():
    'В “ETH” добавить ключ “total_diff” со значением 100.'
    data['ETH']['total_diff'] = 100
    
def change_name():
    'Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”'
    print(data['tokens'][0]['fst_token_info']['name'])
    data['tokens'][0]['fst_token_info']['name'] = 'doge'
    print(data['tokens'][0]['fst_token_info']['name'])

def pop_dict():
    'Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.'
    new_value = data['tokens'][0].pop('total_out')
    new_value_1 = data['tokens'][1].pop('total_out')
    data['ETH']['totalOut'] = (new_value, new_value_1)


def change_key():
    'Внутри "sec_token_info" изменить название ключа “price” на “total_price”.'
    data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')

# add_key_to_ETH()
# pprint.pprint(data)
# show_keys_and_values()
# change_name()
# pop_dict()
# change_key()