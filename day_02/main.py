def read_input(filename):
    grid = []
    with open(filename, "r") as file:
        for line in file:
            row = list(map(int, line.split(" ")))
            grid.append(row)
    return grid

def diff_in_range(nums, lower, upper):
    n = len(nums)
    for i in range(1, n):
        if not (lower <= abs(nums[i] - nums[i - 1]) <= upper):
            return False
    return True

def get_direction(nums):
    status = "inc" if nums[0] < nums[1] else "dec"
    status = "tie" if nums[0] == nums[1] else status
    
    if status != "tie":
        pivot = nums[0]
        n = len(nums)

        for i in range(1, n):
            if pivot == nums[i]:
                status = "tie"
                break
            elif (status == "inc" and pivot < nums[i]) or (status == "dec" and pivot > nums[i]):
                pivot = nums[i]
            else:
                status = "switch"
                break
    
    return status

def is_safe(row, lower, upper):
    direction = get_direction(row)
    if direction == "inc" or direction == "dec":
        return diff_in_range(row, lower, upper)
    else:
        return False

def get_properties(nums):
    # tie, inc, dec
    tie, inc, dec = 0, 0, 0
    n = len(nums)
    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            dec += 1
        elif nums[i] > nums[i - 1]:
            inc += 1
        else:
            tie += 1
    
    return (tie, inc, dec)

def remove_one(nums):
    n = len(nums)
    for i in range(n):
        if is_safe(nums[:i] + nums[i + 1:], 1, 3):
            return True
    return False

def first_star():
    # safe row is row that inc or dec and has diff in range [1, 3]
    total = 0
    # grid = read_input("small_input.txt")
    grid = read_input("input.txt")
    for row in grid:
        total += is_safe(row, 1, 3)
    
    print(f"first star result: {total}")

def second_star():
    total = 0
    # grid = read_input("small_input.txt")
    grid = read_input("input.txt")
    for row in grid:
        if is_safe(row, 1, 3) or remove_one(row):
            total += 1
    
    print(f"second star result: {total}")

if __name__ == "__main__":
    first_star()
    second_star()