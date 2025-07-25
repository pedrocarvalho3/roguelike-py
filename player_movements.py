from map import game_map

def catch_player():
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j] == "💂🏼‍♂️":
                return i,j

def move_player_up():
    i, j = catch_player()
    if game_map[i - 1][j] == " .":
        game_map[i - 1][j] = "💂🏼‍♂️"
        game_map[i][j] = " ."  

def move_player_down():
    i, j = catch_player()
    if game_map[i + 1][j] == " .":
        game_map[i + 1][j] = "💂🏼‍♂️"
        game_map[i][j] = " ." 

def move_player_right():
    i, j = catch_player()
    if game_map[i][j + 1] == " .":
        game_map[i][j + 1] = "💂🏼‍♂️"
        game_map[i][j] = " ." 

def move_player_left():
    i, j = catch_player()
    if game_map[i][j - 1] == " .":
        game_map[i][j - 1] = "💂🏼‍♂️"
        game_map[i][j] = " ." 