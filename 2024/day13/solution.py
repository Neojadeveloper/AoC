import re


def part_two():
    # Button A: X+94, Y+34
    # Button B: X+22, Y+67
    # Prize: X=8400, Y=5400
    matrix = parse_coordinates()
    S = 0
    for line in matrix:
        A = (line[3] * add(line[4]) - line[2] * add(line[5])) / (
            line[3] * line[0] - line[1] * line[2]
        )
        B = (add(line[4]) - A * line[0]) / line[2]
        if A.is_integer() and B.is_integer() and A > 0 and B > 0:
            S += 3 * A + B
            print(f"{A} {B}")
    return S


def add(x):
    # 10 000 000 000 000
    str_x = str(x)
    return int(f"1{"0"*(13-len(str_x))}{str_x}")


def part_one():
    # Button A: X+94, Y+34
    # Button B: X+22, Y+67
    # Prize: X=8400, Y=5400
    matrix = parse_coordinates()
    S = 0
    for line in matrix:
        A = (line[3] * line[4] - line[2] * line[5]) / (
            line[3] * line[0] - line[1] * line[2]
        )
        B = (line[4] - A * line[0]) / line[2]
        if A.is_integer() and B.is_integer():
            S += 3 * A + B
            print(f"{A} {B}")
    return S


def parse_coordinates():
    pattern = r"Button A: X\+(\d+), Y\+(\d+)\s+Button B: X\+(\d+), Y\+(\d+)\s+Prize: X=(\d+), Y=(\d+)"

    data = open("input.txt", "r").read()
    matches = re.findall(pattern, data)

    result = []
    for match in matches:
        result.append(
            (
                int(match[0]),
                int(match[1]),
                int(match[2]),
                int(match[3]),
                int(match[4]),
                int(match[5]),
            )
        )

    return result


print(int(part_one()))
print(int(part_two()))
