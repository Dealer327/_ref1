"""Подготовка игрового процесса"""

import config

Players = ()
Tokens = ('X', 'O')


def player_name():
    """Запрашивает имя игрока, проверяет наличие имени в глобальной переменной имен, записывает в глобальную
    переменную """
    global Players
    if Players:
        name = input('Введите имя второго игрока -> ')
    else:
        name = input('Введите имя игрока -> ')
    if name not in config.PLAYERS:
        print(f'Имени {name} среди игроков нет. Зарегистрируем его или попробуем вести имя снова?')
        new_name = input('Введите (Reg) если хотите зарегистрировать, (Log) попробовать вести имя еще раз -> ').upper()
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
    mode = input(f'Выберите режим игры "Single"(1)!!!(<- Временно не работает, приносим свои извинения)'
                 f' "Two Players"(2) ')
    if mode == '2':
        player_name()
    elif mode == '1':
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
    global Players
    token = input(f'{Players[0]} выберите каким символом будете играть "X" или "O" ').upper()
    if token == 'O':
        Players = (Players[1], Players[0])