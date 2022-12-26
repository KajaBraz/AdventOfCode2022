from read_data import get_data_02_str_list


def get_decimal(snafu_n: str) -> int:
    nums = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
    n = 0
    for i in range(len(snafu_n)):
        n += 5 ** i * nums[snafu_n[~i]]
    return n


def get_snafu(n: int) -> str:
    nums = {2: ('2', 0), 1: ('1', 0), 0: ('0', 0), 3: ('=', 2), 4: ('-', 1)}
    snafu_n = ''
    while n:
        snafu_n += nums[n % 5][0]
        n += nums[n % 5][1]
        n //= 5
    return snafu_n[::-1]


def solve(data):
    n = 0
    for snafu in data:
        n += get_decimal(snafu)
    return get_snafu(n)


if __name__ == '__main__':
    input_data = get_data_02_str_list('input25.txt')
    snafu_number = solve(input_data)
    print(snafu_number)
