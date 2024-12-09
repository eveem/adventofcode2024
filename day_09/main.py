import heapq

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
        if disk[i] != ".":
            total += int(disk[i]) * i

    return total
    
def list_space(disk):
    n = len(disk)
    curr = 0
    res = []
    
    for i in range(n):
        if disk[i] == ".":
            curr += 1
        elif disk[i] != "." and curr != 0:
            heapq.heappush(res, [i - curr, curr])
            curr = 0
    
    return res

def move_file(spaces, file, disk):
    key, value, index = file
    temp = []
    
    while spaces:
        idx, space = heapq.heappop(spaces)
        if space >= value and idx <= index:
            for i in range(idx, idx + value):
                disk[i] = key
            for i in range(index, index + value):
                disk[i] = "."
            space -= value
            if space != 0:
                heapq.heappush(temp, [idx + value, space])
            break
        
        heapq.heappush(temp, [idx, space])

    return disk

def list_file(disk):
    res = []
    n = len(disk)
    i = 0
    
    while i < n:
        ch = disk[i]
        curr = 1
        while i + 1 < n and disk[i] == disk[i + 1]:
            curr += 1
            i += 1
        if ch != ".":
            res.append([ch, curr, i - curr + 1])
        i += 1

    return res

def first_star():
    s = read_input("small_input.txt")
    # s = read_input("input.txt")
    
    disk = init_disk(s)
    disk = fragment(disk)
    total = checksum(disk)

    print(f"first star result: {total}")

def second_star():
    # s = read_input("small_input.txt")
    s = read_input("input.txt")

    disk = init_disk(s)
    files = list_file(disk)

    for file in files[::-1]:
        spaces = list_space(disk)
        disk = move_file(spaces, file, disk)
        
    total = checksum(disk)
    print(f"second star result: {total}")

if __name__ == "__main__":
    first_star()
    second_star()