from read_data import get_data_09_all_line_ints


def calc_manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def calc_sensor_beacon_dists(data):
    dists = {}
    for sensor, beacon in data.items():
        dists[sensor] = calc_manhattan_dist(sensor, beacon)
    return dists


def filter_sensors_beacons_at_row(target_row, sensor_beacon_dict):
    filtered = {}
    for sensor, beacon in sensor_beacon_dict.items():
        dist = calc_manhattan_dist(sensor, beacon)
        if sensor[1] + dist <= target_row or sensor[1] - dist <= target_row:
            filtered[sensor] = beacon
    return filtered


def get_extremes(sensor_beacon_dict, target_row):
    sensors = sensor_beacon_dict.keys()
    min_s = min(sensors, key=lambda s: s[0])
    max_s = max(sensors, key=lambda s: s[0])
    min_y = min_s[0] - (calc_manhattan_dist(min_s, sensor_beacon_dict[min_s]) - abs(min_s[1] - target_row))
    max_y = max_s[0] + (calc_manhattan_dist(max_s, sensor_beacon_dict[max_s]) - abs(max_s[1] - target_row))
    return min_y, max_y


def cnt_free_positions(ind, sensor_beacon_dict, extremes):
    occupied_positions = set(list(sensor_beacon_dict.keys()))
    occupied_positions.update(sensor_beacon_dict.values())
    occupied_cols = {col for col, row in occupied_positions if row == ind}
    free_positions = [col for col in range(extremes[0], extremes[1] + 1) if col not in occupied_cols]
    free_positions = len(free_positions)
    return free_positions


def part_1(data, target_row):
    filtered = filter_sensors_beacons_at_row(target_row, data)
    min_extreme, max_extreme = get_extremes(filtered, target_row)
    free_pos = cnt_free_positions(target_row, filtered, (min_extreme, max_extreme))
    return free_pos


if __name__ == '__main__':
    input_data = get_data_09_all_line_ints('input15.txt')
    input_data = {tuple(coords[:2]): tuple(coords[2:]) for coords in input_data}
    row = 2000000
    r1 = part_1(input_data, row)
    print(r1)
