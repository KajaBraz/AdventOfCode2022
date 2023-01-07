from __future__ import annotations

import sympy

from read_data import get_data_02_str_list


def execute_job(jobs_dict: dict[str, list[str, str, str] | list[str]], monkey: str) -> int:
    if len(jobs_dict[monkey]) == 1:
        return int(jobs_dict[monkey][0])
    m1, m2 = jobs_dict[monkey][0], jobs_dict[monkey][2]
    if jobs_dict[monkey][1] == '+':
        return execute_job(jobs_dict, m1) + execute_job(jobs_dict, m2)
    elif jobs_dict[monkey][1] == '-':
        return execute_job(jobs_dict, m1) - execute_job(jobs_dict, m2)
    elif jobs_dict[monkey][1] == '*':
        return execute_job(jobs_dict, m1) * execute_job(jobs_dict, m2)
    elif jobs_dict[monkey][1] == '/':
        return execute_job(jobs_dict, m1) // execute_job(jobs_dict, m2)


def get_operations(jobs_dict: dict[str, list[str, str, str] | list[str]], monkey: str) -> list[str, str, str] | list[str]:
    if len(jobs_dict[monkey]) == 1:
        return jobs_dict[monkey]
    m = jobs_dict[monkey]
    m1, m2, sign = m[0], m[2], m[1]
    if m1 not in jobs_dict and m2 not in jobs_dict:
        return m
    if m1 not in jobs_dict and m2 in jobs_dict:
        return [m1, sign, get_operations(jobs_dict, m2)]
    if m1 in jobs_dict and m2 not in jobs_dict:
        return [get_operations(jobs_dict, m1), sign, m2]
    return [get_operations(jobs_dict, m1), sign, get_operations(jobs_dict, m2)]


def get_humn_val(jobs_dict: dict[str, list[str, str, str] | list[str]], humn_side_first_monkey: str,
                 non_humn_side_first_monkey: str) -> float:
    jobs_dict.pop('humn')
    equality_num = execute_job(jobs_dict, non_humn_side_first_monkey)
    expression = get_operations(jobs_dict, humn_side_first_monkey)
    expression = str(expression).replace("'", "").replace(",", "").replace("[", "(").replace("]", ")")
    expression = f'{expression} - {equality_num}'
    humn = sympy.symbols('humn')
    result = eval(f'sympy.solve({expression})')
    return result[0]


if __name__ == '__main__':
    input_data = [row.replace(':', '') for row in get_data_02_str_list('input21.txt')]
    input_data_dict = {row[0]: row[1:] for row in [job.split() for job in input_data]}

    # part 1
    part_1 = execute_job(input_data_dict, 'root')

    # part 2
    humn_left_side = input_data_dict['root'][0]
    humn_right_side = input_data_dict['root'][-1]
    part_2 = get_humn_val(input_data_dict, humn_left_side, humn_right_side)

    print(part_1, part_2)
