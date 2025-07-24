from map import map

def catch_player():
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "@":
                return i,j

def move_player_up():
    i, j = catch_player()
    if map[i - 1][j] == ".":
        map[i - 1][j] = "@"
        map[i][j] = "."  

def move_player_down():
    i, j = catch_player()
    if map[i + 1][j] == ".":
        map[i + 1][j] = "@"
        map[i][j] = "." 

def move_player_right():
    i, j = catch_player()
    if map[i][j + 1] == ".":
        map[i][j + 1] = "@"
        map[i][j] = "." 

def move_player_left():
    i, j = catch_player()
    if map[i][j - 1] == ".":
        map[i][j - 1] = "@"
        map[i][j] = "." 