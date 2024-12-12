from collections import Counter
import sys
sys.set_int_max_str_digits(0)

def read_input(filename):
    with open(filename, "r") as file:
        for line in file:
            return line.strip().split(" ")

def blink(stone):
    if stone == "0":
        return ["1"]
    elif len(stone) % 2 == 0:
        m = len(stone) // 2
        l = stone[:m].lstrip("0")
        r = stone[m:].lstrip("0")
        if len(l) == 0:
            l = "0"
        if len(r) == 0:
            r = "0"
        return [l, r]
    
    return [str(int(stone) * 2024)]

def calculate(stones):
    res = []

    for stone in stones:
        for s in blink(stone):
            res.append(s)

    return res

def first_star():
    stones = read_input("small_input_02.txt")
    # stones = read_input("input.txt")
    TIME = 25

    for _ in range(TIME):
        stones = calculate(stones)

    print(f"first star result: {len(stones)}")

def second_star():
    # stones = read_input("small_input_01.txt")
    stones = read_input("input.txt")
    TIME = 75
    total = 0
    
    print(f"second star result: {total}")

if __name__ == "__main__":
    first_star()
    second_star()

# 0
# 1
# 2024
# 20 24
# 2 0 2 4
# 4048 1 4048 8096
# 40 48 2024 40 48 80 96
# 4 0 4 8 20 24 4 0 4 8 8 0 9 6
# 8096 1 8096 16192 2 0 2 4 8096 1 8096 16192 16192 1 18216 12144

# 27
# 2 7
# 4048 14168
# 40 48 28676032
# 4 0 4 8 2867 6032
# 8096 1 8096 16192 28 67 60 32
# 80 96 2024 80 96 32772608 2 8 6 7 6 0 3 2
# 8 0 9 6 20 24 8 0 9 6 3277 2608 4048 16192 12144 ...