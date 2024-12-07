def read_input(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            target, nums = line.strip().split(": ")
            data.append({"target": int(target), "nums": list(map(int, nums.split(" ")))})
    return data

def generate_ops(nums, signs):
    ops = []
    n = len(nums)

    def _helper(idx, path):
        if len(path) == n - 1:
            ops.append(path[:])
            return
        
        for op in signs:
            path.append(op)
            _helper(idx + 1, path)
            path.pop()
    
    _helper(0, [])

    return ops

def calculate(nums, op):
    st = []
    i = 0
    
    for num in nums:
        if st:
            x = st.pop()
            if op[i] == "*":
                t = num * x
                i += 1
            elif op[i] == "+":
                t = num + x
                i += 1
            elif op[i] == "||":
                t = int(str(x) + str(num))
                i += 1
            st.append(t)
        else:
            st.append(num)

    return st[0]

def first_star():
    data = read_input("small_input.txt")
    # data = read_input("input.txt")

    total = 0
    for record in data:
        target = record["target"]
        nums = record["nums"]

        ops = generate_ops(nums, ["+", "*"])
        for op in ops:
            if calculate(nums, op) == target:
                total += target
                break

    print(f"first star result: {total}")

def second_star():
    # data = read_input("small_input.txt")
    data = read_input("input.txt")
    
    total = 0
    for record in data:
        target = record["target"]
        nums = record["nums"]

        ops = generate_ops(nums, ["+", "*", "||"])
        for op in ops:
            if calculate(nums, op) == target:
                total += target
                break

    print(f"second star result: {total}")

if __name__ == "__main__":
    first_star()
    second_star()