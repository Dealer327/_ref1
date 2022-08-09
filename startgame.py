"""Подготовка игрового процесса"""

import config

Players = ()
TOKENS = {'X': '', 'O': ''}


def player_name():
    """Запрашивает имя игрока, проверяет наличие имени в глобальной переменной имен, записывает в глобальную
    переменную """
    global Players
    name = input('Введите имя игрока -> ')
    if name not in config.PLAYERS:
        print(f'Имени {name} среди игроков нет. Зарегистрируем его или попробуем вести имя снова?')
        new_name = input('Введите (Reg) если хотите зарегистрировать, (Log) попробовать вести имя еще раз ->').upper()
        if new_name == 'REG':
            config.PLAYERS[name] = {'first_time': True, 'stats': {'W': '0',
                                                                  'T': '0',
                                                                  'F': '0'}}
            print(f'Добро пожаловать {name}!!!')
            Players += (name,)
        elif new_name == 'LOG':
            player_name()
        else:
            print('Не правильный ввод давайте попробуем еще раз')
            player_name()
    else:
        print(f'Добро пожаловать {name}!!!')
        Players += (name,)


def game_mode():
    """Запрашивает режим игры"""
    mode = input('Выберите режим игры "Single"(Sin) или "Two Players"(Two) ').upper()
    if mode == 'TWO':
        player_name()
    elif mode == 'SIN':
        pass
    return mode


def is_first_game():
    """Проверяет являться ли данная партия первой для любого из действующих игроков"""
    for name in Players:
        if config.PLAYERS[name]['first_time']:
            return True
        else:
            return False


def token_player():
    """Запрашивает символ, которым будут играть игроки"""
    token = input(f'{Players[0]} выберите каким символом будете играть "X" или "O" ').upper()
    if token == 'X':
        TOKENS['X'] = Players[0]
        TOKENS['O'] = Players[1]
    else:
        TOKENS['X'] = Players[1]
        TOKENS['O'] = Players[0]
