def read_input(filename):
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(line)
    return lines

def extract_valid_mul(s):
    stack = []
    n = len(s)
    i = n - 1

    while i >= 2:
        if s[i - 2:i + 1] == "mul":
            st = i - 2
            if s[i + 1] == "(":
                t = s[i + 1]
                i += 2
                while i < n and s[i] != ")":
                    t += s[i]
                    i += 1
                
                if i < n:
                    t += s[i]
                
                try:
                    t = t.replace("(", "").replace(")", "")
                    x, y = map(int, t.split(","))
                    stack.append([x, y])
                except:
                    pass
            i = st
        i -= 1
    
    return stack

def first_star():
    total = 0
    # lines = read_input("1_small_input.txt")
    lines = read_input("input.txt")

    for line in lines:
        pairs = extract_valid_mul(line)
        for x, y in pairs:
            total += x * y

    print(f"first star result: {total}")

def second_star():
    total = 0
    print(f"second star result: {total}")

if __name__ == "__main__":
    first_star()
    second_star()