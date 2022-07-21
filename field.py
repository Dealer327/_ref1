"""Модуль реализации функции о сделаных ходах в текущей партии"""

turns = ['', '', '', '', '', '', '', '', '']
"Функция вывода игрового поля и отоброжения текущих ходов "


def show_field(turns):
    print('-' * 17)
    print(f"|  {turns[0]}  |  {turns[1]}   |  {turns[2]}  |")
    print('-' * 19)
    print(f"|  {turns[3]}  |  {turns[4]}   |  {turns[5]}  |")
    print('-' * 19)
    print(f"|  {turns[6]}  |  {turns[7]}   |  {turns[8]}  |")
    print('-' * 19)


'''Функция ввода хода игрока !!!тест'''


def turns_players():
    a = int(input())
    while a != '':
        if 1 <= a <= 9:
            for i in range(len(turns)):
                if i == a - 1:
                    if turns[i] == '':
                        turns[i] = 'x'
                        show_field(turns)
                    else:
                        print('Эта ячейка игрового поля ')
        a = int(input())


turns_players()

'''Функция проверки выйгрошной комбинации'''


def check_win(turns):
    pass
