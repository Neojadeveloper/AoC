import os

def part_one():
    total = 0
    res = 0
    matrix = rows()
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == "@":
                if i - 1 >= 0 and j-1 >= 0 and matrix[i-1][j-1] == "@": # top-left
                    total += 1
                if i - 1 >= 0 and matrix[i-1][j] == "@": # top
                    total += 1
                if j+1 < col and i - 1 >= 0 and matrix[i-1][j+1] == "@": # top-right
                    total += 1
                if j+1 < col and matrix[i][j+1] == "@": # right
                    total += 1
                if j+1 < col and i + 1 < row and matrix[i+1][j+1] == "@": # bottom-right
                    total += 1
                if i + 1 < row and matrix[i+1][j] == "@": # bottom
                    total += 1
                if i + 1 < row and j-1 >= 0 and matrix[i+1][j-1] == "@": # bottom-left
                    total += 1
                if j-1 >= 0 and matrix[i][j-1] == "@": # left
                    total += 1
                if total < 4 :
                    print(f"i: {i}, j: {j}, total: {total}")
                    res+=1
            total = 0
    print(res)
    
def forklift(matrix):
    total = 0
    res = 0
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == "@":
                if i - 1 >= 0 and j-1 >= 0 and matrix[i-1][j-1] == "@": # top-left
                    total += 1
                if i - 1 >= 0 and matrix[i-1][j] == "@": # top
                    total += 1
                if j+1 < col and i - 1 >= 0 and matrix[i-1][j+1] == "@": # top-right
                    total += 1
                if j+1 < col and matrix[i][j+1] == "@": # right
                    total += 1
                if j+1 < col and i + 1 < row and matrix[i+1][j+1] == "@": # bottom-right
                    total += 1
                if i + 1 < row and matrix[i+1][j] == "@": # bottom
                    total += 1
                if i + 1 < row and j-1 >= 0 and matrix[i+1][j-1] == "@": # bottom-left
                    total += 1
                if j-1 >= 0 and matrix[i][j-1] == "@": # left
                    total += 1
                if total < 4 :
                    print(f"i: {i}, j: {j}, total: {total}, type: {type(matrix[i][j])}")
                    res+=1
                    matrix[i][j] = "#"
            total = 0
    return res
def part_two():
    res = 0
    matrix = rows()
    while True:
        val = forklift(matrix)
        if val == 0:
            break
        res += val
    print(res)

def rows():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(dir_path, "input.txt")
    list_lines = []
    with open(input_path, "r") as f:
        for raw in f:
            # String'ni list'ga aylantiramiz
            list_lines.append(list(raw.strip()))
    return list_lines
if __name__ == "__main__":
    #part_one()
    part_two()