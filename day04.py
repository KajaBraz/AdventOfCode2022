from read_data import get_data_08_all_line_ints


def contains(p1, p2):
    p = sorted(p1 + p2)
    return [p[1], p[2]] == p1 or [p[1], p[2]] == p2


def overlaps(p1, p2):
    p1, p2 = sorted([p1, p2])
    return p1[1] >= p2[0]


def part1(data):
    return sum([contains(p1, p2) for p1, p2 in data])


def part2(data):
    return sum([overlaps(p1, p2) for p1, p2 in data])


if __name__ == '__main__':
    input_data = get_data_08_all_line_ints('input04.txt')
    input_data = [[d[:2], d[2:]] for d in input_data]

    # part 1
    r1 = part1(input_data)

    # part 2
    r2 = part2(input_data)

    print(r1)
    print(r2)
