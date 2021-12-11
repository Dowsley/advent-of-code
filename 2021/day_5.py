import itertools

class Cloud():
    def __init__(self, x1, y1, x2, y2):
        self.start = (x1, y1)
        self.end = (x2, y2)

def get_input(filename, toggle=False):
    with open(filename, 'r') as f:
        lines = list(map(
            lambda s: s.strip().split(" -> "),
            f.readlines(),
        ))

        clouds = []
        max_x = -1
        max_y = -1
        for l in lines:
            x1, y1 = list(map(int, l[0].split(',')))
            x2, y2 = list(map(int, l[1].split(',')))
            if toggle or is_line_vertical(x1, y1, x2, y2):
                tmp_x = max(x1, x2)
                tmp_y = max(y1, y2)
                max_x = tmp_x if tmp_x > max_x else max_x
                max_y = tmp_y if tmp_y > max_y else max_y
                clouds.append(Cloud(x1,y1,x2,y2))

        return (clouds, max_x, max_y)

def is_line_vertical(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2

def visualize_map(cloud_map):
    for row in cloud_map:
        print(''.join(list(map(str, row))))

def build_map(clouds, max_x, max_y):
    cloud_map = [['.' for x in range(max_x+1)] for y in range(max_y+1)]

    for c in clouds:
        line = get_line(c.start, c.end)
        for l in line:
            x, y = l
            char = cloud_map[y][x]
            if char == '.':
                cloud_map[y][x] = 1
            else:
                cloud_map[y][x] += 1

    return cloud_map

def get_line(start, end):
    x1, y1 = start
    x2, y2 = end

    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()
    return points

def solve_part_1(inputs, max_x, max_y):
    cloud_map = build_map(inputs, max_x, max_y)
    visualize_map(cloud_map)

    flat = list(itertools.chain(*cloud_map))
    flat = list(filter(lambda p: p!=".", flat))
    return len(list(filter(lambda p: p>=2, flat)))

if __name__ == '__main__':
    inputs, max_x, max_y = get_input('input/day_5.txt')
    answer1 = solve_part_1(inputs, max_x, max_y)
    print(f"Part 1: {answer1}")

    inputs, max_x, max_y = get_input('input/day_5.txt', toggle=True)
    answer2 = solve_part_1(inputs, max_x, max_y)
    print(f"Part 2: {answer2}")
