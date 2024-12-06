from collections import defaultdict

def read_input(filename):
    grid = []
    with open(filename, "r") as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid

def move(grid):
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "^":
                x, y = i, j
                break
    
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    curr = 0
    
    while True:
        grid[x][y] = "x"
        nx, ny = x + directions[curr][0], y + directions[curr][1]
        if grid[nx][ny] == "#":
            curr += 1
            curr %= 4
        else:
            grid[nx][ny] = "x"
            x, y = nx, ny
        
        if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
            break
            
    return grid

def is_cycle(grid):
    visited = defaultdict(int)
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "^":
                x, y = i, j
                break
    
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    curr = 0
    
    while True:
        visited[(x, y)] += 1
        nx, ny = x + directions[curr][0], y + directions[curr][1]
        if grid[nx][ny] == "#":
            curr += 1
            curr %= 4
        else:
            visited[(nx, ny)] += 1
            x, y = nx, ny
        
        if visited[(x, y)] == 10:
            return True
        
        if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
            return False

def possible_position(grid):
    points = []
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "x":
                points.append([i, j])
    
    return points

def count_x(grid):
    total = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "x":
                total += 1

    return total

def first_star():
    grid = read_input("small_input.txt")
    # grid = read_input("input.txt")

    grid = move(grid)
    total = count_x(grid)

    print(f"first star result: {total}")

def second_star():
    # grid = read_input("small_input.txt")
    grid = read_input("input.txt")
    og_grid = [[i for i in row] for row in grid]
    
    x_grid = move(grid)
    points = possible_position(x_grid)
    total = 0
    res = []
    
    for x, y in points:
        original = og_grid[x][y]
        if original == "^":
            continue
        og_grid[x][y] = "#"
        if is_cycle(og_grid):
            total += 1
            res.append([x, y])
        og_grid[x][y] = original

    print(f"second star result: {total}")

if __name__ == "__main__":
    first_star()
    second_star()