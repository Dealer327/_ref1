"""Модуль верхнего уровня для учебного проекта крестики-нолики"""

import config
from configparser import ConfigParser as CP


def name_player():
    """Ввод имени игрока и проверка присутствие этого имени в глобальной переменной."""

    name = input('Введите свой ник -> ')
    # Не правильно отрабатывает скрипт, каждый раз перезаписывает значения!
    # не знаю как ИСПРАВИТЬ!
    if name not in config.PLAYERS:
        '''1ВАРИАНТ config_file = CP()
        config_file.add_section(name)
        config_file.set(name, 'first_time', 'False')
        config_file.set(name, 'stats', '0,0,0')
        with open('players.ini', 'w') as file_obj:
            config_file.write(file_obj)
        print(config.PLAYERS)'''

        '''2 ВАРИАНТ config_file[name] = {'first_time': 'False', 'stats': '0,0,0'}

        with open('players.ini', 'w') as file_obj:
            config_file.write(file_obj)
        print(config.PLAYERS)'''


name_player()
print(config.read_ini())
# суперцикл
while True:
    command = input('>')
    if command in ('quit', 'exit', 'q', 'e'):
        break
    elif command in ('new', 'n'):
        pass
