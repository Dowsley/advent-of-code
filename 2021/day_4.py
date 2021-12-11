import itertools

def get_input(filename):
    with open(filename, 'r') as f:
        lines = list(map(
            lambda s: s.strip(),
            f.readlines(),
        ))

        boards = []
        board = list()
        for i, l in enumerate(lines):
            if i == 0:
                to_draw = [int(n) for n in l.split(',')]
            elif not len(l):
                if i != 1:
                    boards.append(board.copy())
                board = list()
            else:
                board.append([int(n.strip()) for n in list(filter(lambda x:x!='', l.split(' ')))])
            if i == len(lines) - 1:
                boards.append(board.copy())

        return (to_draw, boards)

def check_win(board):
    for row in board:
        # Row check
        if row.count("M") == len(row):
            return True
        # Column check
        for i in range(len(row)):
            col = [r[i] for r in board]
            if col.count("M") == len(col):
                return True

    return False

def mark_board(board, draw):
    for i in range(len(board)):
        board[i] = [n if n!=draw else "M" for n in board[i]]

def get_sum(board):
    flat = list(itertools.chain(*board))
    return sum(list(filter(lambda x: x!="M", flat)))

def solve_part_1(inputs):
    to_draw, boards = inputs

    for draw in to_draw:
        for b in boards:
            mark_board(b, draw)
            has_won = check_win(b)
            if has_won:
                return get_sum(b) * draw

def solve_part_2(inputs):
    to_draw, boards = inputs

    finished = [None for b in boards]
    for draw in to_draw:
        for i, b in enumerate(boards):
            if not finished[i]:
                mark_board(b, draw)
                has_won = check_win(b)
                if has_won:
                    score = get_sum(b) * draw
                    finished[i] = True
                if len(boards) == finished.count(True):
                    return score

if __name__ == '__main__':
    inputs = get_input('input/day_4.txt')
    answer1 = solve_part_1(inputs)
    print(f"Part 1: {answer1}")

    inputs = get_input('input/day_4.txt')
    answer2 = solve_part_2(inputs)
    print(f"Part 2: {answer2}")
