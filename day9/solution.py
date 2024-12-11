def part_two():
    digits = read_input_data()
    _digits = []
    i = 0
    flag = True
    for digit in digits[0]:
        if flag:
            _digits.append([i] * digit)
        else:
            _digits.append(["."] * digit)
        if flag:
            i += 1
        flag = not flag

    print(_digits)
    l = len(_digits)
    for i in range(l - 1, -1, -1):
        if _digits and "." not in _digits[i]:
            for j in range(i):
                li = len(_digits[i])
                l_point = 0
                for lj in _digits[j]:
                    if lj == ".":
                        l_point += 1
                if "." in _digits[j] and li <= l_point:
                    for k in range(li):
                        _digits[j][_digits[j].index(".")] = _digits[i][k]
                        _digits[i][k] = "."
                    break
    i = 0
    s = 0
    for d in _digits:
        for c in d:
            if c != ".":
                s += i * c
            i += 1
    print(_digits)
    return s


def part_one():
    digits = read_input_data()
    _digits = []
    i = 0
    flag = True
    for digit in digits[0]:
        for d in range(digit):
            if flag:
                _digits.append(i)
            else:
                _digits.append(".")
        if flag:
            i += 1
        flag = not flag

    print(_digits)
    l = len(_digits)
    p = l - 1
    for i in range(l):
        if _digits[i] == ".":
            while i < p:
                if _digits[p] != ".":
                    _digits[i] = _digits[p]
                    _digits[p] = "."
                    p -= 1
                    break
                p -= 1
    print(_digits)
    i = 0
    s = 0
    for d in _digits:
        if d == ".":
            break
        s += i * d
        i += 1
    return s


def read_input_data():
    digits = []
    with open("input.txt", "r") as file:
        for line in file:
            digits.append(list(map(int, line.strip())))
    print(digits)
    return digits


print(part_one())
print(part_two())
