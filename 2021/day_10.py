from math import floor

def get_input(filename):
    with open(filename, 'r') as f:
        return list(map(lambda x: x.strip(), f.readlines()))

def calculate_score_1(line):
    mapping = {
        ')': ['(', 3],
        ']': ['[', 57],
        '}': ['{', 1197],
        '>': ['<', 25137],
    }
    closing = mapping.keys()

    stack = list()
    for c in line:
        if c in closing:
            if mapping[c][0] == stack[-1]:
                stack.pop(-1)
            else:
                return mapping[c][1]
        else:
            stack.append(c)
    return 0

def calculate_score_2(line):
    mapping = {
        ')': ['(', 1],
        ']': ['[', 2],
        '}': ['{', 3],
        '>': ['<', 4],
    }
    mapping_aux = {
        '(': [')', 1],
        '[': [']', 2],
        '{': ['}', 3],
        '<': ['>', 4],
    }
    closing = mapping.keys()

    stack = list()
    for c in line:
        if c in closing:
            if mapping[c][0] == stack[-1]:
                stack.pop(-1)
            else:
                # Corrupted
                return 0
        else:
            stack.append(c)

    # Incomplete
    points = [mapping_aux[c][1] for c in stack]
    points.reverse()
    score = 0
    for p in points:
        score *= 5
        score += p
    return score

def solve_1(inputs):
    score = 0
    for line in inputs:
        res = calculate_score_1(line)
        score += res
    return score

def solve_2(inputs):
    scores = []
    for line in inputs:
        res = calculate_score_2(line)
        if res != 0:
            scores.append(res)
    scores.sort()
    return scores[int((len(scores)-1)/2)]

if __name__ == '__main__':
    inputs = get_input('input/day_10.txt')
    answer1 = solve_1(inputs)
    print(f"Part 1: {answer1}")

    inputs = get_input('input/day_10.txt')
    answer2 = solve_2(inputs)
    print(f"Part 2: {answer2}")
