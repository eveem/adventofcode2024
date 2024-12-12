def read_input(filename):
    grid = []
    with open(filename, "r") as file:
        for line in file:
            grid.append(line.strip())
    return grid

def find_perimeter(grid, crop, x, y, seen):
    perimeter = 0
    area = 0
    rows = len(grid)
    cols = len(grid[0])

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def _helper(x, y):
        nonlocal perimeter
        nonlocal area
        seen.add((x, y))
        
        area += 1
        perimeter += 4
        if x > 0 and grid[x - 1][y] == crop:
            perimeter -= 2
        if y > 0 and grid[x][y - 1] == crop:
            perimeter -= 2

        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == crop and (nx, ny) not in seen:
                _helper(nx, ny)

    _helper(x, y)
    return area, perimeter, seen

def first_star():
    # grid = read_input("small_input_01.txt")
    # grid = read_input("small_input_02.txt")
    # grid = read_input("small_input_03.txt")
    grid = read_input("input.txt")
    
    total = 0
    rows = len(grid)
    cols = len(grid[0])
    seen = set()

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in seen:
                area, perimeter, seen = find_perimeter(grid, grid[r][c], r, c, seen)
                total += area * perimeter

    print(f"first star result: {total}")

def second_star():
    # grid = read_input("small_input_04.txt")
    grid = read_input("input.txt")
    
    total = 0

    print(f"second star result: {total}")

if __name__ == "__main__":
    first_star()
    second_star()