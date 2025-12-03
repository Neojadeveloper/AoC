import os

def part_one():
    total = 0

    for raw in rows():
        print(raw)
        max_pair = ""
        for i in range(len(raw)):
            for j in range(i + 1, len(raw)):
                pair = raw[i] + raw[j]
                if pair > max_pair:
                    max_pair = pair
        total += int(max_pair)
    print(total)

def max_k_digits(s, k):
    n = len(s)
    result = []
    pos = 0
    
    for digit_num in range(k):
        # Qolgan joylar uchun yetarli raqam qolishi kerak
        remaining_digits = k - digit_num - 1
        last_valid_pos = n - remaining_digits - 1
        
        # pos dan last_valid_pos gacha eng katta raqamni topamiz
        best_char = ''
        best_pos = pos
        
        for i in range(pos, last_valid_pos + 1):
            if s[i] > best_char:
                best_char = s[i]
                best_pos = i
            # Agar '9' topsak, bundan kattasi yo'q
            if best_char == '9':
                break
        
        result.append(best_char)
        pos = best_pos + 1
    
    return ''.join(result)

def part_two():
    total = 0
    for raw in rows():
        result = max_k_digits(raw.strip(), 12)
        print(f"{raw} -> {result}")
        total += int(result)
    print(f"Total: {total}")
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