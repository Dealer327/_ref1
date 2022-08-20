"""Модуль реализации функции о сделанных ходах в текущей партии"""

import startgame
import config
from shutil import get_terminal_size as gts





# ОТВЕТИТЬ: чего-то я запутался; в вашем документе Архитектура записано, что вы будете использовать словарь для хранения данных о сделанных ходах - а тут внезапно появляется матрица; вы не определились? помочь с выбором?
DIM = 3
RANGE = range(DIM)
turns = [[' ']*DIM for _ in RANGE]


def show_field(playfiled):

    """Вывод игрового поля"""
    # весь функционал вывода поля будет пополняться в ходе написания остального кода
    #!!!ДОБАВИТЬ НЕ ЗАБЫТЬ!!!
    # ИСПРАВИТЬ: либо лишняя внешняя нижняя граница поля, либо не хватает верхней, левой и правой внешних границ поля
    print('-'*17)
    for i in RANGE:
        print('|'.join([str(row).center(5) for row in playfiled[i]]))
        print('-'*17)





def turns_players():
    """Запрос хода игроков"""
    global turns

    while not check_win(turns):
        for i in range(2):
            move = int(input(f'{startgame.Players[i]} ваш ход -> '))

            if 1 <= move <=3:
                if turns[0][move -1] == " ":
                    turns[0][move - 1] = startgame.Tokens[i]
                    show_field(turns)
                    if check_win(turns):
                        print(f'Victory {startgame.Players[i]}')


                    else:
                        continue
            elif 4 <= move <= 6:
                if turns[1][move - 4] == " ":
                    turns[1][move - 4] = startgame.Tokens[i]
                    show_field(turns)
                    if check_win(turns):
                        print(f'Victory {startgame.Players[i]}')
                        break
                    else:
                        continue
            elif 7 <= move <= 9:
                if turns[2][move -7] == " ":
                    turns[2][move - 7] = startgame.Tokens[i]
                    show_field(turns)
                    if check_win(turns):
                        print(f'Victory {startgame.Players[i]}')
                        break
                    else:
                        continue


def check_win(board):
    """Проверка выигрышных ходов"""
    # столбцы игрового поля
    verticals = [[board[j][i] for j in RANGE] for i in RANGE]
    # диагональные линии игрового поля
    diagonals = [[board[i][i] for i in RANGE],
                [board[i][DIM-i-1] for i in RANGE]]
    # перебор горизонтальных вертикальных и диагональных линий игрового поля
    for win in (board, verticals, diagonals):
        for row in win:
            if ' ' in row:
                continue
            elif len(set(row)) == 1 and all(row):
                return True

def update_stats():
    for i in range(2):
        pass












