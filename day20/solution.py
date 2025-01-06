from collections import deque, defaultdict
from itertools import combinations
from functools import lru_cache


def is_valid_cheat_point(matrix, i, j):
    """Check if wall can be a valid cheat point"""
    row, col = len(matrix), len(matrix[0])
    # Check horizontal .#.
    if j > 0 and j < col - 1 and matrix[i][j - 1] == "." and matrix[i][j + 1] == ".":
        return True
    # Check vertical
    if i > 0 and i < row - 1 and matrix[i - 1][j] == "." and matrix[i + 1][j] == ".":
        return True
    return False


def find_shortest_path(matrix, start, end, cheat_point=None):
    """Find shortest path length, with optional cheat point"""
    row, col = len(matrix), len(matrix[0])
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        (i, j), steps = queue.popleft()
        if (i, j) == end:
            return steps

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if not (0 <= ni < row and 0 <= nj < col):
                continue
            if (ni, nj) in visited:
                continue
            # Can pass if empty or is cheat point
            if matrix[ni][nj] == "." or (ni, nj) == cheat_point:
                visited.add((ni, nj))
                queue.append(((ni, nj), steps + 1))
    return float("inf")


def find_all_cheats(matrix, start, end):
    row, col = len(matrix), len(matrix[0])
    normal_length = find_shortest_path(matrix, start, end)
    cheat_results = defaultdict(int)

    # Try each wall as potential cheat
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == "#" and is_valid_cheat_point(matrix, i, j):
                length_with_cheat = find_shortest_path(matrix, start, end, (i, j))
                if length_with_cheat < normal_length:
                    steps_saved = normal_length - length_with_cheat
                    cheat_results[steps_saved] += 1

    return cheat_results


def part_one():
    matrix = [list(line.strip()) for line in open("input.txt")]
    start = end = None

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "S":
                start = (i, j)
                matrix[i][j] = "."
            elif matrix[i][j] == "E":
                end = (i, j)
                matrix[i][j] = "."

    cheat_results = find_all_cheats(matrix, start, end)
    cnt = 0
    for steps, count in sorted(cheat_results.items()):
        print(f"Steps saved: {steps}, Count: {count}")
        if steps >= 100:
            cnt += count
    print(cnt)


def find_shortest_path_multi(matrix, start, end, cheat_points):
    """Find shortest path using multiple cheat points"""
    row, col = len(matrix), len(matrix[0])
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        (i, j), steps = queue.popleft()
        if (i, j) == end:
            return steps

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if not (0 <= ni < row and 0 <= nj < col):
                continue
            if (ni, nj) in visited:
                continue
            if matrix[ni][nj] == "." or (ni, nj) in cheat_points:
                visited.add((ni, nj))
                queue.append(((ni, nj), steps + 1))
    return float("inf")


def find_valid_cheat_points(matrix):
    """Find all valid cheat points in matrix"""
    row, col = len(matrix), len(matrix[0])
    valid_points = []

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == "#" and is_valid_cheat_point(matrix, i, j):
                valid_points.append((i, j))

    return valid_points


@lru_cache(maxsize=None)
def find_shortest_path_cached(matrix, start, end, cheat_points=None):
    """Cached version of shortest path finding"""
    if cheat_points is None:
        cheat_points = frozenset()

    # Bidirectional BFS
    forward_queue = deque([(start, 0)])
    backward_queue = deque([(end, 0)])
    forward_visited = {start: 0}
    backward_visited = {end: 0}
    best_length = float("inf")

    while forward_queue and backward_queue:
        # Process forward
        pos, steps = forward_queue.popleft()
        if pos in backward_visited:
            best_length = min(best_length, steps + backward_visited[pos])
            continue

        # Process backward
        end_pos, end_steps = backward_queue.popleft()
        if end_pos in forward_visited:
            best_length = min(best_length, end_steps + forward_visited[end_pos])
            continue

        # Early termination
        if steps >= best_length or end_steps >= best_length:
            continue

        # Process neighbors
        for queue, visited, current, curr_steps in [
            (forward_queue, forward_visited, pos, steps),
            (backward_queue, backward_visited, end_pos, end_steps),
        ]:
            i, j = current
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                next_pos = (ni, nj)

                if next_pos in visited or not (
                    0 <= ni < len(matrix) and 0 <= nj < len(matrix[0])
                ):
                    continue

                if matrix[ni][nj] == "." or next_pos in cheat_points:
                    queue.append((next_pos, curr_steps + 1))
                    visited[next_pos] = curr_steps + 1

    return best_length if best_length != float("inf") else None


def part_two():
    # Read input
    matrix = [list(line.strip()) for line in open("input.txt")]
    start = end = None

    # Find S and E
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "S":
                start = (i, j)
                matrix[i][j] = "."
            elif matrix[i][j] == "E":
                end = (i, j)
                matrix[i][j] = "."

    # Find all valid cheat points
    valid_cheats = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "#" and is_valid_cheat_point(matrix, i, j):
                valid_cheats.append((i, j))

    # Find normal path length
    normal_length = find_shortest_path_multi(matrix, start, end, set())
    cheat_results = defaultdict(int)

    # Try combinations of cheats (up to 20)
    for k in range(1, min(21, len(valid_cheats) + 1)):
        for cheat_combo in combinations(valid_cheats, k):
            length = find_shortest_path_multi(matrix, start, end, set(cheat_combo))
            if length < normal_length:
                steps_saved = normal_length - length
                cheat_results[steps_saved] += 1

    # Print results
    for steps, count in sorted(cheat_results.items()):
        print(f"Steps saved: {steps}, Count: {count}")


if __name__ == "__main__":
    part_two()
