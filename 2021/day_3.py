def get_input(filename):
    with open(filename, 'r') as f:
        return list(map(
            lambda s: s.strip(),
            f.readlines(),
        ))

def solve_part_1(inputs):
    length = len(inputs[0])

    gamma = ''   # Most common digit
    epsilon = '' # least common
    for i in range(length):
        all_digits = [s[i] for s in inputs]
        most_common = max(all_digits, key=all_digits.count)
        gamma += most_common
        epsilon += "0" if most_common == "1" else "1"

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return epsilon * gamma

def solve_part_2(inputs):
    length = len(inputs[0])
    oxygen = inputs.copy()
    co2 = inputs.copy()

    # OXYGEN
    for i in range(length):
        all_digits = [s[i] for s in oxygen]
        count_of_1 = all_digits.count("1")
        count_of_0 = all_digits.count("0")
        most_common = "1" if count_of_1 >= count_of_0 else "0"
        if len(oxygen) > 1:
            oxygen = list(filter(lambda n: n[i] == most_common, oxygen))

    # CO2
    for i in range(length):
        all_digits = [s[i] for s in co2]
        count_of_1 = all_digits.count("1")
        count_of_0 = all_digits.count("0")
        most_common = "1" if count_of_1 >= count_of_0 else "0"
        if len(co2) > 1:
            co2 = list(filter(lambda n: n[i] != most_common, co2))

    oxygen = int(oxygen[0], 2)
    co2 = int(co2[0], 2)
    return oxygen * co2

if __name__ == '__main__':
    inputs = get_input('input/day_3.txt')

    answer1 = solve_part_1(inputs)
    print(f"Part 1: {answer1}")

    answer2 = solve_part_2(inputs)
    print(f"Part 2: {answer2}")
