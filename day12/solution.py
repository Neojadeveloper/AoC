def part_two():
    matrix = read_input_data()
    if not matrix or not matrix[0]:  # Bo'sh yoki noto'g'ri matritsa holatini tekshirish
        return {}

    row = len(matrix)
    col = len(matrix[0])
    visited = set()
    s = 0
    for i in range(row):
        for j in range(col):
            sides = set()
            if (i, j) not in visited:  # Agar hujayraga hali tashrif buyurilmagan bo'lsa
                cnt = go_side(matrix, i, j, visited, sides)
                s += cnt * calculate_shape_corners(sides)
                print(f"{matrix[i][j]} {cnt} {calculate_shape_corners(sides)} {sides}")
    return s


def go_side(matrix, i, j, visited, sides):
    row = len(matrix)
    col = len(matrix[0])
    c = matrix[i][j]

    # Tashrif buyurilgan joyni belgilash
    visited.add((i, j))
    sides.add((i, j))
    cnt = 1
    # Yo'nalishlar (yuqori, o'ng, past, chap)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for di, dj in directions:
        ni, nj = i + di, j + dj

        # Koordinata doirada va hali tashrif buyurilmagan bo'lsa
        if (
            0 <= ni < row
            and 0 <= nj < col
            and matrix[ni][nj] == c
            and (ni, nj) not in visited
        ):
            new_cnt = go_side(matrix, ni, nj, visited, sides)
            cnt += new_cnt

    return cnt


def calculate_shape_corners(points):
    points_set = set(
        points
    )  # Qidirishni tezlashtirish uchun nuqtalarni to'plamga aylantiramiz
    corners = 0

    # Qo'shni yo'nalishlar: yuqori, o'ng, past, chap
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for x, y in points:
        # Har bir nuqtaning qo'shnilarini topamiz
        neighbors = [(x + dx, y + dy) for dx, dy in directions]
        connected_neighbors = [n for n in neighbors if n in points_set]

        # Agar qo'shnilarning soni 2 dan kam yoki shakl yo'nalishi o'zgarsa, burchak deb hisoblaymiz
        if (
            len(connected_neighbors) != 2
        ):  # 2 dan ko'p yoki kam qo'shni bo'lsa, burchak bo'ladi
            corners += 1

    return corners


def side(sides, matrix):
    cnt = 0
    row = len(matrix)
    col = len(matrix[0])
    for side in sides:
        for _side in sides:
            if _side == side:
                continue

    return cnt


def part_one():
    matrix = read_input_data()
    if not matrix or not matrix[0]:  # Bo'sh yoki noto'g'ri matritsa holatini tekshirish
        return {}

    row = len(matrix)
    col = len(matrix[0])
    visited = set()  # Tashrif buyurilgan yo'llarni saqlash uchun
    s = 0
    for i in range(row):
        for j in range(col):
            if (i, j) not in visited:  # Agar hujayraga hali tashrif buyurilmagan bo'lsa
                cnt, peri = go(matrix, i, j, visited)
                s += cnt * peri
                print(f"{matrix[i][j]} {cnt} {peri}")
    return s


def go(matrix, i, j, visited):
    row = len(matrix)
    col = len(matrix[0])
    c = matrix[i][j]

    # Tashrif buyurilgan joyni belgilash
    visited.add((i, j))

    cnt, peri = 1, perimeter(matrix, i, j)

    # Yo'nalishlar (yuqori, o'ng, past, chap)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for di, dj in directions:
        ni, nj = i + di, j + dj

        # Koordinata doirada va hali tashrif buyurilmagan bo'lsa
        if (
            0 <= ni < row
            and 0 <= nj < col
            and matrix[ni][nj] == c
            and (ni, nj) not in visited
        ):
            new_cnt, new_peri = go(matrix, ni, nj, visited)
            cnt += new_cnt
            peri += new_peri

    return cnt, peri


def perimeter(matrix, i, j):
    cnt = 0
    cur = matrix[i][j]
    row = len(matrix)
    col = len(matrix[0])

    # Qo'shnilarni tekshirish
    neighbors = [
        (i - 1, j),  # Yuqori
        (i, j + 1),  # O'ng
        (i + 1, j),  # Past
        (i, j - 1),  # Chap
    ]

    for ni, nj in neighbors:
        if ni < 0 or ni >= row or nj < 0 or nj >= col or matrix[ni][nj] != cur:
            cnt += 1
    return cnt


def read_input_data():
    matrix = []
    with open("input.txt", "r") as file:
        for line in file:
            matrix.append(list(line.strip()))
    return matrix


# print(part_one())
print(part_two())
