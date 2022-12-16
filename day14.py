from collections import defaultdict

from read_data import get_data_09_all_line_ints


def get_lines(coordinates):
    d = defaultdict(set)
    for lines in coordinates:
        for i in range(0, len(lines) - 2, 2):
            col1, col2 = min(lines[i], lines[i + 2]), max(lines[i], lines[i + 2])
            row1, row2 = min(lines[i + 1], lines[i + 3]), max(lines[i + 1], lines[i + 3])
            if col1 == col2:
                d[col1].update(range(row1, row2 + 1))
            elif row1 == row2:
                for col in range(col1, col2 + 1):
                    d[col].add(row1)
    mx = get_max(d)
    for k, v in d.items():
        d[k] = sorted(v)
    return d, mx


def get_max(lines_dict):
    mx = 0
    for v in lines_dict.values():
        mx = max(mx, max(v))
    return mx


def add_floor(lines_dict, mx):
    for k, v in lines_dict.items():
        lines_dict[k].append(mx + 2)
    return lines_dict


def pour_sand_2(start_col, start_row, lines_dict, mx, initial_size):
    col, row, updated_size = get_falling_coord_2(start_col, start_row, lines_dict, mx, initial_size)
    while row > 0:
        lines_dict[col].insert(0, row)
        lines_dict[col] = sorted(lines_dict[col])
        col, row, updated_size = get_falling_coord_2(start_col, start_row, lines_dict, mx, updated_size)
    lines_dict[start_col].insert(0, 0)
    return lines_dict, updated_size


def get_falling_coord_2(col, row, lines_dict, mx, initial_size):
    row = get_first_lower(row, lines_dict[col], mx)
    if not lines_dict[col + 1]:
        lines_dict[col + 1] = [mx]
        initial_size = initial_size + 1
    if not lines_dict[col - 1]:
        lines_dict[col - 1] = [mx]
        initial_size = initial_size + 1
    if row + 1 in lines_dict[col - 1]:
        if row + 1 in lines_dict[col + 1]:
            return col, row, initial_size
        return get_falling_coord_2(col + 1, row, lines_dict, mx, initial_size)
    return get_falling_coord_2(col - 1, row, lines_dict, mx, initial_size)


def pour_sand(start_col, start_row, lines_dict, mx):
    col, row = get_falling_coord(start_col, start_row, lines_dict, mx)
    while row > 0:
        lines_dict[col].insert(0, row)
        lines_dict[col] = sorted(lines_dict[col])
        col, row = get_falling_coord(start_col, start_row, lines_dict, mx)
    return lines_dict


def get_falling_coord(col, row, lines_dict, mx):
    row = get_first_lower(row, lines_dict[col], mx)
    if col - 1 in lines_dict and row + 1 in lines_dict[col - 1]:
        if col + 1 in lines_dict and row + 1 in lines_dict[col + 1]:
            return col, row
        elif col + 1 in lines_dict:
            return get_falling_coord(col + 1, row, lines_dict, mx)
    elif col - 1 in lines_dict:
        return get_falling_coord(col - 1, row, lines_dict, mx)
    return 0, 0


def get_first_lower(row, l, mx):
    while row < mx + 1:
        row += 1
        if row in l:
            return row - 1
    return row - 1


def part_1(data):
    d, mx = get_lines(data)
    initial_used_space = sum(len(v) for v in d.values())
    d = pour_sand(500, 0, d, mx)
    final_used_space = sum(len(v) for v in d.values())
    return final_used_space - initial_used_space


def part_2(data):
    d, mx = get_lines(data)
    d = add_floor(d, mx)
    mx += 2
    initial_used_spce = sum(len(v) for v in d.values())
    d, updated_size = pour_sand_2(500, 0, d, mx, initial_used_spce)
    final_used_spce = sum(len(v) for v in d.values())
    return final_used_spce - updated_size


if __name__ == '__main__':
    input_data = get_data_09_all_line_ints('input14.txt')
    r1 = part_1(input_data)
    r2 = part_2(input_data)
    print(r1, r2)
