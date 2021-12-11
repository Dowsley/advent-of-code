def get_input(filename):
    with open(filename, 'r') as f:
        parsed = list(map(
            lambda s: s.strip().split(" "),
            f.readlines(),
        ))
        return [(c[0], int(c[1])) for c in parsed]

def solve_part_1(commands):
    depth = 0
    x_pos = 0

    for c in commands:
        direction = c[0]
        amount = c[1]

        if direction == "up":
            depth -= amount
        elif direction == "down":
            depth += amount
        else:
            x_pos += amount

    return depth * x_pos

def solve_part_2(commands):
    depth = 0
    x_pos = 0
    aim = 0

    for c in commands:
        direction = c[0]
        amount = c[1]

        if direction == "up":
            aim -= amount
        elif direction == "down":
            aim += amount
        else:
            x_pos += amount
            depth += aim * amount

    return depth * x_pos

if __name__ == '__main__':
    commands = get_input('input/day_2.txt')

    answer1 = solve_part_1(commands)
    print(f"Part 1: {answer1}")

    answer2 = solve_part_2(commands)
    print(f"Part 2: {answer2}")
