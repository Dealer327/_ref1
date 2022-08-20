"""Дополнительный модуль подготовки игрового процесса"""

from pathlib import Path
from sys import argv
from configparser import ConfigParser as CP

SKRIPT_DIR = Path(argv[0]).parent
PLAYERS_INI_PATH = SKRIPT_DIR / "players.ini"
SAVES_INI_PATH = SKRIPT_DIR / "saves.ini"


PLAYERS = {}
SAVES = {}
Score = tuple[dict, dict]


def read_ini() -> bool:
    """Читает конфигурационные файлы, сохраняет прочитанные данные в глобальные переменные
       и возвращает True если приложение запущено впервые, иначе False."""
    global PLAYERS, SAVES
    ini_file = CP()
    ini_file.read(PLAYERS_INI_PATH)
    for player in ini_file.sections():
        ft = True if ini_file[player]['first_time'] == 'True' else False
        st = ini_file[player]['stats'].split(',')
        PLAYERS[player] = {'first_time': ft, 'stats': {'W': int(st[0]),
                                                       'T': int(st[1]),
                                                       'F': int(st[2])}}
    ini_file.clear()
    ini_file.read(SAVES_INI_PATH)
    for save in ini_file.sections():
        players = frozenset(save.split(','))
        SAVES[players] = dict(ini_file[save])
    if PLAYERS:
        return False
    else:
        return True



def save_ini():
    """Записывает данные в файлы, из глобальных переменный"""


