def Guard_cnt():
    file_path = "input.txt"
    matrix = []
    g = []
    i = 0
    j = 0
    with open(file_path, "r") as file:
        for line in file:
            _line = []
            j = 0
            for l in line.strip():
                if l == ".":
                    _line.append(0)
                elif l == "#":
                    _line.append(1)
                else:
                    _line.append(2)
                if l == "^":
                    g = [i, j]
                j += 1
            matrix.append(_line)
            i += 1
    # print(matrix)
    print(g)
    print(i)
    print(j)
    s = 1
    r = "u"
    while True:
        if g[0] == 0 or g[0] == i - 1 or g[1] == 0 or g[1] == j - 1:
            break
        if r == "u":
            if matrix[g[0] - 1][g[1]] == 1:
                r = "r"
                continue
            else:
                g[0] -= 1
        elif r == "r":
            if matrix[g[0]][g[1] + 1] == 1:
                r = "d"
                continue
            else:
                g[1] += 1
        elif r == "d":
            if matrix[g[0] + 1][g[1]] == 1:
                r = "l"
                continue
            else:
                g[0] += 1
        elif r == "l":
            if matrix[g[0]][g[1] - 1] == 1:
                r = "u"
                continue
            else:
                g[1] -= 1
        if matrix[g[0]][g[1]] != 2:
            s += 1
        matrix[g[0]][g[1]] = 2
    print(g)
    return s


def Guard_loop():
    file_path = "input.txt"
    matrix = []
    g = []
    _list = []
    i = 0
    j = 0
    with open(file_path, "r") as file:
        for line in file:
            _line = []
            j = 0
            for l in line.strip():
                if l == ".":
                    _line.append(0)
                elif l == "#":
                    _line.append(1)
                else:
                    _line.append(2)
                if l == "^":
                    g = [i, j]
                j += 1
            matrix.append(_line)
            i += 1
    # for row in matrix:
    #     print(row)
    #     print("\n")

    r = "u"
    ch = [g[0] - 1, g[1]]
    rch = "u"
    matrix[ch[0]][ch[1]] = 1
    cnt = 0
    while True:
        if g[0] == 0 or g[0] == i - 1 or g[1] == 0 or g[1] == j - 1:
            if ch == [9, 7] and rch == "d":
                break
            print(ch)
            print(g)
            matrix[ch[0]][ch[1]] = 0
            g = [6, 4]
            r = "u"
            for row in matrix:
                for col in row:
                    if col == 2:
                        matrix[matrix.index(row)][row.index(col)] = 0
            if rch == "u":
                if matrix[ch[0] - 1][ch[1]] == 1:
                    ch[1] += 1
                    rch = "r"
                else:
                    ch[0] -= 1
            elif rch == "r":
                if matrix[ch[0]][ch[1] + 1] == 1:
                    ch[0] -= 1
                    rch = "d"
                else:
                    ch[1] += 1
            elif rch == "d":
                if matrix[ch[0] + 1][ch[1]] == 1:
                    ch[1] -= 1
                    rch = "l"
                else:
                    ch[0] += 1
            elif rch == "l":
                if matrix[ch[0]][ch[1] - 1] == 1:
                    ch[0] += 1
                    rch = "u"
                else:
                    ch[1] -= 1
            matrix[ch[0]][ch[1]] = 1
            print(ch)
            print("--")
        if r == "u":
            if matrix[g[0] - 1][g[1]] == 1:
                r = "r"
                continue
            else:
                g[0] -= 1
        elif r == "r":
            if matrix[g[0]][g[1] + 1] == 1:
                r = "d"
                continue
            else:
                g[1] += 1
        elif r == "d":
            if matrix[g[0] + 1][g[1]] == 1:
                r = "l"
                continue
            else:
                g[0] += 1
        elif r == "l":
            if matrix[g[0]][g[1] - 1] == 1:
                r = "u"
                continue
            else:
                g[1] -= 1
        if matrix[g[0]][g[1]] == 2:
            if r == "u":
                if matrix[g[0] - 1][g[1]] != 1:
                    continue
            if r == "r":
                if matrix[g[0]][g[1] + 1] != 1:
                    continue
            if r == "d":
                if matrix[g[0] + 1][g[1]] != 1:
                    continue
            if r == "l":
                if matrix[g[0]][g[1] - 1] != 1:
                    continue
            n = list(ch + [rch])
            if n not in _list:
                _list.append(n)
            print(f"topildi {ch} {rch}")
            print(_list)
            if ch == [9, 7] and rch == "d":
                break
            matrix[ch[0]][ch[1]] = 0
            g = [6, 4]
            r = "u"
            for row in matrix:
                for col in row:
                    if col == 2:
                        matrix[matrix.index(row)][row.index(col)] = 0
            if rch == "u":
                if matrix[ch[0] - 1][ch[1]] == 1:
                    ch[1] += 1
                    rch = "r"
                else:
                    ch[0] -= 1
            elif rch == "r":
                if matrix[ch[0]][ch[1] + 1] == 1:
                    ch[0] -= 1
                    rch = "d"
                else:
                    ch[1] += 1
            elif rch == "d":
                if matrix[ch[0] + 1][ch[1]] == 1:
                    ch[1] -= 1
                    rch = "l"
                else:
                    ch[0] += 1
            elif rch == "l":
                if matrix[ch[0]][ch[1] - 1] == 1:
                    ch[0] += 1
                    rch = "u"
                else:
                    ch[1] -= 1
            matrix[ch[0]][ch[1]] = 1
        if ch == [4, 5]:
            print(f"---{g}---")
        matrix[g[0]][g[1]] = 2
    return _list


# print(Guard_cnt())
print(Guard_loop())
