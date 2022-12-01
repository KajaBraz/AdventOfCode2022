def get_input(path: str):
    data = open(path, 'r').read()
    nums = data.split('\n\n')
    nums = [[int(n) for n in cals.split('\n')] for cals in nums]
    return nums


if __name__ == '__main__':
    input_data = get_input('input01.txt')

    # part 1
    cals = [sum(n) for n in input_data]
    max_cals_elf = max(cals)
    print(max_cals_elf)

    # part 2
    max_cals_thee_elves = sorted(cals, reverse=True)[:3]
    print(sum(max_cals_thee_elves))