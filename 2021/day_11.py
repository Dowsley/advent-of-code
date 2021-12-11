def get_input(filename):
    with open(filename, 'r') as f:
        parsed = list(map(
            lambda s: [int(c) for c in s.strip()],
            f.readlines(),
        ))
        return parsed

def adj_finder(matrix, position):
    adj = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            rangeX = range(0, matrix.shape[0])  # X bounds
            rangeY = range(0, matrix.shape[1])  # Y bounds

            (newX, newY) = (position[0]+dx, position[1]+dy)  # adjacent cell

            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                adj.append((newX, newY))

    return adj

def increase(inputs):
    has_flashed = [[False for i in line] for line in inputs]
    for y in range(len(has_flashed)):
        for x in range(len(has_flashed[y])):
            has_flashed[x][y] = False

    # Increase
    for y in range(len(inputs)):
        for x in range(len(inputs[y])):
            inputs[x][y] += 1

    # Find first to flash
    flash_amount = 0
    has_a_flash = True
    while(has_a_flash):
        has_a_flash = False
        for y in range(len(inputs)):
            for x in range(len(inputs[y])):
                if inputs[x][y] > 9 and not has_flashed[x][y]:
                    has_a_flash = True
                    flash_amount += 1
                    inputs[x][y] = 0
                    if x+1 <= len(inputs[0])-1:
                        inputs[x+1][y] += 1
                    if x-1 >= 0:
                        inputs[x-1][y] += 1
                    if y+1 <= len(inputs)-1:
                        inputs[x][y+1] += 1
                    if y-1 >= 0:
                        inputs[x][y-1] += 1
                    if x+1 <= len(inputs[0])-1 and y+1 <= len(inputs)-1:
                        inputs[x+1][y+1] += 1
                    if x-1 >= 0 and y-1 >= 0:
                        inputs[x-1][y-1] += 1
                    if x+1 <= len(inputs[0])-1 and y-1 >= 0:
                        inputs[x+1][y-1] += 1
                    if x-1 >= 0 and y+1 <= len(inputs)-1:
                        inputs[x-1][y+1] += 1
        return flash_amount

def adj_finder(matrix, position):
    adj = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            rangeX = range(0, matrix.shape[0])  # X bounds
            rangeY = range(0, matrix.shape[1])  # Y bounds

            (newX, newY) = (position[0]+dx, position[1]+dy)  # adjacent cell

            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                adj.append((newX, newY))

    return adj

def solve_part_1(inputs, steps):
    n = 0
    for i in range(steps):
        n += increase(inputs)
    return n

def solve_part_2(inputs):
    pass

if __name__ == '__main__':
    inputs = get_input('input/day_11.txt')

    answer1 = solve_part_1(inputs, 10)
    print(f"Part 1: {answer1}")

    answer2 = solve_part_2(inputs)
    print(f"Part 2: {answer2}")
