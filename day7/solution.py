def part_one():
    equalition = read_input_data()
    res = 0
    for key, value in equalition.items():
        res += is_bridge(key, value)
    return res


def part_two():
    equalition = read_input_data()
    res = 0
    for key, value in equalition.items():
        res += is_bridge3(key, value)
    return res


def is_bridge3(key, value):
    cnt = len(value) - 1
    operators = [0] * cnt
    rounds = 3**cnt
    for i in range(rounds):
        r = value[0]
        for o in range(len(operators)):
            if operators[o] == 0:
                r += value[o + 1]
            elif operators[o] == 1:
                r *= value[o + 1]
            elif operators[o] == 2:
                r = concat(r, value[o + 1])
        print(f"{key} == {r} {key == r} {value} {operators}")
        if key == r:
            return key
        operators = ternar_inc(operators)
    return 0


def concat(a, b):
    return int("".join(map(str, [a, b])))


def ternar_inc(operators):
    for i in range(len(operators) - 1, -1, -1):
        if operators[i] < 2:
            operators[i] += 1
            return operators
        else:
            operators[i] = 0
    operators.insert(0, 1)
    return operators


def is_bridge(key, value):
    cnt = len(value) - 1
    operators = [0] * cnt
    rounds = 2**cnt
    for i in range(rounds):
        r = value[0]
        for o in range(len(operators)):
            if operators[o] == 0:
                r += value[o + 1]
            else:
                r *= value[o + 1]
        print(f"{key} == {r} {value} {operators}")
        if key == r:
            return key
        operators = binar_inc(operators)
    return 0


def binar_inc(operators):
    for i in range(len(operators) - 1, -1, -1):
        if operators[i] == 0:
            operators[i] = 1
            return operators
        else:
            operators[i] = 0
    operators.insert(0, 1)
    return operators


def read_input_data():
    equalition = {}
    with open("input.txt", "r") as file:
        for line in file:
            equalition[int(line.split(":")[0])] = list(
                map(int, line.split(":")[1].strip().split())
            )
    print(equalition)
    return equalition


# print(part_one())
print(part_two())
