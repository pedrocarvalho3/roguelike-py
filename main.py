import os
from map import map, show_map

from player_movements import (
    move_player_left,
    move_player_right,
    move_player_up,
    move_player_down
)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_start_screen():
    clear_screen()
    print(r"""
  ██████╗ ██╗   ██╗████████╗ ██████╗ ███╗   ██╗
 ██╔═══██╗██║   ██║╚══██╔══╝██╔═══██╗████╗  ██║
 ██║   ██║██║   ██║   ██║   ██║   ██║██╔██╗ ██║
 ██║   ██║██║   ██║   ██║   ██║   ██║██║╚██╗██║
 ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██║ ╚████║
  ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═══╝
    """)
    print("           Welcome to PYTHON ROGUELIKE!")
    print("\n        Press [WASD] to move. Press [Q] to quit...\n")
    input()

def game():
    show_start_screen()
    clear_screen()
    show_map(map)


    while True:
        input("\nPressione Enter para mover para cima...")
        move_player_left()
        clear_screen()
        show_map(map)



game()