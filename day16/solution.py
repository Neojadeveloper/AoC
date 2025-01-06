def part_one():
    # Xarita
    matrix = read_input_data()

    row, col = len(matrix), len(matrix[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # (up, right, down, left)

    # Boshlanish va maqsad nuqtasi
    start = (row - 2, 1)  # S koordinatasi
    goal = (1, col - 2)  # E koordinatasi

    all_paths = []  # Barcha yo'llar va ularning quvvatlari

    # Stack va boshlang'ich qiymat
    stack = [(start, [], None, 0)]  # (joriy nuqta, yo'l, oldingi yo'nalish, quvvat)

    while stack:
        (x, y), path, prev_direction, power = stack.pop()
        current_path = path + [(x, y)]
        print(f"Yo'l: Quvvat = {power}, Yo'l = {current_path}")
        # Maqsadga yetganimizni tekshirish
        if (x, y) == goal:
            all_paths.append((current_path, power))
            print(f"ooooo Yo'l: Quvvat = {power}, Yo'l = {current_path}")
            continue

        # Har bir yo'nalishni tekshirish
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            direction = (dx, dy)

            if (
                0 <= nx < row
                and 0 <= ny < col
                and matrix[nx][ny] in [".", "E"]
                and (nx, ny) not in path
            ):
                # Quvvatni hisoblash
                if direction == prev_direction:  # To'g'ri yo'nalishda harakat
                    new_power = power + 1
                else:  # 90 gradusga burilish
                    new_power = power + 1000 + 1

                stack.append(((nx, ny), current_path, direction, new_power))

    # Natijalarni chiqarish
    print(f"Barcha yo'llar soni: {len(all_paths)}")
    for i, (path, power) in enumerate(all_paths, 1):
        print(f"Yo'l {i}: Quvvat = {power}, Yo'l = {path}")

    # Eng optimal yo'lni topish
    if all_paths:
        min_path = min(all_paths, key=lambda x: x[1])
        print(f"Eng optimal yo'l: Quvvat = {min_path[1]}, Yo'l = {min_path[0]}")
    else:
        print("Hech qanday yo'l topilmadi")


def read_input_data():
    # Misol ma'lumot (real holatda fayldan o'qish kerak)
    data = open("input.txt").read()
    return [list(line) for line in data.split("\n")]


print(part_one())
# print(part_two())
