def part_two():
    # Step 1: Read input data
    matrix, moves = read_input_data()

    # Step 2: Expand the warehouse map
    expanded_matrix = []
    for row in matrix:
        expanded_row = []
        for char in row:
            if char == "#":
                expanded_row.append("##")
            elif char == "O":
                expanded_row.append("[]")
            elif char == ".":
                expanded_row.append("..")
            elif char == "@":
                expanded_row.append("@.")
        expanded_matrix.append("".join(expanded_row))
    matrix = [list(row) for row in expanded_matrix]
    row, col = len(matrix), len(matrix[0])
    for line in matrix:
        print("".join(line))
    # Step 3: Locate the starting position of `@`
    cur = (0, 0)
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == "@":
                cur = (i, j)
                break

    i, j = cur  # Current position of `@`

    # Step 4: Define the movement logic
    def can_move(delta_i, delta_j):
        """Determine if @ and associated [] tiles can move."""
        ni, nj = i + delta_i, j + delta_j
        moving_objects = []
        while 0 <= ni < row and 0 <= nj < col and matrix[ni][nj] == "[":
            moving_objects.append((ni, nj))
            ni += delta_i
            nj += delta_j
        if 0 <= ni < row and 0 <= nj < col and matrix[ni][nj] == ".":
            return moving_objects, ni, nj
        if (
            len(moving_objects) == 0
            and 0 <= ni < row
            and 0 <= nj < col
            and matrix[ni][nj] == "."
        ):
            return [], ni, nj
        return None, None, None

    # Step 5: Execute moves
    for move in moves:
        if move == "^":
            moving_objects, ni, nj = can_move(-1, 0)
            if moving_objects is not None:
                for oi, oj in reversed(moving_objects):
                    matrix[oi][oj], matrix[oi - 1][oj] = ".", "["
                    matrix[oi][oj + 1], matrix[oi - 1][oj + 1] = ".", "]"
                matrix[i][j], matrix[i - 1][j] = ".", "@"
                matrix[i][j + 1], matrix[i - 1][j + 1] = ".", "."
                i -= 1
        elif move == ">":
            moving_objects, ni, nj = can_move(0, 2)
            if moving_objects is not None:
                for oi, oj in reversed(moving_objects):
                    matrix[oi][oj], matrix[oi][oj + 2] = ".", "["
                    matrix[oi][oj + 1], matrix[oi][oj + 3] = ".", "]"
                matrix[i][j], matrix[i][j + 2] = ".", "@"
                matrix[i][j + 1], matrix[i][j + 3] = ".", "."
                j += 2
        elif move == "v":
            moving_objects, ni, nj = can_move(1, 0)
            if moving_objects is not None:
                for oi, oj in reversed(moving_objects):
                    matrix[oi][oj], matrix[oi + 1][oj] = ".", "["
                    matrix[oi][oj + 1], matrix[oi + 1][oj + 1] = ".", "]"
                matrix[i][j], matrix[i + 1][j] = ".", "@"
                matrix[i][j + 1], matrix[i + 1][j + 1] = ".", "."
                i += 1
        elif move == "<":
            moving_objects, ni, nj = can_move(0, -2)
            if moving_objects is not None:
                for oi, oj in reversed(moving_objects):
                    matrix[oi][oj], matrix[oi][oj - 2] = ".", "["
                    matrix[oi][oj + 1], matrix[oi][oj - 1] = ".", "]"
                matrix[i][j], matrix[i][j - 2] = ".", "@"
                matrix[i][j + 1], matrix[i][j - 1] = ".", "."
                j -= 2
        print(move)
        for line in matrix:
            print("".join(line))
    # Step 6: Display the final matrix
    for line in matrix:
        print("".join(line))
    s = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == "[":
                s += 100 * i + j
    return s


def part_one():
    matrix, low = read_input_data()
    row = len(matrix)
    col = len(matrix[0])
    for line in matrix:
        print("".join(line))
    print(low)
    # Start joylashgan o'rnini topamiz
    cur = (0, 0)
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == "@":
                cur = (i, j)
                break

    i, j = cur  # `@`ning hozirgi o'rni

    # Harakatlarni ishlovchi funksiya
    for l in low:
        # Tekshirish uchun yordamchi funksiya
        def can_move(delta_i, delta_j):
            """@ va barcha O belgilarini harakatlantirish mumkinligini tekshirish."""
            ni, nj = i + delta_i, j + delta_j  # Birinchi tekshiriladigan joy
            moving_objects = []  # Harakatlanadigan elementlar
            while 0 <= ni < row and 0 <= nj < col and matrix[ni][nj] == "O":
                moving_objects.append((ni, nj))
                ni += delta_i
                nj += delta_j
            # Harakat qilish uchun oxirgi joy bo'sh (`.`) bo'lishi kerak
            if 0 <= ni < row and 0 <= nj < col and matrix[ni][nj] == ".":
                return moving_objects, ni, nj
            # Agar darhol `@` yonida faqat `.` bo'lsa, ham ruxsat beramiz
            if (
                len(moving_objects) == 0
                and 0 <= ni < row
                and 0 <= nj < col
                and matrix[ni][nj] == "."
            ):
                return [], ni, nj
            return None, None, None

        # Harakatlarni amalga oshirish
        if l == "^":  # Yuqoriga
            moving_objects, ni, nj = can_move(-1, 0)
            if moving_objects is not None:
                for oi, oj in reversed(moving_objects):  # O'larni harakatlantirish
                    matrix[oi][oj], matrix[oi - 1][oj] = ".", "O"
                matrix[i][j], matrix[i - 1][j] = ".", "@"
                i -= 1
        elif l == ">":  # O'ngga
            moving_objects, ni, nj = can_move(0, 1)
            if moving_objects is not None:
                for oi, oj in reversed(moving_objects):
                    matrix[oi][oj], matrix[oi][oj + 1] = ".", "O"
                matrix[i][j], matrix[i][j + 1] = ".", "@"
                j += 1
        elif l == "v":  # Pastga
            moving_objects, ni, nj = can_move(1, 0)
            if moving_objects is not None:
                for oi, oj in reversed(moving_objects):
                    matrix[oi][oj], matrix[oi + 1][oj] = ".", "O"
                matrix[i][j], matrix[i + 1][j] = ".", "@"
                i += 1
        elif l == "<":  # Chapga
            moving_objects, ni, nj = can_move(0, -1)
            if moving_objects is not None:
                for oi, oj in reversed(moving_objects):
                    matrix[oi][oj], matrix[oi][oj - 1] = ".", "O"
                matrix[i][j], matrix[i][j - 1] = ".", "@"
                j -= 1
    # Yakuniy matritsani ekranga chiqaramiz
    for line in matrix:
        print("".join(line))
    s = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == "O":
                s += 100 * i + j
    return s


def read_input_data():
    # Misol ma'lumot (real holatda fayldan o'qish kerak)
    data = open("input.txt").read()
    head, low = data.split("\n\n")
    matrix = [list(line) for line in head.split("\n") if line]
    return matrix, list(low.replace("\n", ""))


# print(part_one())
print(part_two())
