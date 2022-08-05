"""Модуль реализации функции о сделанных ходах в текущей партии"""


DIM = 3
turns = [[' ']*DIM for _ in range(DIM)]


def show_field(playfiled):
    """Вывод игрового поля"""
    # весь функционал вывода поля будет пополняться в ходе написания остального кода
    #!!!ДОБАВИТЬ НЕ ЗАБЫТЬ!!!
    # ИСПРАВИТЬ: либо лишняя внешняя нижняя границы поля, либо не хватает верхней, левой и правой внешних границ поля
    for i in range(DIM):
        print('|'.join([str(row).center(5) for row in playfiled[i]]))
        print('-'*17)


def check_win():
    """Проверка выигрышных ходов"""
    # столбцы игрового поля
    horizontals = [[turns[j][i] for j in range(DIM)] for i in range(DIM)]
    # диагональные линии игрового поля
    diagonals = [[turns[i][i] for i in range(DIM)],
                 [turns[i][DIM-i-1] for i in range(DIM)]]
    # перебор горизонтальных вертикальных и диагональных линий игрового поля
    for win in (turns, horizontals, diagonals):
        for row in win:
            if ' ' in row:
                continue
            elif len(set(row)) == 1 and all(row):
                return True


show_field(turns)
check_win()
