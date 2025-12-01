def part_two():
    stones = read_input_data()
    print(stones)
    cnt = 0
    memo = {}
    for stone in stones:
        cnt += stones_cnt(stone, memo, 75)
    return cnt


def stones_cnt(n, memo, blink):
    if blink == 0:
        return 1
    if (n, blink) in memo:
        return memo[(n, blink)]

    _stones = []
    if n == 0:
        _stones.append(1)
    else:
        n_str = str(n)
        if len(n_str) % 2 == 0:
            mid = len(n_str) // 2
            _stones.append(int(n_str[:mid]))
            _stones.append(int(n_str[mid:]))
        else:
            _stones.append(n * 2024)

    cnt = sum(stones_cnt(stone, memo, blink - 1) for stone in _stones)

    memo[(n, blink)] = cnt
    return cnt


def part_one():
    stones = read_input_data()
    _stones = []
    print(stones)
    for j in range(25):
        for i in range(len(stones)):
            if stones[i] == 0:
                _stones.append(1)
            elif len(str(stones[i])) % 2 == 0:
                _stones.append(int(str(stones[i])[0 : len(str(stones[i])) // 2]))
                _stones.append(int(str(stones[i])[len(str(stones[i])) // 2 :]))
            else:
                _stones.append(stones[i] * 2024)
        stones = _stones
        _stones = []
        print(stones)
    return len(stones)


def read_input_data():
    with open("input.txt", "r") as file:
        for line in file:
            return list(map(int, line.strip().split(" ")))


print(part_one())
print(part_two())
