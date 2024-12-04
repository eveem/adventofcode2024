def read_input(filename):
    grid = []
    with open(filename, "r") as file:
        for line in file:
            grid.append(line.strip())
    return grid

def count_xmas(grid):
    total = 0
    pattern = [
        [[0, 0, "X"], [0, 1, "M"], [0, 2, "A"], [0, 3, "S"]], # horizontal
        [[0, 0, "X"], [0, -1, "M"], [0, -2, "A"], [0, -3, "S"]], # horizontal backward
        [[0, 0, "X"], [1, 0, "M"], [2, 0, "A"], [3, 0, "S"]], # vertical
        [[0, 0, "X"], [-1, 0, "M"], [-2, 0, "A"], [-3, 0, "S"]], # vertical
        [[0, 0, "X"], [1, 1, "M"], [2, 2, "A"], [3, 3, "S"]], # diagonal top left to bottom right
        [[0, 0, "X"], [1, -1, "M"], [2, -2, "A"], [3, -3, "S"]], # diagonal top right to bottom left
        [[0, 0, "X"], [-1, 1, "M"], [-2, 2, "A"], [-3, 3, "S"]], # diagonal bottom left to top right
        [[0, 0, "X"], [-1, -1, "M"], [-2, -2, "A"], [-3, -3, "S"]], # diagonal bottom right to top left
    ]

    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            for p in pattern:
                matched = 0
                for dx, dy, exp in p:
                    if 0 <= dx + i < m and 0 <= dy + j < n and grid[dx + i][dy + j] == exp:
                        matched += 1
                total += matched == 4
    
    return total

def count_cross_mas(grid):
    total = 0
    pattern = [
        [
            [0, 0, "M"], [0, 2, "S"], 
            [1, 1, "A"], 
            [2, 0, "M"], [2, 2, "S"]
        ], 
        [
            [0, 0, "S"], [0, 2, "S"], 
            [1, 1, "A"], 
            [2, 0, "M"], [2, 2, "M"]
        ], 
        [
            [0, 0, "M"], [0, 2, "M"], 
            [1, 1, "A"], 
            [2, 0, "S"], [2, 2, "S"]
        ], 
        [
            [0, 0, "S"], [0, 2, "M"], 
            [1, 1, "A"], 
            [2, 0, "S"], [2, 2, "M"]
        ], 
    ]

    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            for p in pattern:
                matched = 0
                for dx, dy, exp in p:
                    if 0 <= dx + i < m and 0 <= dy + j < n and grid[dx + i][dy + j] == exp:
                        matched += 1
                total += matched == 5
    return total

def first_star():
    grid = read_input("small_input.txt")
    # grid = read_input("input.txt")
    total = count_xmas(grid)
    print(f"first star result: {total}")

def second_star():
    # grid = read_input("small_input.txt")
    grid = read_input("input.txt")
    total = count_cross_mas(grid)
    print(f"second star result: {total}")

if __name__ == "__main__":
    first_star()
    second_star()