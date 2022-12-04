from read_data import get_data_08_all_line_ints


def contains(p1, p2):
    if p2[0] <= p1[0] <= p2[1]:
        if p2[1] >= p1[1] >= p2[0]:
            return True
    if p1[0] <= p2[0] <= p1[1]:
        if p1[1] >= p2[1] >= p1[0]:
            return True
    return False


def overlaps(p1, p2):
    if p2[0] <= p1[0] <= p2[1]:
        return True
    if p2[1] >= p1[1] >= p2[0]:
        return True
    if p1[0] <= p2[0] <= p1[1]:
        return True
    if p1[1] >= p2[1] >= p1[0]:
        return True
    return False


def part1(data):
    return sum([contains(p1, p2) for p1, p2 in data])


def part2(data):
    return sum([overlaps(p1, p2) for p1, p2 in data])


if __name__ == '__main__':
    input_data = get_data_08_all_line_ints('input04.txt')
    input_data = [[d[:2], d[2:]] for d in input_data]
    print(input_data)

    # part 1
    r1 = part1(input_data)

    # part 2
    r2 = part2(input_data)

    print(r1)
    print(r2)
