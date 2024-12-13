def read_input(filename):
    machines = []
    with open(filename, "r") as file:
        lines = list(file)
        n = len(lines)
        for i in range(0, n, 4):
            machine = {}
            for j in range(3):
                line = lines[i + j].strip().split(" ")
                if j == 0:
                    x = int(line[2].replace("X+", "").replace(",", ""))
                    y = int(line[3].replace("Y+", ""))
                    machine["A"] = (x, y)
                elif j == 1:
                    x = int(line[2].replace("X+", "").replace(",", ""))
                    y = int(line[3].replace("Y+", ""))
                    machine["B"] = (x, y)
                elif j == 2:
                    x = int(line[1].replace("X=", "").replace(",", ""))
                    y = int(line[2].replace("Y=", ""))
                    machine["Target"] = (x, y)
            machines.append(machine)
    
    return machines

def calculate(machines):
    xa, ya = machines["A"]
    xb, yb = machines["B"]
    xt, yt = machines["Target"]

    COST_A = 3
    COST_B = 1

    res = float("inf")

    for i in range(1, 101):
        for j in range(1, 101):
            if xa * i + xb * j == xt and ya * i + yb * j == yt:
                res = min(res, i * COST_A + j * COST_B)

    return res

def calculate_2(machines):
    xa, ya = machines["A"]
    xb, yb = machines["B"]
    xt, yt = machines["Target"]
    xt += 10000000000000
    yt += 10000000000000

    COST_A = 3
    COST_B = 1

    a = xa * yb 
    b = xb * ya
    c = xt * yb
    d = yt * xb

    if a > b:
        e = a - b
        f = c - d
    else:
        e = b - a
        f = d - c
    
    x = f / e
    y = (xt - xa * x) / xb

    res = float("inf")
    if int(x) == x and int(y) == y:
        res = x * COST_A + y * COST_B

    return res

def first_star():
    machines = read_input("small_input_01.txt")
    # machines = read_input("input.txt")
    total = 0

    for machine in machines:
        tokens = calculate(machine)
        if tokens != float("inf"):
            total += tokens

    print(f"first star result: {total}")

def second_star():
    # machines = read_input("small_input_01.txt")
    # machines = read_input("small_input_02.txt")
    machines = read_input("input.txt")
    total = 0

    for i, machine in enumerate(machines):
        tokens = calculate_2(machine)
        if tokens != float("inf"):
            total += tokens

    print(f"second star result: {int(total)}")

if __name__ == "__main__":
    first_star()
    second_star()