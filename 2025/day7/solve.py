import os

def part_one():
    total = 0
    matrix = rows()
    m = len(matrix)
    n = len(matrix[0])
    beams = [0] * n
    for r in range(m):
        for c in range(n):
            cell = matrix[r][c]
            if cell == "S":
                beams[c] += 1
            elif cell == "^":
                if beams[c] > 0:
                    print(f"Row {r}, Col {c}: Beams before split: {beams[c]}")
                    total += 1
                    beam_count = beams[c]
                    beams[c] = 0
                    if c - 1 >= 0:
                        beams[c - 1] += beam_count
                    if c + 1 < n:
                        beams[c + 1] += beam_count
    print(total)

def part_two():
    matrix = rows()
    m = len(matrix)
    n = len(matrix[0])
    
    # S pozitsiyasini topamiz
    start_col = -1
    for c in range(n):
        if matrix[0][c] == 'S':
            start_col = c
            break
    
    # BFS/DFS - har bir yo'lni kuzatamiz
    # State: (row, col, path_id)
    # Har safar split bo'lganda yangi path yaratamiz
    
    timelines = 0
    stack = [(0, start_col)]  # (row, col)
    paths = {(0, start_col): 1}  # (row, col): timeline_count
    
    for r in range(m):
        new_paths = {}
        for c in range(n):
            if (r, c) not in paths:
                continue
            
            count = paths[(r, c)]
            cell = matrix[r][c]
            
            if cell == "^":
                # Split - har bir timeline 2 ga bo'linadi
                if c - 1 >= 0 and r + 1 < m:
                    new_paths[(r + 1, c - 1)] = new_paths.get((r + 1, c - 1), 0) + count
                if c + 1 < n and r + 1 < m:
                    new_paths[(r + 1, c + 1)] = new_paths.get((r + 1, c + 1), 0) + count
            else:  # "." or "S"
                # Pastga davom
                if r + 1 < m:
                    new_paths[(r + 1, c)] = new_paths.get((r + 1, c), 0) + count
                else:
                    # Pastga chiqish - bu timeline tugadi
                    timelines += count
        
        paths = new_paths
    
    # Oxirgi qatorda qolgan barcha timeline'lar
    timelines += sum(paths.values())
    
    print(timelines)

def rows():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(dir_path, "input.txt")
    matrix = []
    with open(input_path, "r") as f:
        for raw in f:
            raw  = raw.strip()
            matrix.append(raw)
    return matrix
if __name__ == "__main__":
    #print(rows())
    part_one()
    part_two()