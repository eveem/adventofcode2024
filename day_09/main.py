def read_input(filename):
    with open(filename, "r") as file:
        for line in file:
            return line.strip()

def init_disk(s):
    res = []
    curr = 0
    n = len(s)
    for i in range(0, n, 2):
        res += [str(curr)] * int(s[i])
        curr += 1
        if i + 1 != n:
            res += ["."] * int(s[i + 1])
    
    return res

def fragment(disk):
    n = len(disk)
    l = 0
    r = n - 1

    while l < r:
        if disk[l] == "." and disk[r] != ".":
            disk[l], disk[r] = disk[r], "."
            r -= 1
            l += 1
        elif disk[l] != ".":
            l += 1
        elif disk[r] == ".":
            r -= 1

    return disk

def checksum(disk):
    total = 0
    n = len(disk)

    for i in range(n):
        if disk[i] == ".":
            break
        total += int(disk[i]) * i

    return total
    
def first_star():
    s = read_input("small_input.txt")
    # s = read_input("input.txt")
    
    disk = init_disk(s)
    disk = fragment(disk)
    total = checksum(disk)

    print(f"first star result: {total}")

def second_star():
    s = read_input("small_input.txt")
    # s = read_input("input.txt")
    
    total = 0

    print(f"second star result: {total}")

if __name__ == "__main__":
    first_star()
    second_star()