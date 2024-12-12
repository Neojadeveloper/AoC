def part_two():
    matrix = read_input_data()
    print(matrix)
    row = len(matrix)
    col = len(matrix[0])
    s = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                s += move(col, row, i, j, matrix)
    return s


def move(col, row, i, j, matrix):
    cnt = []  # 9-ga yetadigan yo'llar sonini saqlaydi
    visited = set()  # Tashrif buyurilgan hujayralarni saqlash

    def forward(col, row, i, j, u):
        if (
            i,
            j,
        ) in visited:  # Agar bu hujayraga avval tashrif buyurilgan bo'lsa, davom ettirmaymiz
            return
        visited.add((i, j))  # Hozirgi hujayrani tashrif qilingan deb belgilash

        print(f"{matrix[i][j]}({i},{j})")
        if matrix[i][j] == 9:  # Agar 9 ga yetgan bo'lsa
            cnt.append(1)
            print("---------")
            return

        k = 0
        while k < 4:
            if u == 0 and i - 1 >= 0 and matrix[i - 1][j] - matrix[i][j] == 1:
                forward(col, row, i - 1, j, 0)
            if u == 1 and j + 1 < col and matrix[i][j + 1] - matrix[i][j] == 1:
                forward(col, row, i, j + 1, 1)
            if u == 2 and i + 1 < row and matrix[i + 1][j] - matrix[i][j] == 1:
                forward(col, row, i + 1, j, 2)
            if u == 3 and j - 1 >= 0 and matrix[i][j - 1] - matrix[i][j] == 1:
                forward(col, row, i, j - 1, 3)
            u = (u + 1) % 4
            k += 1

    visited.clear()  # Har bir yangi boshlang'ich nuqta uchun tashriflarni tozalash
    forward(col, row, i, j, 0)
    print(len(cnt))
    return len(cnt)


def part_one():
    matrix = read_input_data()
    print(matrix)
    row = len(matrix)
    col = len(matrix[0])
    s = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                s += move(col, row, i, j, matrix)
    return s


def move(col, row, i, j, matrix):
    cnt = []

    def forvard(col, row, i, j, u):
        print(f"{matrix[i][j]}({i},{j})")
        if matrix[i][j] == 9:
            cnt.append(1)
            print("---------")
        k = 0
        while k < 4:
            if u == 0:
                if i - 1 >= 0 and matrix[i - 1][j] - matrix[i][j] == 1:
                    forvard(col, row, i - 1, j, 0)
            if u == 1:
                if j + 1 < col and matrix[i][j + 1] - matrix[i][j] == 1:
                    forvard(col, row, i, j + 1, 1)
            if u == 2:
                if i + 1 < row and matrix[i + 1][j] - matrix[i][j] == 1:
                    forvard(col, row, i + 1, j, 2)
            if u == 3:
                if j - 1 >= 0 and matrix[i][j - 1] - matrix[i][j] == 1:
                    forvard(col, row, i, j - 1, 3)
            u = (u + 1) % 4
            k += 1

    forvard(col, row, i, j, 0)
    print(len(cnt))
    return len(cnt)


def read_input_data():
    matrix = []
    with open("input.txt", "r") as file:
        for line in file:
            matrix.append(list(map(int, line.strip())))
    return matrix


print(part_one())
