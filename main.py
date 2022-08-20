"""Модуль верхнего уровня для учебного проекта крестики-нолики"""


import startgame
import config
import helpme
import field

print('Крестики | Нолики')

if config.read_ini() != True:
    print('Добро пожаловать в игру!')
startgame.player_name()
helpme.show_commands()

if startgame.is_first_game():
    helpme.show_help()
    helpme.show_commands()



# суперцикл
while True:
    command = input(' > ').lower()
    if command in ('quit', 'exit', 'q', 'e'):
        break
    elif command in ('new', 'n'):
        startgame.game_mode()
        startgame.token_player()
        helpme.help_start()
        field.turns_players()
        helpme.show_commands()
        continue







