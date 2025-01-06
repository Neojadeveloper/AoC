from collections import deque


def part_one():
    koor = read_input_data()
    print(koor)

    l = 71
    byte = 1024
    matrix = [list("." * l) for _ in range(l)]

    for b in range(byte):
        i = koor[b][0]
        j = koor[b][1]
        matrix[i][j] = "#"
    for m in matrix:
        print("".join(m))
    print(min_path(matrix, (l - 1, l - 1), (0, 0)))


def part_two():
    koor = read_input_data()
    print(koor)

    l = 71
    byte = len(koor)
    matrix = [list("." * l) for _ in range(l)]

    for b in range(byte):
        i = koor[b][0]
        j = koor[b][1]
        matrix[i][j] = "#"
        p = min_path(matrix, (l - 1, l - 1), (0, 0))
        if p:
            print(p)
        else:
            print(koor[b])
            break
    for m in matrix:
        print("".join(m))


def min_path(matrix, goal, start):
    l = len(matrix)
    queue = deque([start])
    visted = set()
    dirict = [(-1, 0), (0, 1), (0, -1), (1, 0)]  # up, right, down, left
    step = 0
    while queue:
        for _ in range(len(queue)):
            i, j = queue.popleft()
            if (i, j) == goal:
                return step
            for di, dj in dirict:
                ni, nj = i + di, j + dj
                if (
                    0 <= ni < l
                    and 0 <= nj < l
                    and (ni, nj) not in visted
                    and matrix[ni][nj] == "."
                ):
                    queue.append((ni, nj))
                    visted.add((ni, nj))
        step += 1
    return None


def read_input_data():
    with open("input.txt") as f:
        return [tuple(map(int, line.strip().split(","))) for line in f]


part_two()
