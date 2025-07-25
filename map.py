game_map = []
height = 41
width = 61

for i in range(height):
    row = []
    for j in range(width):
        if i == (height - 1) // 2 and j == (width - 1) // 2:
            row.append("💂🏼‍♂️")
        elif i == 0 or i == height - 1 or j == 0 or j == width - 1:
            row.append(" █")
        else:
            row.append(" .")
    game_map.append(row)

def show_map(game_map):
    for row in game_map:
        print("".join(row))

if __name__ == "__main__":
    show_map(game_map)