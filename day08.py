from read_data import get_data_02_str_list


def a(data):
    visible = 0
    for x in range(1, len(data) - 1):
        for y in range(1, len(data[x]) - 1):
            r = right_vis(x, y, data)
            l = left_vis(x, y, data)
            u = upper_vis(x, y, data)
            d = down_vis(x, y, data)
            visible = visible + 1 if any([r, l, u, d]) else visible
    return visible


def right_vis(x, y, grid):
    return all(True if grid[x][y] > t else False for t in grid[x][y + 1:])


def left_vis(x, y, grid):
    return all(True if grid[x][y] > t else False for t in grid[x][:y])


def upper_vis(x, y, grid):
    return all(True if grid[x][y] > t else False for t in [p[y] for p in grid[:x]])


def down_vis(x, y, grid):
    return all(True if grid[x][y] > t else False for t in [p[y] for p in grid[x + 1:]])


def count_leading(l):
    i = 0
    s = 0
    while i < len(l) and l[i]:
        s += 1
        i += 1
    return s


def right_seen(x, y, grid):
    if y == len(grid[0]) - 1:
        return 0
    cur = grid[x][y + 1]
    s = 1
    if grid[x][y] <= cur:
        return s
    print('r', grid[x][y + 2:])
    for t in grid[x][y + 2:]:
        if grid[x][y] <= t:
            return s + 1
        if t >= cur:
            s += 1
            cur = t
        else:
            break
    return s


def left_seen(x, y, grid):
    if y == 0:
        return 0
    cur = grid[x][y - 1]
    s = 1
    if grid[x][y] <= cur:
        return s
    print('l', grid[x][:y - 1][::-1])
    for t in grid[x][:y - 1][::-1]:
        if grid[x][y] <= t:
            return s + 1
        if t >= cur:
            s += 1
            cur = t
        else:
            break
    return s


def upper_seen(x, y, grid):
    if x == 0:
        return 0
    cur = grid[x - 1][y]
    s = 1
    if grid[x][y] <= cur:
        return s
    print('u', [p[y] for p in grid[:x - 1]][::-1])
    for t in [p[y] for p in grid[:x - 1]][::-1]:
        if grid[x][y] <= t:
            return s + 1
        if t >= cur:
            s += 1
            cur = t
        else:
            break
    return s


def down_seen(x, y, grid):
    if x == len(grid) - 1:
        return 0
    cur = grid[x + 1][y]
    s = 1
    if grid[x][y] <= cur:
        return s
    print('d', [p[y] for p in grid[x + 2:]])
    for t in [p[y] for p in grid[x + 2:]]:
        if grid[x][y] <= t:
            return s + 1
        if t >= cur:
            s += 1
            cur = t
        else:
            break
    return s


def b(data):
    scenic_score = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            r = right_seen(x, y, data)
            l = left_seen(x, y, data)
            u = upper_seen(x, y, data)
            d = down_seen(x, y, data)
            print(x, y, data[x][y])
            print('r, l, u, d: ', r, l, u, d, '->', r * l * u * d)
            print('pr', scenic_score)
            scenic_score = max(r * l * u * d, scenic_score)
            print('po', scenic_score)
            print()
    return scenic_score


def part1(data):
    vis = a(data)
    return len(data) * 2 + (len(data[0]) - 2) * 2 + vis


def part2(data):
    return b(data)


if __name__ == '__main__':
    input_data = get_data_02_str_list('input08.txt')
    input_data = [[int(tree) for tree in row] for row in input_data]
    # pprint(input_data)

    # part 1
    # r1 = part1(input_data)

    # part 2
    r2 = part2(input_data)

    # print(r1)
    print(r2)
