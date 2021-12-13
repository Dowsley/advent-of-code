import itertools
from collections import OrderedDict

def triangular_number(n):
    return (n*(n+1))/2

def get_input(filename):
    with open(filename, 'r') as f:
        return list(map(int, f.readlines()[0].strip().split(',')))

def solve_1(inputs):
    least_fuel_amount = float("inf")
    least_fuel_pos = None
    for i in inputs:
        total = 0
        for j in inputs:
            total += abs(i-j)
        if total < least_fuel_amount:
            least_fuel_amount = total
            least_fuel_pos = i
    return least_fuel_amount

def solve_2(inputs):
    max_n = max(inputs)
    min_n = min(inputs)
    r = range(min_n, max_n+1)

    least_fuel_amount = float("inf")
    least_fuel_pos = None
    for i in r:
        total = 0
        for j in inputs:
            res = triangular_number(abs(i-j))
            total += res
        if total < least_fuel_amount:
            least_fuel_amount = total
            least_fuel_pos = i
    return least_fuel_amount

if __name__ == '__main__':
    inputs = get_input('input/day_7.txt')
    answer1 = solve_1(inputs)
    print(f"Part 1: {answer1}")

    inputs = get_input('input/day_7.txt')
    answer2 = solve_2(inputs)
    print(f"Part 2: {answer2}")
