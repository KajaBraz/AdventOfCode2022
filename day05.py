import re

from read_data import get_data_02_str_list


def arrange_columns(columns_as_rows, n):
    columns = [[] for _ in range(n)]
    for row in columns_as_rows[::-1]:
        for i in range(len(row)):
            if row[i]:
                columns[i].append(row[i])
    return columns


def move_one_step(current_stacks, procedure, change_order=True):
    current_stacks_copy = [[item for item in row] for row in current_stacks]
    items_num, stack_from, stack_to = procedure
    items = current_stacks_copy[stack_from - 1][len(current_stacks_copy[stack_from - 1]) - items_num:]
    current_stacks_copy[stack_to - 1] = current_stacks_copy[stack_to - 1] + items[::-1] if change_order else \
        current_stacks_copy[stack_to - 1] + items
    current_stacks_copy[stack_from - 1] = current_stacks_copy[stack_from - 1][
                                          :len(current_stacks_copy[stack_from - 1]) - items_num]
    return current_stacks_copy


def get_top_items(stack):
    return ''.join([item[-1] for item in stack if item])


def move_stacks_items(arranged_stacks, steps, change_order=True):
    for step in steps:
        arranged_stacks = move_one_step(arranged_stacks, step, change_order)
    return get_top_items(arranged_stacks)


if __name__ == '__main__':
    stacks_transposed = get_data_02_str_list('input05a.txt')
    procedures = get_data_02_str_list('input05b.txt')
    procedures = [[int(n) for n in re.findall(r'\d+', row)] for row in procedures]
    stacks_num = len(stacks_transposed[-1].split())
    stacks_transposed = [['' if re.match(r'\s{4}', row[i:i + 4]) else row[i:i + 3] for i in range(0, len(row), 4)] for
                         row in stacks_transposed[:-1]]
    stacks_transposed = [[re.sub(r'[\[\]]', '', s) for s in row] for row in stacks_transposed]
    stacks = arrange_columns(stacks_transposed, stacks_num)

    # part 1
    r1 = move_stacks_items(stacks, procedures)

    # part 2
    r2 = move_stacks_items(stacks, procedures, False)

    print(r1)
    print(r2)
