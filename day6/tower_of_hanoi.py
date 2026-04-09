def tower_of_hanoi(n, source, auxiliary, target, moves=None):
    if moves is None:
        moves = []

    if n == 1:
        moves.append((source, target))
    else:
        tower_of_hanoi(n - 1, source, target, auxiliary, moves)
        moves.append((source, target))
        tower_of_hanoi(n - 1, auxiliary, source, target, moves)

    return moves


def print_hanoi_moves(n):
    moves = tower_of_hanoi(n, 'A', 'B', 'C')
    print(f"Total moves required for {n} disks: {len(moves)}")
    for index, (src, dst) in enumerate(moves, start=1):
        print(f"Move {index}: {src} -> {dst}")


if __name__ == '__main__':
    try:
        n = int(input('Enter the number of disks: '))
        if n <= 0:
            raise ValueError('The number of disks must be positive.')
    except ValueError as error:
        print(f'Invalid input: {error}')
    else:
        print_hanoi_moves(n)
