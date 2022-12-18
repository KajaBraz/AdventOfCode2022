from collections import defaultdict

from read_data import get_data_09_all_line_ints


def count_sides(coords: set[tuple[int, int, int]]) -> int:
    checked = defaultdict(int)
    for p1 in coords:
        sides = 6
        for p2 in checked.keys():
            if are_touching(p1, p2):
                checked[p2] -= 1
                sides -= 1
        checked[p1] = sides
    return sum(checked.values())


def are_touching(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> bool:
    x, y, z = p1
    i, j, k = p2
    if abs(x - i) == 1 and y - j == z - k == 0:
        return True
    if abs(y - j) == 1 and x - i == z - k == 0:
        return True
    if abs(z - k) == 1 and x - i == y - j == 0:
        return True
    return False


def get_neighs(coord: tuple[int, int, int]) -> set[tuple[int, int, int]]:
    x, y, z = coord
    return {(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)}


def is_outside(cube: tuple[int, int, int], coords: set[tuple[int, int, int]]) -> bool:
    x_min, x_max = min([x for x, y, z in coords]), max([x for x, y, z in coords])
    y_min, y_max = min([y for x, y, z in coords]), max([y for x, y, z in coords])
    z_min, z_max = min([z for x, y, z in coords]), max([z for x, y, z in coords])

    x_range = range(x_min, x_max + 1)
    y_range = range(y_min, y_max + 1)
    z_range = range(z_min, z_max + 1)

    if cube in coords:
        return False

    checked = set()
    to_check = [cube]

    while to_check:
        x, y, z = to_check.pop()
        if (x, y, z) not in checked:
            checked.add((x, y, z))
            if x not in x_range or y not in y_range or z not in z_range:
                return True
            if (x, y, z) not in coords:
                to_check += get_neighs((x, y, z))
    return False


def part_1(coords: set[tuple[int, int, int]]) -> int:
    return count_sides(coords)


def part_2(coords: set[tuple[int, int, int]]) -> int:
    outer_sides = 0
    for cube in coords:
        for neigh in get_neighs(cube):
            outer_sides = outer_sides + 1 if is_outside(neigh, coords) else outer_sides
    return outer_sides


if __name__ == '__main__':
    input_data = {tuple(coord) for coord in get_data_09_all_line_ints('input18.txt')}

    r1 = part_1(input_data)
    print(r1)

    r2 = part_2(input_data)
    print(r2)
