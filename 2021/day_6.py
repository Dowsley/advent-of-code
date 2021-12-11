import itertools

def get_input(filename):
    with open(filename, 'r') as f:
        l = f.readlines()[0].strip().split(',')
        return list(map(int, l))

def spawn_new_fish(timers, amount):
    new_fish = [8 for i in range(amount)]
    return timers + new_fish

def tick_timers(timers):
    amount = 0
    for i, t in enumerate(timers):
        if t==0:
            timers[i] = 6
            amount += 1
        else:
            timers[i] -= 1
    return amount

def solve_part_1(inputs, n_days):
    timers = inputs.copy()
    for i in range(1, n_days+1):
        print(i)
        new_fish_amount = tick_timers(timers)
        timers = spawn_new_fish(timers, new_fish_amount)
    return len(timers)

if __name__ == '__main__':
    inputs = get_input('input/day_6.txt')

    answer1 = solve_part_1(inputs, 80)
    print(f"Part 1: {answer1}")

    answer2 = solve_part_1(inputs, 256)
    print(f"Part 2: {answer2}")
