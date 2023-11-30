from typing import List, Tuple, Dict, Set

from read_data import get_data_00


def play(directions: str, rounds: int) -> int:
    rocks = [('####',), ('.#.', '###', '.#.'), ('###', '..#', '..#'), ('#', '#', '#', '#'), ('##', '##')]
    rocks_start_indices = get_rocks_initial_indices(rocks)

    board_representation = {i: set() for i in range(7)}
    board_height = 0
    direction_i = 0

    for r in range(rounds):
        rock_i = r % len(rocks)
        rock = insert_rock(board_height, rocks_start_indices[rock_i])

        keep_moving = True

        while keep_moving and not any(row < 0 for row, column in rock):
            direction = directions[direction_i % len(directions)]
            rock = move_side(direction, rock, board_representation)

            direction_i += 1
            if reached_bottom(board_representation, rock):
                keep_moving = False
            else:
                rock = move_down(rock)

        board_representation, board_height = update_board(board_representation, rock)
    return board_height


def get_rocks_initial_indices(rocks: List[Tuple[str]]) -> List[List[Tuple[int, int]]]:
    rocks_indices = [
        [(row, column + 2) for row in range(len(rock)) for column in range(len(rock[row])) if rock[row][column] == '#']
        for rock in rocks]
    return rocks_indices


def insert_rock(board_height: int, rock_indices: List[Tuple[int, int]], new_blank_rows: int = 3) -> List[
    Tuple[int, int]]:
    updated_indices = [(i + board_height + new_blank_rows, j) for i, j in rock_indices]
    return updated_indices


def update_board(board_repr: Dict[int, Set[int]], rock: List[Tuple[int, int]]) -> Tuple[Dict[int, Set[int]], int]:
    for row, column in rock:
        board_repr[column].add(row)
    new_height = max(max(v) for v in board_repr.values() if len(v) > 0) + 1
    return board_repr, new_height


def move_down(rock_coords: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    return [(i - 1, j) for i, j in rock_coords]


def move_side(direction: str, rock: List[Tuple[int, int]], board_repr: Dict[int, Set[int]]) -> List[Tuple[int, int]]:
    column_move = -1 if direction == '<' else 1
    can_move = all(is_free(row, column + column_move, board_repr) for row, column in rock)
    if can_move:
        moved = [(row, column + column_move) for row, column in rock]
        return moved
    return rock


def reached_bottom(board_repr: Dict[int, Set[int]], rock_indices: List[Tuple[int, int]]) -> bool:
    for row, column in rock_indices:
        if not board_repr[column]:
            if row == 0:
                return True
        elif row - 1 in board_repr[column]:
            return True
    return False


def is_free(row: int, column: int, board_repr: Dict[int, Set[int]]) -> bool:
    if 0 <= row and 0 <= column < len(board_repr):
        if row not in board_repr[column]:
            return True
    return False


if __name__ == '__main__':
    sample_directions = get_data_00('sample17.txt')
    input_directions = get_data_00('input17.txt')
    example_1 = play(sample_directions, 2022)
    part_1 = play(input_directions, 2022)

    print(f'Part 1:\n\tExample:  {example_1}\n\tSolution: {part_1}')
