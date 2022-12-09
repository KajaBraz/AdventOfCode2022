from read_data import get_data_05_str_int_two_cols


def move(direction, steps, tail_positions: set[tuple[int, int]], tail_knots: dict[int, tuple[int, int]]) -> \
        tuple[set[tuple[int, int]], dict[int, tuple[int, int]]]:
    h, (xh, yh) = 0, tail_knots[0]
    for _ in range(steps):
        xh, yh = move_direction(xh, yh, direction)
        tail_knots[h] = (xh, yh)
        tail_knots = adjust_tail(tail_knots)
        sorted_knots = sorted(tail_knots.items(), key=lambda z: z[0])
        tail = sorted_knots[-1]
        t, (xt, yt) = tail
        tail_positions.add((xt, yt))
    return tail_positions, tail_knots


def adjust_tail(tail_knots: dict[int, tuple[int, int]]) -> dict[int, tuple[int, int]]:
    h, (xh, yh) = 0, tail_knots[0]
    for k in range(h + 1, len(tail_knots)):
        x, y = tail_knots[k]
        if not touches(xh, yh, x, y):
            x, y = follow(xh, yh, x, y)
            tail_knots[k] = (x, y)
        h, (xh, yh) = k, tail_knots[k]
    return tail_knots


def move_direction(x: int, y: int, direction: str) -> tuple[int, int]:
    directions = {'U': move_up, 'D': move_down, 'R': move_right, 'L': move_left}
    return directions[direction](x, y)


def move_up(x: int, y: int) -> tuple[int, int]:
    return x - 1, y


def move_down(x: int, y: int) -> tuple[int, int]:
    return x + 1, y


def move_right(x: int, y: int) -> tuple[int, int]:
    return x, y + 1


def move_left(x: int, y: int) -> tuple[int, int]:
    return x, y - 1


def touches(xh: int, yh: int, xt: int, yt: int) -> bool:
    return abs(xh - xt) <= 1 and abs(yh - yt) <= 1


def follow(xh: int, yh: int, xt: int, yt: int) -> tuple[int, int]:
    if xh - xt == 2:
        if yh == yt:
            return xt + 1, yt
        if yh - yt >= 1:
            return xt + 1, yt + 1
        if yt - yh >= 1:
            return xt + 1, yt - 1
    if xt - xh == 2:
        if yh == yt:
            return xt - 1, yt
        if yh - yt >= 1:
            return xt - 1, yt + 1
        if yt - yh >= 1:
            return xt - 1, yt - 1
    if yh - yt == 2:
        if xh == xt:
            return xt, yt + 1
        if xh - xt >= 1:
            return xt + 1, yt + 1
        if xt - xh >= 1:
            return xt - 1, yt + 1
    if yt - yh == 2:
        if xh == xt:
            return xt, yt - 1
        if xh - xt >= 1:
            return xt + 1, yt - 1
        if xt - xh >= 1:
            return xt - 1, yt - 1
    return xt, yt


def part1(data: list[tuple[str, int]]) -> int:
    knots_positions = {knot: (0, 0) for knot in range(2)}
    tail_positions = set()
    for direction, steps in data:
        tail_positions, knots_positions = move(direction, steps, tail_positions, knots_positions)
    return len(tail_positions)


def part2(data: list[tuple[str, int]]) -> int:
    knots_positions = {knot: (0, 0) for knot in range(10)}
    tail_positions = set()
    for direction, steps in data:
        tail_positions, knots_positions = move(direction, steps, tail_positions, knots_positions)
    return len(tail_positions)


if __name__ == '__main__':
    input_data = get_data_05_str_int_two_cols('input09.txt')

    # part 1
    r1 = part1(input_data)

    # part 2
    r2 = part2(input_data)

    print(r1)
    print(r2)
