import os
from getch import getch 

from map import game_map, show_map
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
    show_map(game_map)


    while True:
        key = getch().lower()  

        if key == "w":
            move_player_up()
        elif key == "s":
            move_player_down()
        elif key == "a":
            move_player_left()
        elif key == "d":
            move_player_right()
        elif key == "q":
            print("Saindo do jogo...")
            break

        clear_screen()
        show_map(game_map)



game()