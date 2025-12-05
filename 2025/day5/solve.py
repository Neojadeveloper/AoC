import os

def part_one():
    total = 0
    row, ids = rows()
    for id in ids:
        for r in row:
            first, second = r.split("-")
            if int(first) <= int(id) <= int(second):
                total += 1
                break
    print(total)

def part_two():
    total = 0
    ranges, _ = rows()
    
    # Range'larni [start, end] formatiga o'tkazamiz
    intervals = []
    for r in ranges:
        first, second = r.split("-")
        intervals.append([int(first), int(second)])
    
    # Start bo'yicha tartiblash
    intervals.sort(key=lambda x: x[0])
    
    # Range'larni birlashtirish
    merged = [intervals[0]]
    print(intervals)
    for start, end in intervals[1:]:
        last = merged[-1]
        if start <= last[1] + 1:  # Overlap yoki tutash
            last[1] = max(last[1], end)
        else:
            merged.append([start, end])
    
    # Har bir range'dagi ID'lar sonini hisoblash
    for start, end in merged:
        total += end - start + 1
    
    print(total)
def rows():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(dir_path, "input.txt")
    fresh_range = []
    ids = []
    with open(input_path, "r") as f:
        for raw in f:
            raw  = raw.strip()
            if not raw:
                continue
            if '-' in raw:
                fresh_range.append(raw)
            else:                
                ids.append(raw)
    return fresh_range, ids
if __name__ == "__main__":
    part_one()
    part_two()