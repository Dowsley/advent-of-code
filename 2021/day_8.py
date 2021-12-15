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
    d = [2,3,4,7]

    out = 0
    for l in inputs:
        p = process_input(l)[1]
        for w in p:
            if len(w) in d:
                out +=1
    return out

def decode(encoded_digits):
    originals_by_n = { # DIGIT: Original segments set
        "0": set("abcefg"),
        "1": set("cf"),
        "2": set("acdeg"),
        "3": set("acdfg"),
        "4": set("bcdf"),
        "5": set("abdfg"),
        "6": set("abdefg"),
        "7": set("acf"),
        "8": set("abcdefg"),
        "9": set("abcdfg"),
    }
    # LENGTH: Digit
    originals_by_len = {}
    for k, v in originals_by_n.items():
        l = len(v)
        if not originals_by_len.get(l):
            originals_by_len[l] = list()
        originals_by_len[l].append(v)

    # DECODE!
    maps = []
    encoded_digits.sort(key=len)
    encoded_digits = list(map(set, encoded_digits))

    # Step 1: Decode segments from unique numbers 1,7,4,8
    uniques = encoded_digits[:3] + [encoded_digits[-1]]
    for encoded in uniques:
        original = originals_by_len[len(encoded)][0].copy()
        encoded = encoded.copy()
        # Get combinations
        for e, o in maps:
            original = original.difference(o)
            encoded = encoded.difference(e)
        maps.append([encoded, original])

    # Step 2: Decode segments from non-unique numbers
    non_uniques = encoded_digits[4:][:-1]
    for encoded in non_uniques:
        tmp = encoded.copy()
    print(non_uniques)

def solve_2(inputs):
    res = []

    for i in inputs:
        all_digits, display_digits = process_input(i)
        mapping = decode(all_digits)

if __name__ == '__main__':
    inputs = get_input('input/day_8.txt')
    answer1 = solve_1(inputs)
    print(f"Part 1: {answer1}")

    inputs = get_input('input/day_8.txt')
    answer2 = solve_2(inputs)
    print(f"Part 2: {answer2}")
