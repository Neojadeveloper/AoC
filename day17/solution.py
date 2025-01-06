data = open("input.txt").read()
register, operations = data.split("\n\n")
operations = list(map(int, operations.split(":")[1].strip().split(",")))
A, B, C = [int(register.split(":")[1].strip()) for register in register.split("\n")]
l = len(operations)
print(operations)


"""
0 (adv): Bu instruktsiya A ro'yxatidagi sonni 2^operand ga bo'lishni amalga oshiradi. Natija A ro'yxatiga yoziladi.
1 (bxl): B ro'yxatidagi sonni operandga bitwise XOR (bittik XOR) qilish.
2 (bst): Operandni 8 ga bo'lib qoldiqni hisoblash va B ro'yxatiga yozish.
3 (jnz): Agar A ro'yxatidagi son 0 bo'lmasa, berilgan operandga ko'ra programmada yopish (jump) qiladi.
4 (bxc): B ro'yxatidagi sonni C ro'yxatidagi son bilan XOR qilish.
5 (out): Operandni 8 ga bo'lib qoldiqni hisoblash va ekranga chiqarish.
6 (bdv): A ro'yxatidagi sonni 2^operand ga bo'lish va natijani B ro'yxatiga yozish.
7 (cdv): A ro'yxatidagi sonni 2^operand ga bo'lish va natijani C ro'yxatiga yozish.
"""
i = 0
s = []
while i < l:
    c = operations[i]
    j = operations[i + 1]
    o = j if 0 <= j < 4 else A if j == 4 else B if j == 5 else C if j == 6 else -1

    if c == 0:
        A = A // 2**o
    elif c == 1:
        B = B ^ j
    elif c == 2:
        B = o % 8
    elif c == 3 and A != 0:
        i = j
        continue
    elif c == 4:
        B = B ^ C
    elif c == 5:
        s.append(o % 8)
    elif c == 6:
        B = A // 2**o
    elif c == 7:
        C = A // 2**o
    i += 2
    # print(f"c={c} j={j} o={o} A={A} B={B} C={C} s={s}")
for val in s:
    print(val, end=",")


def calc(A, operations):
    B, C = 0, 0
    s = []  # out qiymatlari
    i = 0
    while i < len(operations):
        c = operations[i]  # opcode
        j = operations[i + 1]  # operand
        o = j if 0 <= j < 4 else A if j == 4 else B if j == 5 else C if j == 6 else -1

        if c == 0:  # adv
            A //= 2**o
        elif c == 1:  # bxl
            B ^= j
        elif c == 2:  # bst
            B = o % 8
        elif c == 3:  # jnz
            if A != 0:
                i = j
                continue
        elif c == 4:  # bxc
            B ^= C
        elif c == 5:  # out
            s.append(o % 8)
        elif c == 6:  # bdv
            B = A // 2**o
        elif c == 7:  # cdv
            C = A // 2**o
        i += 2
    return s


curr = [(1, 0)]
for i, a in curr:
    for a in range(a, a + 8):
        if calc(a, operations) == operations[-i:]:
            curr.append((i + 1, a * 8))
            if i == len(operations):
                print(a)
