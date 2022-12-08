from read_data import get_data_02_str_list


def right_vis(x: int, y: int, grid: list[list[int]]) -> bool:
    return all(True if grid[x][y] > t else False for t in grid[x][y + 1:])


def left_vis(x: int, y: int, grid: list[list[int]]) -> bool:
    return all(True if grid[x][y] > t else False for t in grid[x][:y])


def upper_vis(x: int, y: int, grid: list[list[int]]) -> bool:
    return all(True if grid[x][y] > t else False for t in [p[y] for p in grid[:x]])


def down_vis(x: int, y: int, grid: list[list[int]]) -> bool:
    return all(True if grid[x][y] > t else False for t in [p[y] for p in grid[x + 1:]])


def right_seen(x: int, y: int, grid: list[list[int]]) -> int:
    if y == len(grid[0]) - 1:
        return 0
    s = 0
    for t in grid[x][y + 1:]:
        s += 1
        if grid[x][y] <= t:
            return s + 1
    return s


def left_seen(x: int, y: int, grid: list[list[int]]) -> int:
    if y == 0:
        return 0
    s = 0
    for t in grid[x][:y][::-1]:
        s += 1
        if grid[x][y] <= t:
            return s
    return s


def upper_seen(x: int, y: int, grid: list[list[int]]) -> int:
    if x == 0:
        return 0
    s = 0
    for t in [p[y] for p in grid[:x]][::-1]:
        s += 1
        if grid[x][y] <= t:
            return s + 1
    return s


def down_seen(x: int, y: int, grid: list[list[int]]) -> int:
    if x == len(grid) - 1:
        return 0
    s = 0
    for t in [p[y] for p in grid[x + 1:]]:
        s += 1
        if grid[x][y] <= t:
            return s + 1
    return s


def count_visible(data: list[list[int]]) -> int:
    edge_trees = len(data) * 2 + (len(data[0]) - 2) * 2
    inner_trees = 0
    for x in range(1, len(data) - 1):
        for y in range(1, len(data[x]) - 1):
            r = right_vis(x, y, data)
            l = left_vis(x, y, data)
            u = upper_vis(x, y, data)
            d = down_vis(x, y, data)
            inner_trees = inner_trees + 1 if any([r, l, u, d]) else inner_trees
    return edge_trees + inner_trees


def get_highest_scenic_score(data: list[list[int]]) -> int:
    scenic_score = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            r = right_seen(x, y, data)
            l = left_seen(x, y, data)
            u = upper_seen(x, y, data)
            d = down_seen(x, y, data)
            scenic_score = max(r * l * u * d, scenic_score)
    return scenic_score


if __name__ == '__main__':
    input_data = get_data_02_str_list('input08.txt')
    input_data = [[int(tree) for tree in row] for row in input_data]

    # part 1
    r1 = count_visible(input_data)

    # part 2
    r2 = get_highest_scenic_score(input_data)

    print(r1)
    print(r2)
