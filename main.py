"""Модуль верхнего уровня для учебного проекта крестики-нолики"""

from configparser import ConfigParser as CP

import config


def name_player():
    """Ввод имени игрока и проверка присутствие этого имени в глобальной переменной."""
    # Не правильно отрабатывает скрипт, каждый раз перезаписывает значения!
    # не знаю как исправить!
    name = input('Введите свой ник -> ')
    if name not in config.PLAYERS:
        # 1 ВАРИАНТ
        config_file = CP()
        config_file.add_section(name)
        config_file.set(name, 'first_time', 'False')
        config_file.set(name, 'stats', '0,0,0')
        with open('players.ini', 'w') as file_obj:
            config_file.write(file_obj)
        print(config.PLAYERS)

        # 2 ВАРИАНТ
        # config_file[name] = {'first_time': 'False', 'stats': '0,0,0'}
        # with open('players.ini', 'w') as file_obj:
        #     config_file.write(file_obj)
        # print(config.PLAYERS)


name_player()
print(config.read_ini())


# суперцикл
while True:
    command = input(' > ')
    if command in ('quit', 'exit', 'q', 'e'):
        break
    elif command in ('new', 'n'):
        pass
