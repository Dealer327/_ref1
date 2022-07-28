"""Модуль реализации функции о сделанных ходах в текущей партии"""


turns = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def show_field():
    """Функция отрисовки игрового поля"""
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(turns[0], turns[1], turns[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(turns[3], turns[4], turns[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(turns[6], turns[7], turns[8]))
    print("\t     |     |")
    print("\n")
show_field()