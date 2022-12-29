from read_data import get_data_02_str_list, get_data_04_two_dim_str_list


def get_round_score_1(x: int, y: int) -> int:
    loser_winner = {'rock': 'sci', 'sci': 'pap', 'pap': 'rock'}
    elf = {'A': 'rock', 'B': 'pap', 'C': 'sci'}
    me = {'X': ('rock', 1), 'Y': ('pap', 2), 'Z': ('sci', 3)}
    if loser_winner[me[y][0]] == elf[x]:
        return me[y][1] + 6
    if elf[x] == me[y][0]:
        return me[y][1] + 3
    return me[y][1]


def play_1(rounds: list[list[str, str]]) -> int:
    return sum(get_round_score_1(player_1, player_2) for player_1, player_2 in rounds)


def play_1_1(rounds: list[str]) -> int:
    loser_winner = {
        'A X': 3 + 1, 'A Y': 6 + 2, 'A Z': 0 + 3,
        'B X': 0 + 1, 'B Y': 3 + 2, 'B Z': 6 + 3,
        'C X': 6 + 1, 'C Y': 0 + 2, 'C Z': 3 + 3
    }
    return sum(loser_winner[r] for r in rounds)


def get_round_score_2(x: int, y: int) -> int:
    elf = {'A': 'rock', 'B': 'pap', 'C': 'sci'}
    round_ends = {'X': ('lose', 0), 'Y': ('draw', 3), 'Z': ('win', 6)}
    loser_winner = {'rock': 'sci', 'sci': 'pap', 'pap': 'rock'}
    winner_loser = {'sci': 'rock', 'pap': 'sci', 'rock': 'pap'}
    me = {'rock': 1, 'pap': 2, 'sci': 3}
    if round_ends[y][0] == 'win':
        return round_ends[y][1] + me[winner_loser[elf[x]]]
    if round_ends[y][0] == 'draw':
        return round_ends[y][1] + me[elf[x]]
    return me[loser_winner[elf[x]]]


def play_2(rounds: list[list[str, str]]) -> int:
    return sum(get_round_score_2(player_1, expected_ending) for player_1, expected_ending in rounds)


if __name__ == '__main__':
    data = get_data_04_two_dim_str_list('input02.txt')
    data2 = get_data_02_str_list('input02.txt')

    # part 1
    total_score_1 = play_1(data)
    total_score_1_1 = play_1_1(data2)

    # part 2
    total_score_2 = play_2(data)

    print(total_score_1, total_score_1_1)
    print(total_score_2)
