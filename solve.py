def problem1():
    # File reading and processing
    file_path = "sourse.txt"  # Replace with your file path

    # Initialize arrays
    array1 = []
    array2 = []

    # Read the file and split into two arrays
    with open(file_path, "r") as file:
        for line in file:
            # Split the line into two numbers and add to respective arrays
            num1, num2 = map(int, line.split())
            array1.append(num1)
            array2.append(num2)

    # Sort the arrays
    array1.sort()
    array2.sort()

    res = 0
    for i in range(len(array1)):
        res += abs(array1[i] - array2[i])

    summ = 0
    for arr1 in array1:
        cnt = 0
        for arr2 in array2:
            if arr1 == arr2:
                cnt += 1
        summ += arr1 * cnt
    return summ


def problem2():
    file_path = "report.txt"
    output_path = "rep.txt"
    cnt = 0

    with open(output_path, "w"):
        pass

    def by(l):
        with open(output_path, "a") as output_file:
            b = True
            if l[0] > l[1]:
                for i in range(len(l) - 1):
                    if not (l[i] > l[i + 1] and 1 <= l[i] - l[i + 1] <= 3):

                        b = False
                        break
            elif l[0] < l[1]:
                for i in range(len(l) - 1):
                    if not (l[i] < l[i + 1] and 1 <= l[i + 1] - l[i] <= 3):
                        b = False
                        break
            else:
                return 0  # Skip lines where l[0] == l[1]

            if b:
                output_file.write(line)
                return 1
            else:
                return 0

    # Clear the output file at the start
    try:
        with open(file_path, "r") as file:
            for line in file:
                l = line.split()
                try:
                    l = [int(x) for x in l]
                except ValueError:
                    continue  # Skip malformed lines

                if by(l) == 1:
                    cnt += 1
                else:
                    for i in range(len(l)):
                        if by(l[:i] + l[i + 1 :]) == 1:
                            cnt += 1
                            break
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    return cnt


def problem2_2():
    file_path = "report.txt"
    output_path = "rep.txt"
    results = []

    # Clear the output file at the start
    with open(output_path, "w"):
        pass

    try:
        with open(file_path, "r") as file, open(output_path, "a") as output_file:
            cnt = 0
            for line in file:
                l = line.split()
                try:
                    l = [int(x) for x in l]
                except ValueError:
                    results.append(f"{line.strip()}: Malformed data, skipped.\n")
                    continue  # Skip malformed lines

                # Check if the sequence is safe without removing any level
                if is_safe(l):
                    result = f"{line.strip()}: Safe without removing any level.\n"
                    results.append(result)
                    output_file.write(result)
                    cnt += 1
                else:
                    # Check if it's safe by removing one level
                    safe, removed_index = is_safe_by_removing_one_level(l)
                    if safe:
                        result = f"{line.strip()}: Safe by removing level {removed_index + 1}, {l[removed_index]}.\n"
                        results.append(result)
                        output_file.write(result)
                        cnt += 1
                    else:
                        result = f"{line.strip()}: Unsafe regardless of which level is removed.\n"
                        results.append(result)
                        output_file.write(result)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return results
    return cnt


def is_safe(sequence):
    """Check if the sequence is strictly increasing or decreasing with differences in [1, 3]."""
    increasing = all(
        1 <= sequence[i + 1] - sequence[i] <= 3 for i in range(len(sequence) - 1)
    )
    decreasing = all(
        1 <= sequence[i] - sequence[i + 1] <= 3 for i in range(len(sequence) - 1)
    )
    return increasing or decreasing


def is_safe_by_removing_one_level(sequence):
    """Check if the sequence becomes safe by removing one level."""
    for i in range(len(sequence)):
        modified_sequence = sequence[:i] + sequence[i + 1 :]
        if is_safe(modified_sequence):
            return True, i
    return False, -1


import re


def extract_numbers(expression):
    # Regexp to extract numbers inside mul(X,Y)
    pattern = r"mul\((\d+),(\d+)\)"
    match = re.match(pattern, expression)

    if match:
        # Extract first and second numbers
        num1, num2 = map(int, match.groups())
        return num1, num2
    else:
        return None


def extract_mul_expressions(file_path):
    # Regexp to extract all occurrences of mul(X,Y)
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = []
    mul = 0
    try:
        with open(file_path, "r") as file:
            for line in file:
                # Find all matches in the current line
                line_matches = re.findall(pattern, line)
                matches.extend(line_matches)

        if matches:
            print("Extracted mul expressions:")
            for match in matches:
                a, b = extract_numbers(match)
                if a and b:
                    mul += a * b
        else:
            print("No mul expressions found in the file.")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    print(mul)


# Replace 'input.txt' with your actual file path
# extract_mul_expressions("input.txt")


import re


def extract_valid_mul_expressions(file_path):
    # Regexp for mul(x, y), do(), and don't()
    mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    # State to track whether mul instructions are enabled or ignored
    enable_mul = True
    extracted_mul = []
    mul = 0

    try:
        with open(file_path, "r") as file:
            for line in file:
                segments = re.split(f"({do_pattern}|{dont_pattern})", line)
                for s in segments:
                    stripped_line = s.strip()

                    # Check for do() instruction
                    if re.match(do_pattern, stripped_line):
                        enable_mul = True
                        continue

                    # Check for don't() instruction
                    if re.match(dont_pattern, stripped_line):
                        enable_mul = False
                        continue

                    # Process mul(x, y) only if enable_mul is True
                    if enable_mul:
                        matches = re.findall(mul_pattern, stripped_line)
                        extracted_mul.extend(matches)
            for m in extracted_mul:
                a, b = extract_numbers(m)
                if a and b:
                    mul += a * b
            print(mul)

        return extracted_mul
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return []


# Replace 'input.txt' with your file path
# file_path = "input.txt"
# result = extract_valid_mul_expressions(file_path)


def xmas():
    file_path = "input.txt"
    with open(file_path, "r") as f:
        file = []
        for l in f:
            file.append(list(l))
        cnt = 0
        cnt2 = 0
        I = len(file) - 1
        for i in range(I + 1):
            J = len(file[i]) - 1
            for j in range(J + 1):
                if file[i][j] == "X":
                    # right
                    if j + 3 <= J:
                        if (
                            file[i][j + 1] == "M"
                            and file[i][j + 2] == "A"
                            and file[i][j + 3] == "S"
                        ):
                            cnt += 1
                    # left
                    if j >= 3:
                        if (
                            file[i][j - 1] == "M"
                            and file[i][j - 2] == "A"
                            and file[i][j - 3] == "S"
                        ):
                            cnt += 1
                    # up
                    if i >= 3:
                        if (
                            file[i - 1][j] == "M"
                            and file[i - 2][j] == "A"
                            and file[i - 3][j] == "S"
                        ):
                            cnt += 1
                    # down
                    if i + 3 <= I:
                        if (
                            file[i + 1][j] == "M"
                            and file[i + 2][j] == "A"
                            and file[i + 3][j] == "S"
                        ):
                            cnt += 1
                    # left up
                    if j >= 3 and i >= 3:
                        if (
                            file[i - 1][j - 1] == "M"
                            and file[i - 2][j - 2] == "A"
                            and file[i - 3][j - 3] == "S"
                        ):
                            cnt += 1
                    # right up
                    if j + 3 <= J and i >= 3:
                        if (
                            file[i - 1][j + 1] == "M"
                            and file[i - 2][j + 2] == "A"
                            and file[i - 3][j + 3] == "S"
                        ):
                            cnt += 1
                    # right down
                    if j + 3 <= J and i + 3 <= I:
                        if (
                            file[i + 1][j + 1] == "M"
                            and file[i + 2][j + 2] == "A"
                            and file[i + 3][j + 3] == "S"
                        ):
                            cnt += 1
                    # left down
                    if j >= 3 and i + 3 <= I:
                        if (
                            file[i + 1][j - 1] == "M"
                            and file[i + 2][j - 2] == "A"
                            and file[i + 3][j - 3] == "S"
                        ):
                            cnt += 1
                if file[i][j] == "A":
                    # four corner
                    if j >= 1 and i >= 1 and j + 1 <= J and i + 1 <= I:
                        if (
                            file[i - 1][j - 1] == "M"
                            and file[i + 1][j + 1] == "S"
                            or file[i - 1][j - 1] == "S"
                            and file[i + 1][j + 1] == "M"
                        ) and (
                            file[i - 1][j + 1] == "M"
                            and file[i + 1][j - 1] == "S"
                            or file[i - 1][j + 1] == "S"
                            and file[i + 1][j - 1] == "M"
                        ):
                            cnt2 += 1
        return cnt, cnt2


from colorama import Fore, Back, Style


def print_queue():
    file_path = "input.txt"
    ord_rule = []
    __ord = []
    print_line = []
    role = {}
    with open(file_path, "r") as file:
        for line in file:
            idx = line.rfind("|")
            if idx != -1:
                l = int(line[0:idx])
                r = int(line.strip()[idx + 1 :])
                __ord.append([l, r])
                if r in role:
                    role[r].append(l)
                else:
                    role[r] = [l]
            elif line.strip():
                print_line.append(list(map(int, line.strip().split(","))))
    print(f"{Fore.BLUE}{role}")
    # __ord.sort(reverse=True)
    print(f"{Fore.RED}{__ord} {Fore.RESET}")

    def check_role(l, r, ord_rule):
        ir = ord_rule.index(r)
        il = ord_rule.index(l)
        if il > ir:
            t = [l]
            if l in role:
                for r in role[l]:
                    if r in ord_rule[ir:il]:
                        t.append(r)
                        ord_rule.remove(r)
            ord_rule.remove(l)
            ord_rule = ord_rule[:ir] + t + ord_rule[ir:]
        return ord_rule

    for line in __ord:
        l = line[0]
        r = line[1]
        # if _ord.index(l) > _ord.index(r):
        #     print(f"{l}|{r}")
        print(ord_rule)

        if l in ord_rule:
            if r not in ord_rule:
                ord_rule.append(r)
                ord_rule = check_role(l, r, ord_rule)
            else:
                ord_rule = check_role(l, r, ord_rule)
        elif r in ord_rule:
            ord_rule.insert(ord_rule.index(r), l)
            ord_rule = check_role(l, r, ord_rule)
        else:
            ord_rule.append(l)
            ord_rule.append(r)
            ord_rule = check_role(l, r, ord_rule)
        for key, value in role.items():
            for v in value:
                if key in ord_rule and v in ord_rule:
                    if ord_rule.index(key) < ord_rule.index(v):
                        print(ord_rule)
                        print(f"{l}|{r} {key}")
    print(ord_rule)
    print(role)
    res = 0
    res2 = 0
    for line in print_line:
        t = []
        s = []
        for l in line:
            t.append(ord_rule.index(l))
            s.append(ord_rule.index(l))
        s.sort()
        m = int(len(t) / 2)
        if t == s:
            res += ord_rule[t[m]]
        else:
            res2 += ord_rule[s[m]]
    return res, res2


if __name__ == "__main__":
    print(print_queue())
