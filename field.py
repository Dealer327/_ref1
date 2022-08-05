"""Модуль реализации функции о сделанных ходах в текущей партии"""




DIM = 3
turns = [[' ']*DIM for _ in range(DIM)]



def show_field(playfiled):
    """Вывод игрового поля"""
    #Весь функционал вывода поля будет пополняться в ходе написания остального кода
    #!!!ДОБАВИТЬ НЕ ЗАБЫТЬ!!!
    for i in range(DIM):
        print('|'.join([str(row).center(5) for row in playfiled[i]]))
        print('-'*17)

def check_win():
    """Проверка выйграшных ходов"""
    #столбцы игрового поля
    horizontals = [[turns[j][i] for j in range(DIM)] for i in range(DIM)]
    #диагональные линии игровго поля
    diagonals = [[turns[i][i] for i in range(DIM)],
                 [turns[i][DIM-i-1] for i in range(DIM)]]
    #перебор горизонтальных вертикальных и диаганальных линий игровго поля
    for vin in (turns,horizontals,diagonals):
        for row in vin:
            if ' ' in row:
                continue
            elif len(set(row)) == 1 and all(row):
                return True
show_field(turns)
check_win()
