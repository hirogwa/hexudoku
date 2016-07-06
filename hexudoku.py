import time


def backtrack(board):
    c, candidates = next_blank_coordinate(board)
    if c is None:
        # solved
        return True
    for value in candidates:
        board[c] = value
        if backtrack(board):
            return True
    board[c] = 0
    return False


def next_blank_coordinate(board):
    for i in range(base ** 2):
        if board[i] == 0:
            return i, get_candidates(board, i)
    return None, None


def get_candidates(board, c):
    taken = []
    # horizontal
    taken.extend([board[x] for x in range(base**2) if x // base == c // base])
    # vertical
    taken.extend([board[x] for x in range(base**2) if x % base == c % base])
    # block
    taken.extend(
        [board[x] for x in range(base**2) if block_index(x) == block_index(c)]
    )
    return [x for x in range(1, base + 1) if x not in taken]


def block_index(c):
    row = c // base ** 1.5
    col = c % base // base ** 0.5
    return int((base ** 0.5) * row + col)


def validate_board(board):
    for i in range(base):
        a = sorted(board[i * base:(i + 1) * base])
        print('row {}: {}'.format(
            i, 'ok' if a == list(range(1, base + 1)) else 'fail'))

        b = sorted([board[x] for x in range(base ** 2) if x % base == i % base])
        print('col {}: {}'.format(
            i, 'ok' if b == list(range(1, base + 1)) else 'fail'))

        c = sorted([board[x] for x in range(base ** 2) if block_index(x) == i])
        print('blk {}: {}'.format(
            i, 'ok' if c == list(range(1, base + 1)) else 'fail'))


def valid_base_or_assert():
    assert len(board) == base**2
    for i in range(1, 5):
        if i ** 2 == base:
            return True
    assert False


def print_board(board):
    fmt = '{:x}' if base == 16 else '{:d}'
    for row in [board[i:i+base] for i in range(0, len(board), base)]:
        print(' '.join([fmt.format(x) for x in row]))

board = [
    1, 2, 3, 4,
    3, 0, 0, 2,
    2, 0, 4, 1,
    4, 1, 2, 0
]
base = 4

board = [
    0, 2, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 6, 0, 0, 0, 0, 3,
    0, 7, 4, 0, 8, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 3, 0, 0, 2,
    0, 8, 0, 0, 4, 0, 0, 1, 0,
    6, 0, 0, 5, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 7, 8, 0,
    5, 0, 0, 0, 0, 9, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 4, 0,
]
base = 9


if __name__ == '__main__':
    s = time.time()
    valid_base_or_assert()
    print('Q:')
    print_board(board)
    if backtrack(board):
        print('A:')
        print_board(board)
    else:
        print('failed')
    f = time.time()

    print('Time:')
    print(f - s)

    validate_board(board)
