def part_two():
    towels, towel_sets = read_input_data()
    # print(towels, towel_sets)
    cnt = 0
    memo = {}
    for towel_set in towel_sets:
        l = cnt_make_line(towel_set, towels, memo)
        if l > 0:
            cnt += l
    print(cnt)


def cnt_make_line(line, rules, memo):
    """
    Liniyani qoidalarga bo'lib bo'lish mumkinligini memoizatsiya bilan tekshiradi.
    """
    print(f"memo - {memo}")
    if line in memo:  # Memoizatsiyani tekshirish
        return memo[line]

    if not line:  # Bo'sh string bo'lsa, ha
        return 1
    cnt = 0
    for rule in rules:  # Uzunlik bo'yicha tartiblangan qoidalar
        if line.startswith(rule):
            cnt += cnt_make_line(line[len(rule) :], rules, memo)
    memo[line] = cnt
    return cnt


def part_one():
    towels, towel_sets = read_input_data()
    # print(towels, towel_sets)
    cnt = 0
    memo = {}
    for towel_set in towel_sets[0:1]:
        if cnt_make_line(towel_set, towels, memo):
            cnt += 1
    print(cnt)


def can_make_line(line, rules, memo):
    """
    Liniyani qoidalarga bo'lib bo'lish mumkinligini memoizatsiya bilan tekshiradi.
    """
    print(line)
    if line in memo:  # Memoizatsiyani tekshirish
        return memo[line]

    if not line:  # Bo'sh string bo'lsa, ha
        return True

    for rule in sorted(
        rules, key=len, reverse=True
    ):  # Uzunlik bo'yicha tartiblangan qoidalar
        if line.startswith(rule):
            # Qolgan substringni rekursiv tekshirish
            if can_make_line(line[len(rule) :], rules, memo):
                memo[line] = True
                return True

    memo[line] = False  # Qoidalarga mos kelmasa
    return False


def read_input_data():
    data = open("input.txt").read()
    towels, towel_sets = data.split("\n\n")
    towels = sorted(
        [towel.strip() for towel in towels.split(",")], reverse=True, key=len
    )
    towel_sets = [towel_set.strip() for towel_set in towel_sets.split("\n")]
    return towels, towel_sets


part_two()
