from collections import Counter
import sys
sys.set_int_max_str_digits(0)

def read_input(filename):
    with open(filename, "r") as file:
        for line in file:
            return Counter(line.strip().split(" "))

def blink(stones):
    temp = Counter()
    for k, v in stones.items():
        if k == "0":
            temp["1"] += v
        elif len(k) % 2 == 0:
            m = len(k) // 2
            l = k[:m].lstrip("0")
            r = k[m:].lstrip("0")
            if len(l) == 0:
                l = "0"
            if len(r) == 0:
                r = "0"
            temp[l] += v
            temp[r] += v
        else:
            temp[str(int(k) * 2024)] += v
    
    return temp

def first_star():
    # stones = read_input("small_input_02.txt")
    stones = read_input("input.txt")
    TIME = 25

    for _ in range(TIME):
        stones = blink(stones)

    print(f"first star result: {sum(stones.values())}")

def second_star():
    # stones = read_input("small_input_01.txt")
    stones = read_input("input.txt")
    TIME = 75

    for _ in range(TIME):
        stones = blink(stones)

    print(f"second star result: {sum(stones.values())}")

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