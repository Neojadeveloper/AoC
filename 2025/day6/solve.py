from ast import operator
import math
import os

def part_one():
    total = 0
    matrix, _ = rows()
    n = len(matrix[0])
    m = len(matrix)
    for r in range(n):
        if matrix[m-1][r] == "*":
            temp = 1
            for i in range(m-1):
                temp *= int(matrix[i][r])
            total += temp
        else:
            temp = 0
            for i in range(m-1):
                temp += int(matrix[i][r])
            total += temp

    print(total)

def part_two():
    total = 0
    _ , matrix = rows()
    n = len(matrix[0])
    m = len(matrix)
    for row in matrix:
        print(row)
    safalopod = []
    for r in range(n,-1,-1):
        s = ""
        for i in range(m-1):
            p = matrix[i][r-1:r].strip()
            if p:
                s += p
        if s:
            safalopod.append(s)
        print(safalopod)
        operator = matrix[m-1][r-1:r].strip()
        print(operator)
        if operator: 
            temp = 0
            if operator == "+":
                for i in safalopod:
                    temp+= int(i)
            if operator == "*":
                temp = 1
                for i in safalopod:
                    temp*= int(i)    
            total += temp
            operator = matrix[m-1][r-1:r]
            safalopod = []
    print(total)

def rows():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(dir_path, "input.txt")
    matrix_one = []
    matrix_two = []
    with open(input_path, "r") as f:
        for raw in f:
            raw  = raw.rstrip("\n")
            matrix_two.append(raw)
            raw = raw.split(" ")
            _ = []
            for r in raw:
                if r:
                    _.append(r)
            matrix_one.append(_)
    return matrix_one, matrix_two
if __name__ == "__main__":
    part_one()
    part_two()