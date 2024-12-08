def read_input(filename):
    grid = []
    with open(filename, "r") as file:
        for line in file:
            grid.append(line.strip())
    return grid

def list_position(grid):
    data = {}
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != ".":
                if grid[i][j] not in data:
                    data[grid[i][j]] = []
                data[grid[i][j]].append([i, j])
    
    return data

def find_diff(points):
    res = []
    n = len(points)

    for i in range(n):
        x, y = points[i]
        for j in range(i + 1, n):
            u, v = points[j]
            res.append([u - x, v - y])

    return res

def generate_antinode(points, rows, cols, flag):
    res = []
    n = len(points)

    for i in range(n):
        x, y = points[i]
        for j in range(i + 1, n):
            if not flag:
                r = 1
            else:
                r = 50
            while r > 0:
                u, v = points[j]
                dx, dy = (u - x) * r, (v - y) * r
                if 0 <= x - dx < rows and 0 <= y - dy < cols:
                    res.append([x - dx, y - dy])
                dx, dy = (x - u) * r, (y - v) * r
                if 0 <= u - dx < rows and 0 <= v - dy < cols:
                    res.append([u - dx, v - dy])
                r -= 1

    return res

def first_star():
    # grid = read_input("small_input.txt")
    grid = read_input("input.txt")
    
    data = list_position(grid)
    rows = len(grid)
    cols = len(grid[0])
    total = 0

    for _, v in data.items():
        points = generate_antinode(v, rows, cols, False)
        for x, y in points:
            if grid[x][y] == ".":
                total += 1

    print(f"first star result: {total}")

def second_star():
    # grid = read_input("small_input.txt")
    grid = read_input("input.txt")
    
    data = list_position(grid)
    rows = len(grid)
    cols = len(grid[0])
    antinodes = set()

    for _, v in data.items():
        for x, y in v:
            antinodes.add((x, y))
        points = generate_antinode(v, rows, cols, True)
        for x, y in points:
            if grid[x][y] == ".":
                antinodes.add((x, y))

    print(f"second star result: {len(antinodes)}")

if __name__ == "__main__":
    first_star()
    second_star()