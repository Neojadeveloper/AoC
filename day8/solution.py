def part_two():
    matrix = read_input_data()
    row = len(matrix)
    col = len(matrix[0])
    cnt = 0
    print(f"{row}, {col}")
    nodes = set()  # Nodalarni takroran qo'shmaslik uchun to'plam
    for i in range(row):
        for j in range(col):
            ch = matrix[i][j]
            if ch != ".":  # Faqat belgi bor joylarni tekshirish
                node = (i, j)
                if node not in nodes:
                    cnt += 1
                    nodes.add(node)
                for k in range(i, row):
                    for l in range(col):
                        if i == k and l <= j:
                            continue  # O'z-o'zini va ilgari tekshirilganlarni o'tkazib yuborish
                        if matrix[k][l] == ch:
                            dr = k - i
                            dc = l - j
                            print(f"{ch}({i},{j}) {matrix[k][l]}({k},{l}) {dr},{dc}")
                            tdr = dr
                            tdc = dc
                            # Yuqoriga siljish
                            while i - dr >= 0 and 0 <= j - dc < col:
                                node = (i - dr, j - dc)
                                print(f"up {matrix[i-dr][j-dc]}{node}")
                                if node not in nodes:
                                    cnt += 1
                                    nodes.add(node)
                                dr += tdr
                                dc += tdc
                            dr = k - i
                            dc = l - j
                            # Pastga siljish
                            while k + dr < row and 0 <= l + dc < col:
                                node = (k + dr, l + dc)
                                print(f"down {matrix[k+dr][l+dc]}{node}")
                                if node not in nodes:
                                    cnt += 1
                                    nodes.add(node)
                                dr += tdr
                                dc += tdc

    print(list(nodes))
    return cnt


def part_one():
    matrix = read_input_data()
    row = len(matrix)
    col = len(matrix[0])
    cnt = 0
    print(f"{row}, {col}")
    nodes = set()  # Nodalarni takroran qo'shmaslik uchun to'plam
    for i in range(row):
        for j in range(col):
            ch = matrix[i][j]
            if ch != ".":  # Faqat belgi bor joylarni tekshirish
                for k in range(i, row):
                    for l in range(col):
                        if i == k and l <= j:
                            continue  # O'z-o'zini va ilgari tekshirilganlarni o'tkazib yuborish
                        if matrix[k][l] == ch:
                            dr = k - i
                            dc = l - j
                            print(f"{ch}({i},{j}) {matrix[k][l]}({k},{l}) {dr},{dc}")

                            # Yuqoriga siljish
                            if i - dr >= 0 and 0 <= j - dc < col:
                                node = (i - dr, j - dc)
                                print(f"up {matrix[i-dr][j-dc]}{node}")
                                if node not in nodes:
                                    cnt += 1
                                    nodes.add(node)

                            # Pastga siljish
                            if k + dr < row and 0 <= l + dc < col:
                                node = (k + dr, l + dc)
                                print(f"down {matrix[k+dr][l+dc]}{node}")
                                if node not in nodes:
                                    cnt += 1
                                    nodes.add(node)

    print(list(nodes))
    return cnt


def read_input_data():
    """
    Matritsani fayldan o'qiydi va massiv sifatida qaytaradi.
    """
    matrix = []
    with open("input.txt", "r") as file:
        for line in file:
            matrix.append(list(line.strip()))
    return matrix


print(part_one())
print(part_two())
