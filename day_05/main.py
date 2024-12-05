def read_input(filename):
    valid = set()
    order = []

    with open(filename, "r") as file:
        flag = True
        for line in file:
            curr = line.strip()
            if curr == "":
                flag = False
            if flag:
                x, y = map(int, curr.split("|"))
                valid.add((x, y))
            elif flag == False and curr != "":
                x = list(map(int, curr.split(",")))
                order.append(x)
            
    return valid, order

def is_correct_order(valid, order):
    n = len(order)
    for i in range(n):
        for j in range(i + 1, n):
            if (order[i], order[j]) not in valid or (order[j], order[i]) in valid:
                return False
    return True

def invalid_pairs(valid, order):
    n = len(order)
    res = []
    for i in range(n):
        for j in range(i + 1, n):
            if (order[i], order[j]) not in valid:
                res.append([order[i], order[j]])
    
    return res

def permutation(nums):
    res = []
    n = len(nums)
    def _helper(path):
        if len(path) == n:
            res.append(path[:])
            return
        
        for i in range(n):
            if nums[i] not in path:
                path.append(nums[i])
                _helper(path)
                path.pop()
    
    _helper([])
    return res

def first_star():
    total = 0
    # valid, order = read_input("small_input.txt")
    valid, order = read_input("input.txt")

    for line in order:
        n = len(line)
        if is_correct_order(valid, line):
            total += line[n // 2]

    print(f"first star result: {total}")

def second_star():
    total = 0
    # valid, order = read_input("small_input.txt")
    valid, order = read_input("input.txt")

    for line in order:
        n = len(line)
        if not is_correct_order(valid, line):
            for new_order in permutation(line):
                if is_correct_order(valid, new_order):
                    total += new_order[n // 2]
                    break

    print(f"second star result: {total}")

if __name__ == "__main__":
    first_star()
    second_star()