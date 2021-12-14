def get_input(filename):
    with open(filename, 'r') as f:
        lines =  list(map(lambda x: list(map(int, x.strip())), f.readlines()))
        return lines

def get_adjacents(matrix, i, j):
    adj = [
        get_location(matrix,i-1,j),
        get_location(matrix,i+1,j),
        get_location(matrix,i,j-1),
        get_location(matrix,i,j+1)
    ]
    return list(filter(lambda x: x != None, adj))

def is_lowest(adj, el):
    return all([x > el for x in adj])

def get_location(matrix, i, j):
    if i >= 0 and j >= 0:
        try:
            return matrix[i][j]
        except:
            return None
    return None

def is_in_basin(basin, i, j):
    for x, y in basin:
        if i == x and j == y:
            return True
    return False

def construct_basin(matrix, basin, i, j):
    el = matrix[i][j]
    if el != 9:
        basin.append((i, j))
    else:
        return

    # Get adjacents
    to_try = [
        (i-1,j),
        (i+1,j),
        (i,j-1),
        (i,j+1),
    ]
    for x, y in to_try:
        if not is_in_basin(basin, x, y):
            n = get_location(matrix, x, y)
            if n != None:
                if n >= el:
                    construct_basin(matrix, basin, x, y)

def solve_2(matrix):
    # Get lowest points
    basins = []
    for i, x in enumerate(matrix):
        for j, y in enumerate(x):
            adj = get_adjacents(matrix, i, j)
            if is_lowest(adj, y):
                b = []
                construct_basin(matrix, b, i, j)
                basins.append(b)

    sizes = list(map(len, basins))
    sizes.sort(reverse=True)

    mult = 1
    for s in sizes[:3]:
        mult *= s
    return mult

def solve_1(matrix):
    risks = []
    for i, x in enumerate(matrix):
        for j, y in enumerate(x):
            adj = get_adjacents(matrix, i, j)
            if is_lowest(adj, y):
                risks.append(y+1)
    return sum(risks)

if __name__ == '__main__':
    inputs = get_input('input/day_9.txt')
    answer1 = solve_1(inputs)
    print(f"Part 1: {answer1}")

    inputs = get_input('input/day_9.txt')
    answer2 = solve_2(inputs)
    print(f"Part 2: {answer2}")
