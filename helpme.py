"""Модуль помощи и подсказок игрокам"""
import startgame
import field


help_turns = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

COMMANDS = {
    'Начать новую игру': ('new', 'n'),
    'Выйти из игры': ('quit', 'exit', 'q', 'e')

}
Rules = f'' \
        f'Играть предстоит в интерфейсе командной строки. Поэтому для выполнения действий в игре необходимо ' \
        f'вводить команду и нажимать Enter'
Victory = f'Что бы одержать победу вам не обходимо поставить знак {startgame.Tokens[0]} или {startgame.Tokens[1]} ' \
          f'(в зависимости какой вы выбрали в начале игры) первым в последовательность из 3!'
number_turns = f'Для позиционирования своего символа используйте цифры для ввода 1-9'


def show_help():
    """Выводит в stdout раздел помощи"""
    print('***Help***')
    print(Rules)
    print(Victory)



def show_commands():
    for i in COMMANDS:
        print(f'{i} -> {COMMANDS[i]}')

def help_start():
    print(number_turns)
    help_board = field.show_field(help_turns)