def read_data(path: str) -> [list[str]]:
    with open(path) as f:
        input_lines = [line.strip() for line in f]
    return [line.split() for line in input_lines]


def play_1(rounds):
    loser_winner = {'rock': 'sci', 'sci': 'pap', 'pap': 'rock'}
    elf = {'A': 'rock', 'B': 'pap', 'C': 'sci'}
    me = {'X': ('rock', 1), 'Y': ('pap', 2), 'Z': ('sci', 3)}
    score = 0
    for x, y in rounds:
        score += me[y][1]
        if loser_winner[me[y][0]] == elf[x]:
            score += 6
        elif elf[x] == me[y][0]:
            score += 3
    return score


def play_2(rounds):
    elf = {'A': 'rock', 'B': 'pap', 'C': 'sci'}
    round_ends = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
    loser_winner = {'rock': 'sci', 'sci': 'pap', 'pap': 'rock'}
    winner_loser = {'sci': 'rock', 'pap': 'sci', 'rock': 'pap'}
    me = {'rock': 1, 'pap': 2, 'sci': 3}
    score = 0
    for x, y in rounds:
        if round_ends[y] == 'win':
            score += me[winner_loser[elf[x]]]
            score += 6
        elif round_ends[y] == 'draw':
            score += me[elf[x]]
            score += 3
        else:
            score += me[loser_winner[elf[x]]]
    return score


if __name__ == '__main__':
    data = read_data('input02.txt')

    # part 1
    total_score_1 = play_1(data)

    # part 2
    total_score_2 = play_2(data)

    print(total_score_1, total_score_2)
