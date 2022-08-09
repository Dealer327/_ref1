"""Модуль верхнего уровня для учебного проекта крестики-нолики"""


import startgame
import config
import helpme
import field

print('Крестики | Нолики')
startgame.player_name()
if startgame.is_first_game():
    helpme.show_help()
startgame.game_mode()
startgame.token_player()



# суперцикл
while True:
    command = input(' > ')
    if command in ('quit', 'exit', 'q', 'e'):
        break
    elif command in ('new', 'n'):
        pass
