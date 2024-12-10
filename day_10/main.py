def read_input(filename):
    grid = []
    with open(filename, "r") as file:
        for line in file:
            grid.append(line.strip())
    return grid

# how many 9 can reach from 0
# only up, down, left, right

def dfs(grid, x, y):
    reachable = set()
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    seen = set()
    rows = len(grid)
    cols = len(grid[0])

    def _helper(x, y):
        seen.add((x, y))

        if grid[x][y] == "9":
            reachable.add((x, y))
            return 

        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in seen and grid[nx][ny] != "." and int(grid[x][y]) + 1 == int(grid[nx][ny]):
                _helper(nx, ny)

    _helper(x, y)

    return reachable

def find_start_points(grid):
    points = []
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "0":
                points.append([i, j])

    return points

def count_path(grid, x, y):
    res = 0
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    seen = set()
    seen.add((x, y))
    rows = len(grid)
    cols = len(grid[0])

    def _helper(x, y):
        nonlocal res
        
        if grid[x][y] == "9":
            res += 1
            return
        
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in seen and grid[nx][ny] != "." and int(grid[x][y]) + 1 == int(grid[nx][ny]):
                seen.add((nx, ny))
                _helper(nx, ny)
                seen.remove((nx, ny))

    _helper(x, y)

    return res

def first_star():
    # grid = read_input("small_input_04.txt")
    grid = read_input("input.txt")
    
    total = 0
    points = find_start_points(grid)

    for i, j in points:
        total += len(dfs(grid, i, j))

    print(f"first star result: {total}")

def second_star():
    # grid = read_input("small_input_04.txt")
    grid = read_input("input.txt")
    
    total = 0
    points = find_start_points(grid)

    for i, j in points:
        total += count_path(grid, i, j)

    print(f"second star result: {total}")

if __name__ == "__main__":
    first_star()
    second_star()