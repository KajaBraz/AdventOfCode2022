from pprint import pprint

from read_data import get_data_05_str_int_two_cols


def instert_noops(initial_instructions: list[tuple]) -> list[tuple[tuple, int]]:
    updated_instructions = []
    i = 1
    for instruction in initial_instructions:
        updated_instructions.append((instruction, i))
        if instruction[0] == 'addx':
            i += 1
            updated_instructions.append((('noop',), i))
        i += 1
    return updated_instructions


def execute_instructions(updated_instructions: list[tuple[tuple, int]], save_nth: int, img_size: int) -> \
        tuple[dict[int, int], list[str]]:
    current_exec, following_exec = 1, 0
    executions = {}
    img = []
    for instruction, i in updated_instructions:
        img = img + ['#'] if (i - 1) % img_size in [current_exec - 1, current_exec, current_exec + 1] else img + ['.']

        if i % save_nth == 0:
            executions[i] = current_exec * i

        current_exec, following_exec = current_exec + following_exec, 0

        if instruction[0] == 'addx':
            following_exec += instruction[1]
    return executions, img


def get_img(pixels: list[str], width: int) -> list[str]:
    return [''.join(pixels[i:i + width]) for i in range(0, len(pixels), width)]


def get_solution(updated_instructions: list[tuple[tuple, int]], save_nth: int, img_size: int) -> tuple[int, list[str]]:
    executions, img = execute_instructions(updated_instructions, save_nth, img_size)
    signal_strengths_sum = sum([executions[i] for i in range(20, 221, 40)])
    img = get_img(img, 40)
    return signal_strengths_sum, img


if __name__ == '__main__':
    input_data = get_data_05_str_int_two_cols('input10.txt')
    instructions = instert_noops(input_data)
    solution = get_solution(instructions, 20, 40)

    # part 1
    part_1 = solution[0]

    # part 2
    part_2 = solution[1]

    print(part_1)
    pprint(part_2)
