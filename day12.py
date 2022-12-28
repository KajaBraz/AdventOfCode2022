import string

from read_data import get_data_02_str_list


def find_start(board: list[str], start_ch: str) -> list[tuple[int, int]]:
    return [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == start_ch]


def convert_board(board: list[str]) -> list[list[tuple[int, str]]]:
    values = {c: ord(c) - 97 for c in string.ascii_lowercase}
    return [[(values[c], c) if c == c.lower() else (values['z'], 'E') for c in row] for row in board]


def find_path(updated_board: list[list[tuple[int, str]]], start_point: tuple[int, int]) -> int:
    x_start, y_start = start_point
    paths = [((x_start, y_start), 0)]
    visited = set()
    while paths:
        path, count = paths.pop(0)
        if path not in visited:
            visited.add(path)
            next_steps, steps = go_one_step(path, count, updated_board)
            if steps:
                return steps
            paths.extend(next_steps)
    return len(updated_board) ** 2 + 1


def go_one_step(previous: tuple[int, int], count: int, updated_board: list[list[tuple[int, str]]]) -> tuple[
    list[tuple[tuple[int, int], int]], int]:
    x, y = previous
    neighs = get_neighs(x, y, updated_board)
    next_steps = [((nx, ny), count + 1) for nx, ny in neighs if updated_board[nx][ny][0] <= updated_board[x][y][0] + 1]
    done = [count + 1 for nx, ny in neighs if
            updated_board[nx][ny][0] <= updated_board[x][y][0] + 1 and updated_board[nx][ny][1] == 'E']
    return next_steps, min(done) if done else 0


def get_neighs(x: int, y: int, updated_board: list[list[tuple[int, str]]]) -> list[tuple[int, int]]:
    return [(x + i, y + j) for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)] if
            0 <= x + i < len(updated_board) and 0 <= y + j < len(updated_board[0])]


def part_1(board: list[str]) -> int:
    start_points = find_start(board, 'S')
    updated_board = convert_board(board)
    return min(find_path(updated_board, start_point) for start_point in start_points)


def part_2(board: list[str]) -> int:
    start_points = find_start(board, 'a')
    updated_board = convert_board(board)
    return min(find_path(updated_board, start_point) for start_point in start_points)


if __name__ == '__main__':
    input_data = get_data_02_str_list('input12.txt')
    r1 = part_1(input_data)
    print('r1', r1)
    r2 = part_2(input_data)
    print('r2', r2)
