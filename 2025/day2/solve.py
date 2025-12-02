import os

def part_one():
    total = 0

    for raw in rows():
        print(raw)
        first, second = raw.split("-")
        for i in range(int(first), int(second) + 1):
            s = str(i)
            if len(s) % 2 != 0:
                continue
            half = len(s) // 2
            if s[:half] == s[half:]:
                total += i
                print(f"Invalid: {s}")
    print(total)
def part_two():
    total = 0

    for raw in rows():
        print(raw)
        first, second = raw.split("-")
        for i in range(int(first), int(second) + 1):
            s = str(i)
            if is_invalid(s):
                total += i
                print(f"Invalid: {s}")
    print(total)

def is_invalid(s):
    n = len(s)
    for pattern_len in range(1, n // 2 + 1):
        if n % pattern_len != 0:
            continue
        pattern = s[:pattern_len]
        repeat_count = n // pattern_len
        if pattern * repeat_count == s:
            return True
    return False
def rows():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(dir_path, "input.txt")
    list_lines = []
    with open(input_path, "r") as f:
        for raw in f:
            for line in raw.strip().split(","):
                if not line:
                    continue
                # print(line)
                list_lines.append(line)
    return list_lines
if __name__ == "__main__":
    part_one()
    part_two()