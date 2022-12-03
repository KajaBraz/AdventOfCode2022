from string import ascii_lowercase

from read_data import get_data_02_str_list


def split_compartments(compartments):
    return [[comp[:len(comp) // 2], comp[len(comp) // 2:]] for comp in compartments]


def get_priority(item):
    lower = ascii_lowercase
    upper = lower.upper()
    letters = lower + upper
    values = range(1, 53)
    priorities = {letters[i]: values[i] for i in range(52)}
    return priorities[item]


def find_common(items_list):
    items_list = [set(item) for item in items_list]
    s = items_list[0]
    for z in items_list[1:]:
        s = s & z
    return s.pop()


def sum_priorities1(data):
    return sum(get_priority(find_common([comp1, comp2])) for comp1, comp2 in split_compartments(data))


def sum_priorities2(data):
    data = [data[i:i + 3] for i in range(0, len(data), 3)]
    return sum(get_priority(find_common([c1, c2, c3])) for c1, c2, c3 in data)


if __name__ == '__main__':
    input_data = get_data_02_str_list('input03.txt')

    # part 1
    priorities_1 = sum_priorities1(input_data)

    # part 2
    priorities_2 = sum_priorities2(input_data)

    print(priorities_1)
    print(priorities_2)
