import os

def part_one():
    total = 0
    lines = rows()
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            a, b = lines[i].split(",")
            c, d = lines[j].split(",")
            area = abs((int(b)-int(d)+1)*(int(a)-int(c)+1))
            if area > total:
                total = area
    print(total)

def part_two():
    lines = rows()
    greens = set()
    for i in range(0, len(lines), 2):
        a,b = lines[i].split(",")
        c,d = lines[i+1].split(",")
        if a == c:
            for y in range(min(int(b), int(d)), max(int(b), int(d))+1):
                greens.add((int(a), y))
        elif b == d:
            for x in range(min(int(a), int(c)), max(int(a), int(c))+1):
                greens.add((x, int(b)))
    greens = sorted(greens)
    print(greens)
def rows():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(dir_path, "input.txt")
    lines = []
    with open(input_path, "r") as f:
        for raw in f:
            raw = raw.strip()
            if raw:
                lines.append(raw)
    return lines

if __name__ == "__main__":
    part_one()
    part_two()