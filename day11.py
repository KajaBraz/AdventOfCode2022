import re

from read_data import get_data_00


def get_dict(data):
    monkeys = []
    for monkey in data:
        d = {'items': [int(n) for n in re.findall(r'\d+', monkey[1])],
             'operation': monkey[2][17:],
             'test': int(re.findall(r'\d+', monkey[3])[0]),
             'true': int(re.findall(r'\d+', monkey[4])[0]),
             'false': int(re.findall(r'\d+', monkey[5])[0]),
             'inspected': 0}
        monkeys.append(d)
    return monkeys


def play_round(monkeys, divide=True, divisor=1):
    i = 0
    while i < len(monkeys):
        monkey_dict = monkeys[i]
        items = monkey_dict['items']
        monkey_dict['inspected'] += len(items)
        monkey_dict['items'] = []
        worry_level_items = [(execute_operation(monkey_dict['operation'], item) // 3) for item in items] if divide else \
            [execute_operation(monkey_dict['operation'], item) % divisor for item in items]
        monkeys[monkey_dict['true']]['items'] += \
            [item for item in worry_level_items if item % monkey_dict['test'] == 0]
        monkeys[monkey_dict['false']]['items'] += \
            [item for item in worry_level_items if item % monkey_dict['test'] != 0]
        i += 1
    return monkeys


def execute_operation(operation, n1):
    n2 = n1 if len(re.findall(r'old', operation)) == 2 else int(re.findall(r'\d+', operation)[0])
    if '+' in operation:
        return n1 + n2
    if '*' in operation:
        return n1 * n2



def part1(data):
    monkeys = [monkey for monkey in data]
    for i in range(20):
        monkeys = play_round(monkeys)
    inspections = sorted([monkey['inspected'] for monkey in monkeys], reverse=True)
    return inspections[0] * inspections[1]


def part2(data):
    monkeys = [monkey for monkey in data]
    divisors = [d['test'] for d in monkeys]
    divisor = 1
    for div in divisors:
        divisor*= div
    for i in range(10000):
        monkeys = play_round(monkeys, False, divisor)
    inspections = sorted([monkey['inspected'] for monkey in monkeys], reverse=True)
    return inspections[0] * inspections[1]


if __name__ == '__main__':
    input_data = get_data_00('input11.txt').split('\n\n')
    input_data = [[row.strip() for row in monkey.split('\n')] for monkey in input_data]
    m1 = get_dict(input_data)
    m2 = get_dict(input_data)

    # part 1
    r1 = part1(m1)
    print(r1)

    # part 2
    r2 = part2(m2)
    print(r2)
