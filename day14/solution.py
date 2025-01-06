import math


def predict_easter_egg(robots, width, height, max_steps):
    """
    Predict the time it takes for robots to display the Easter egg pattern.

    Args:
    robots: List of tuples (px, py, vx, vy) for initial positions and velocities.
    width: Width of the space.
    height: Height of the space.
    max_steps: Maximum number of seconds to simulate.

    Returns:
    The fewest number of seconds for the Easter egg pattern to appear.
    """

    def is_compact(positions):
        """Check if the positions are compact (likely forming a recognizable shape)."""
        xs, ys = zip(*positions)
        return max(xs) - min(xs) < width and max(ys) - min(ys) < height

    def display_grid(positions):
        """Display the positions in a grid."""
        grid = [["." for _ in range(width)] for _ in range(height)]
        for x, y in positions:
            if 0 <= x < width and 0 <= y < height:
                grid[y][x] = "#"
        for row in grid:
            print("".join(row))
        print()

    best_time = None

    for t in range(max_steps):
        positions = [(px + vx * t, py + vy * t) for px, py, vx, vy in robots]

        # Calculate compactness
        xs, ys = zip(*positions)
        if max(xs) - min(xs) < width and max(ys) - min(ys) < height:
            print(f"Compact pattern detected at time {t}:")
            display_grid(positions)
            best_time = t
            break

    if best_time is not None:
        return best_time
    return -1  # Easter egg not found within the given steps


def part_two():
    points = read_input_data()
    robots = []
    for p in points:
        robots.append((p[0][0], p[0][1], p[1][0], p[1][1]))
    print(robots)
    time_to_easter_egg = predict_easter_egg(robots, 101, 103, 20000)
    print(f"The fewest number of seconds: {time_to_easter_egg}")


def part_one():
    matrix = read_input_data()
    row = 102
    col = 100
    _list = []
    for m in matrix:
        x = m[0][0]
        y = m[0][1]
        for i in range(100):
            dx = x + m[1][0]
            dy = y + m[1][1]
            print(f"{dx} {dy}")
            if dx < 0:
                x = col + dx + 1
            elif dx > col:
                x = dx - col - 1
            else:
                x = dx
            if dy < 0:
                y = row + dy + 1
            elif dy > row:
                y = dy - row - 1
            else:
                y = dy
        _list.append((x, y))
    print(_list)
    a = [0, 0, 0, 0]
    for l in _list:
        if l[0] < col / 2 and l[1] < row / 2:
            a[0] += 1
        if l[0] > col / 2 and l[1] < row / 2:
            a[1] += 1
        if l[0] > col / 2 and l[1] > row / 2:
            a[2] += 1
        if l[0] < col / 2 and l[1] > row / 2:
            a[3] += 1
    print(a)
    return math.prod(a)


def read_input_data():
    result = []
    with open("input.txt", "r") as file:
        for line in file:
            p = line.strip().split(" ")[0].split("=")[1].split(",")
            v = line.strip().split(" ")[1].split("=")[1].split(",")
            result.append((tuple(map(int, p)), tuple(map(int, v))))
    return result


# print(part_one())
print(part_two())
