from collections import Counter

from read_data import get_data_02_str_list


def get_initial_positions(data):
    positions = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '#':
                positions.add((i, j))
    return positions


def get_all_neighs(x, y):
    return {(x + i, y + j) for i in (1, 0, -1) for j in (1, 0, -1)} - {(x, y)}


def get_direction_neighs(x, y, direction):
    neighs_positions = {'N': ((-1, 0), (-1, 1), (-1, -1)), 'S': ((1, 0), (1, 1), (1, -1)),
                        'W': ((0, -1), (-1, -1), (1, -1)), 'E': ((0, 1), (-1, 1), (1, 1))}
    return {(x + neigh[0], y + neigh[1]) for neigh in neighs_positions[direction]}


def can_move(considered_neighs, elves_positions):
    return all(neigh not in elves_positions for neigh in considered_neighs)


def choose_direction(round_directions, x, y, elves_positions):
    for dir in round_directions:
        all_neighs = get_all_neighs(x, y)
        if can_move(all_neighs, elves_positions):
            return ''
        neighs = get_direction_neighs(x, y, dir)
        if can_move(neighs, elves_positions):
            return dir
    return ''


def get_new_position(x, y, direction):
    new_directions = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1), '': (0, 0)}
    return x + new_directions[direction][0], y + new_directions[direction][1]


def propose_moves(round_directions, elves_positions):
    proposed_positions = {}
    for x, y in elves_positions:
        proposed_dir = choose_direction(round_directions, x, y, elves_positions)
        xn, yn = get_new_position(x, y, proposed_dir)
        proposed_positions[(x, y)] = (xn, yn)
    return proposed_positions


def move_round(proposed_moves):
    proposed = Counter(proposed_moves.values())
    new_positions = set()
    for old_pos, new_pos in proposed_moves.items():
        if proposed[new_pos] == 1:
            new_positions.add(new_pos)
        else:
            new_positions.add(old_pos)
    return new_positions


def calculate_area(elves_positions):
    edges_up_down = {pos[0] for pos in elves_positions}
    edges_right_down = {pos[1] for pos in elves_positions}
    up, down = min(edges_up_down), max(edges_up_down)
    left, right = min(edges_right_down), max(edges_right_down)
    area = (down - up + 1) * (right - left + 1)
    return area


def count_empty_tiles(area, elves_positions):
    return area - len(elves_positions)


def part_1(data):
    new_positions = get_initial_positions(data)
    round_directions = ['N', 'S', 'W', 'E']
    for _ in range(10):
        elves_positions = new_positions
        proposed_moves = propose_moves(round_directions, elves_positions)
        new_positions = move_round(proposed_moves)
        round_directions = round_directions[1:] + [round_directions[0]]
    all_tiles = calculate_area(new_positions)
    return count_empty_tiles(all_tiles, new_positions)


def part_2(data):
    elves_positions = set()
    new_positions = get_initial_positions(data)
    round_directions = ['N', 'S', 'W', 'E']
    i = 0
    while elves_positions != new_positions:
        i += 1
        elves_positions = new_positions
        proposed_moves = propose_moves(round_directions, elves_positions)
        new_positions = move_round(proposed_moves)
        round_directions = round_directions[1:] + [round_directions[0]]
    return i


if __name__ == '__main__':
    input_data = get_data_02_str_list('input23.txt')

    # part 1
    empty_tiles = part_1(input_data)
    print(empty_tiles)

    # part 2
    moves = part_2(input_data)
    print(moves)
