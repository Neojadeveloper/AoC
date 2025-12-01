import os

def part_one():
    dial = 50
    cnt = 0

    for raw in rows():
        direction = raw[0].upper()
        try:
            steps = int(raw[1:])
        except ValueError:
            # skip malformed lines
            continue

        if direction == "R":
            dial = (dial + steps) % 100
        else:
            dial = (dial - steps) % 100

        if dial == 0:
            cnt += 1

    print(cnt)
def part_two():
    """
    Count every time the dial passes through or lands on 0 during rotation.
    Method 0x434C49434B (CLICK) - count all clicks through 0.
    """
    dial = 50
    cnt = 0

    for raw in rows():
        direction = raw[0].upper()
        try:
            steps = int(raw[1:])
        except ValueError:
            continue
        for _ in range(steps):
            if direction == "R":
                dial = (dial + 1) % 100
            else:
                dial = (dial - 1) % 100
            
            if dial == 0:
                cnt += 1

    print(cnt)
    
def rows():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(dir_path, "input.txt")
    list_lines = []
    with open(input_path, "r") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            list_lines.append(line)
    return list_lines
if __name__ == "__main__":
    part_one()
    part_two()