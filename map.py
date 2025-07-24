map = []
height = 21
width = 41

for i in range(height):
    row = []
    for j in range(width):
        if i == (height - 1) // 2 and j == (width - 1) // 2:
            row.append("@")
        elif i == 0 or i == height - 1 or j == 0 or j == width - 1:
            row.append("#")
        else:
            row.append(".")
    map.append(row)

def show_map(map):
    for row in map:
        print("".join(row))

if __name__ == "__main__":
    show_map(map)