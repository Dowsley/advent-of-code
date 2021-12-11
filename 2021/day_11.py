def get_input(filename):
    with open(filename, 'r') as f:
        parsed = list(map(
            lambda s: [int(c) for c in s.strip()],
            f.readlines(),
        ))
        return parsed

def print_matrix(inputs):
    for row in inputs:
        print(row)
    print("\n")

def flash(inputs, x, y, has_flashed):
    if x+1 <= len(inputs[0])-1:
        flash_aux(inputs, x+1, y, has_flashed)
    if x-1 >= 0:
        flash_aux(inputs, x-1, y, has_flashed)
    if y+1 <= len(inputs)-1:
        flash_aux(inputs, x, y+1, has_flashed)
    if y-1 >= 0:
        flash_aux(inputs, x, y-1, has_flashed)
    if x+1 <= len(inputs[0])-1 and y+1 <= len(inputs)-1:
        flash_aux(inputs, x+1, y+1, has_flashed)
    if x-1 >= 0 and y-1 >= 0:
        flash_aux(inputs, x-1, y-1, has_flashed)
    if x+1 <= len(inputs[0])-1 and y-1 >= 0:
        flash_aux(inputs, x+1, y-1, has_flashed)
    if x-1 >= 0 and y+1 <= len(inputs)-1:
        flash_aux(inputs, x-1, y+1, has_flashed)

def flash_aux(matrix, x, y, has_flashed):
    if matrix[x][y] != "." and not has_flashed.get(f"{x}{y}"):
        matrix[x][y] += 1

def compute_flashes(old):
    aux = [[n+1 for n in line] for line in old]

    has_flashed = {}

    flashes = 0
    prev_flashes = -1
    while(flashes > prev_flashes):
        prev_flashes = flashes
        new = [["." if n > 9 else n for n in line] for line in aux]
        for y in range(len(old)):
            for x in range(len(old[y])):
                if new[x][y] == ".":
                    flash(new, x, y, has_flashed)
                    flashes += 1
        # Clear "."
        for y in range(len(old)):
            for x in range(len(old[y])):
                if new[x][y] == ".":
                    new[x][y] = 0
                    has_flashed[f"{x}{y}"] = True
        aux = [line.copy() for line in new]

    return (new, flashes)

def solve_part_1(inputs, steps):
    n = 0
    for i in range(steps):
        inputs, new_n = compute_flashes(inputs)
        n += new_n
    return n

def solve_part_2(inputs):
    total_elements = len(inputs) * len(inputs[0])
    i = 1
    while(True):
        inputs, new_n = compute_flashes(inputs)
        if total_elements == new_n:
            return i
        i += 1

if __name__ == '__main__':
    inputs = get_input('input/day_11.txt')

    answer1 = solve_part_1(inputs, 100)
    print(f"Part 1: {answer1}")

    answer2 = solve_part_2(inputs)
    print(f"Part 2: {answer2}")
