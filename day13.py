from __future__ import annotations

import re


def get_data(path: str) -> list:
    with open(path, 'r') as f:
        r = f.readlines()
    r = [re.sub(r'\s', '', line) for line in r]
    r = [line for line in r if line]
    return [eval(line) for line in r]


def compare_ints(left: int, right: int) -> int:
    if left < right:
        return 0
    if right < left:
        return 1
    if left == right:
        return -1


def compare_lists(left: list, right: list) -> int:
    if not len(right) and not len(left):
        return -1
    if not len(right) and len(left):
        return 1
    if not len(left) and len(right):
        return 0
    while True:
        comp = compare_pair(left[0], right[0])
        if comp in [0, 1]:
            return comp
        return compare_pair(left[1:], right[1:])


def compare_pair(left: list | int, right: list | int) -> int:
    if type(left) == type(right) == int:
        return compare_ints(left, right)
    if type(left) == type(right) == list:
        return compare_lists(left, right)
    if type(left) == int:
        left = [left]
    elif type(right) == int:
        right = [right]
    return compare_pair(left, right)


def find_insert_ind(new_item: list | int, data: list) -> int:
    i = 1
    for item in data:
        if compare_pair(item, new_item) == 0:
            i += 1
    return i


def part_1(data: list) -> int:
    data = [[data[i], data[i + 1]] for i in range(0, len(data), 2)]
    r = 0
    for i, pair in enumerate(data):
        p1, p2 = pair
        if compare_pair(p1, p2) == 0:
            r += (i + 1)
    return r


def part_2(data: list, new_item_1: list | int, new_item_2: list | int) -> int:
    increment = 1 if new_item_2 >= new_item_1 else 0
    return find_insert_ind(new_item_1, data) * (find_insert_ind(new_item_2, data) + increment)


if __name__ == '__main__':
    input_data = get_data('input13.txt')
    r1 = part_1(input_data)
    print(r1)
    r2 = part_2(input_data, [[2]], [[6]])
    print(r2)
