from collections import Counter, defaultdict

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

# def count_points(grid, crop, x, y):
#     rows = len(grid)
#     cols = len(grid[0])
#     cnt = defaultdict(int)
#     seen = set()
#     directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#     def _helper(x, y):
#         seen.add((x, y))
#         for dx, dy in directions:
#             nx, ny = dx + x, dy + y
#             if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == crop and (nx, ny) not in seen:
#                 _helper(nx, ny)
    
#     _helper(x, y)

#     for x, y in seen:
#         for dx, dy in directions:
#             nx, ny = dx + x, dy + y
#             if nx < 0 or nx == rows or ny < 0 or ny == cols or grid[nx][ny] != crop:
#                 cnt[(nx, ny)] += 1

#     return cnt

# def group_points(cnt):
#     res = []

#     def _dfs(x, y, path, directions):
#         path.append((x, y))
#         cnt[(x, y)] -= 1
#         for dx, dy in directions:
#             nx, ny = dx + x, dy + y
#             if (nx, ny) in cnt and cnt[(nx, ny)] > 0 and (nx, ny) not in path:
#                 _dfs(nx, ny, path, directions)
#         return path

#     temp = sorted(cnt.items(), key=lambda item: (item[1], -item[0][0], -item[0][1]), reverse=True)

#     for (u, v), val in temp:
#         while cnt[(u, v)] > 0 and (((u + 1, v) in cnt and cnt[(u + 1, v)] > 0) or ((u, v + 1) in cnt and cnt[(u, v + 1)] > 0)):
#             if cnt[(u, v)] > 0 and (u + 1, v) in cnt and cnt[(u + 1, v)] > 0:
#                 res.append(_dfs(u, v, [], [[1, 0]]))
#             if cnt[(u, v)] > 0 and (u, v + 1) in cnt and cnt[(u, v + 1)] > 0:
#                 res.append(_dfs(u, v, [], [[0, 1]]))

#     for (u, v), val in cnt.items():
#         for _ in range(val):
#             res.append([(u, v)])

#     return res

def flood_field(grid, crop, x, y, visited):
    rows = len(grid)
    cols = len(grid[0])

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    def _helper(x, y):
        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == crop and (nx, ny) not in visited:
                _helper(nx, ny)
    
    _helper(x, y)
    return visited


def find_corners(grid, points):
    corners = 0
    rows = len(grid)
    cols = len(grid[0])

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    for x, y in points:
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if (nx, ny) not in points:
                if (x - dy, y + dx) not in points or (nx - dy, ny + dx) in points:
                    corners += 1

    return corners

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
    # grid = read_input("small_input_01.txt")
    # grid = read_input("small_input_02.txt")
    # grid = read_input("small_input_03.txt")
    # grid = read_input("small_input_04.txt")
    grid = read_input("small_input_05.txt")
    # grid = read_input("small_input_06.txt")
    # grid = read_input("input.txt")
    
    total = 0
    rows = len(grid)
    cols = len(grid[0])
    seen = set()

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in seen:
                area, _, seen = find_perimeter(grid, grid[r][c], r, c, seen)
                points = flood_field(grid, grid[r][c], r, c, set())
                seen = seen.union(points)
                side = find_corners(grid, points)
                total += area * side

    print(f"second star result: {total}")

if __name__ == "__main__":
    first_star()
    second_star()