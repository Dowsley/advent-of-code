import itertools
from collections import OrderedDict

class TimerGroup():
    def __init__(self, clock, qty):
        self.clock = clock
        self.qty = qty
    def __repr__(self):
        return f"({self.clock}, {self.qty})"

def get_input(filename):
    with open(filename, 'r') as f:
        lst = f.readlines()[0].strip().split(',')
        lst = list(map(int, lst))
        initial = [0 for i in range(0, 9)]
        for c in lst:
            initial[c] += 1
    return initial

def rotate(l, n):
    return l[n:] + l[:n]

def tick_timers(timers):
    new = rotate(timers, 1) # Shift to left
    fish_to_reset = timers[0]
    new[6] += fish_to_reset
    return new

def solve(inputs, n_days):
    timers = inputs.copy()
    for i in range(1, n_days+1):
        timers = tick_timers(timers)
    return sum(timers)

if __name__ == '__main__':
    inputs = get_input('input/day_6.txt')
    answer1 = solve(inputs, 80)
    print(f"Part 1: {answer1}")

    inputs = get_input('input/day_6.txt')
    answer2 = solve(inputs, 256)
    print(f"Part 2: {answer2}")
