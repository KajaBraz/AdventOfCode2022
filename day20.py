from typing import List, Tuple

from read_data import get_data_01_int_list


def find_new_i(nums_len: int, n: int, old_i: int) -> int:
    """
    Find the new position of the number being considered in a given iteration.
    """

    new_i = (old_i + n) % (nums_len - 1)
    if new_i == 0 and n < 0:
        new_i = nums_len - 1
    return new_i


def move(nums: List[int], iterations=1) -> List[int]:
    """
    Iterate over the list's elements and move them accordingly.
    """

    indexed = [(i, n) for i, n in enumerate(nums)]
    nums_len = len(indexed)

    for raw_i in range(nums_len * iterations):
        i, n = indexed[raw_i % nums_len]
        if n != 0:
            new_i = find_new_i(nums_len, n, i)
            update_coords(indexed, i, new_i)
    return [b for a, b in sorted(indexed)]


def update_coords(ind_nums: List[Tuple[int, int]], old_i: int, new_i: int) -> None:
    """
    Given a list of tuples, in which the first element is the number's index updated after each iteration
    and the second element is the number, update the indices of each item, depending on their value
    in relation to the position of the item being moved in the current iteration.
    """

    for i, (j, n) in enumerate(ind_nums):
        if j == old_i:
            ind_nums[i] = (new_i, n)
        elif old_i > j >= new_i:
            ind_nums[i] = (j + 1, n)
        elif old_i < j <= new_i:
            ind_nums[i] = (j - 1, n)


def find_0(nums: List[int]) -> int:
    """
    Find the index of number 0. It is assumed there is only one such element.
    """

    for i, n in enumerate(nums):
        if n == 0:
            return i
    return -1


def sum_1000th_2000th_3000th_after_i(nums: List[int], i: int) -> int:
    """
    Calculate the sum of the numbers at the following positions: 1000th, 2000th, and 3000th.
    Roll the list accordingly if it does not contain enough elements.
    """

    th1000 = (i + 1000) % len(nums)
    th2000 = (i + 2000) % len(nums)
    th3000 = (i + 3000) % len(nums)
    return nums[th1000] + nums[th2000] + nums[th3000]


def solve(nums: List[int], encryption_key: int = 1, iterations: int = 1) -> int:
    """
    Complete all the necessary steps to solve the challenge.
    """

    nums = [n * encryption_key for n in nums]
    moved = move(nums, iterations)
    i_zero = find_0(moved)
    s = sum_1000th_2000th_3000th_after_i(moved, i_zero)
    return s


if __name__ == '__main__':
    coords = get_data_01_int_list('input20.txt')

    res_1 = solve(coords)
    print(res_1)

    res_2 = solve(coords, 811589153, 10)
    print(res_2)
