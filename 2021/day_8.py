def get_input(filename):
    with open(filename, 'r') as f:
        lines =  list(map(lambda x: x.strip(), f.readlines()))
        return lines

def process_input(inp):
    out = inp.split("|")
    out[0] = out[0].strip().split(" ")
    out[1] = out[1].strip().split(" ")
    return out

def solve_1(inputs):
    for l in inputs:
        p = process_input(l)
        print(p)

def solve_2(inputs):
    pass

if __name__ == '__main__':
    inputs = get_input('input/day_8.txt')
    answer1 = solve_1(inputs)
    print(f"Part 1: {answer1}")

    inputs = get_input('input/day_8.txt')
    answer2 = solve_2(inputs)
    print(f"Part 2: {answer2}")
