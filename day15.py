from read_data import get_data_09_all_line_ints


def calc_manhattan_dist(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def filter_sensors_beacons_at_row(target_row, sensor_beacon_dict: dict[tuple[int, int], tuple[int, int]]) -> dict[
    tuple[int, int], tuple[int, int]]:
    filtered = {}
    for sensor, beacon in sensor_beacon_dict.items():
        dist = calc_manhattan_dist(sensor, beacon)
        if sensor[1] + dist <= target_row or sensor[1] - dist <= target_row:
            filtered[sensor] = beacon
    return filtered


def get_covered_positions_at_row(target_row: int, sensor_beacon_dict: dict[tuple[int, int], tuple[int, int]]) -> \
        list[range]:
    covered = set()
    for sensor, beacon in sensor_beacon_dict.items():
        dist = calc_manhattan_dist(sensor, beacon)
        if sensor[1] + dist <= target_row or sensor[1] - dist <= target_row:
            reach = dist - abs(sensor[1] - target_row)
            if reach > 0:
                covered.add(range(sensor[0] - reach, sensor[0] + reach + 1))
    return sorted(covered, key=lambda r: r.start)


def get_extremes(sensor_beacon_dict: dict[tuple[int, int], tuple[int, int]], target_row: int) -> tuple[int, int]:
    min_y, max_y = 1000000000, -1000000000
    for sensor, beacon in sensor_beacon_dict.items():
        min_y_temp = sensor[0] - (calc_manhattan_dist(sensor, beacon) - abs(sensor[1] - target_row))
        max_y_temp = sensor[0] + (calc_manhattan_dist(sensor, beacon) - abs(sensor[1] - target_row))
        min_y = min_y_temp if min_y_temp < min_y else min_y
        max_y = max_y_temp if max_y_temp > max_y else max_y
    return min_y, max_y


def cnt_no_beacon_positions(target_row: int, sensor_beacon_dict: dict[tuple[int, int], tuple[int, int]],
                            extremes: tuple[int, int]) -> set[int]:
    occupied_positions = set(list(sensor_beacon_dict.keys()))
    occupied_positions.update(sensor_beacon_dict.values())
    occupied_cols = {col for col, row in occupied_positions if row == target_row}
    no_beacon_positions = set(range(extremes[0], extremes[1] + 1)) - occupied_cols
    return no_beacon_positions


def has_free_pos(rows_ranges) -> tuple[bool, int]:
    biggest = rows_ranges[0][-1]
    for r in rows_ranges[1:]:
        if r[0] > biggest + 1:
            return True, r[0] - 1
        biggest = max(biggest, r[-1])
    return False, -1000000000


def find_distress_beacon(sensor_beacon_dict: dict[tuple[int, int], tuple[int, int]], min_coord: int, max_coord: int) -> \
        tuple[int, int]:
    for cur_row in range(min_coord, max_coord + 1):
        row_ranges = get_covered_positions_at_row(cur_row, sensor_beacon_dict)
        no_beacon_pos = has_free_pos(row_ranges)
        if no_beacon_pos[0]:
            return no_beacon_pos[1], cur_row
    return -1000000000, -1000000000


def part_1(data: dict[tuple[int, int], tuple[int, int]], target_row: int) -> int:
    filtered = filter_sensors_beacons_at_row(target_row, data)
    min_extreme, max_extreme = get_extremes(filtered, target_row)
    no_beacon_positions = cnt_no_beacon_positions(target_row, filtered, (min_extreme, max_extreme))
    return len(no_beacon_positions)


def part_2(data: dict[tuple[int, int], tuple[int, int]], min_coord: int = 0, max_coord: int = 4000000) -> int:
    x, y = find_distress_beacon(data, min_coord, max_coord)
    return 4000000 * x + y


if __name__ == '__main__':
    input_data = get_data_09_all_line_ints('input15.txt')
    input_data = {tuple(coords[:2]): tuple(coords[2:]) for coords in input_data}
    r1 = part_1(input_data, 2000000)
    print(r1)
    r2 = part_2(input_data)
    print(r2)
