def get_numbers():
    fhand = open('input.txt', 'r')
    inp = fhand.read()
    fhand.close()
    counter = 0
    line = ''
    while True:
        line += inp[counter]
        counter += 1
        if inp[counter] == '\n':
            break

    return line.split(',')


def get_boards():
    game_boards = {}
    fhand = open('input.txt', 'r')
    counter = 0
    line_num = 0
    for line in fhand:
        if line_num == 0:
            line_num += 1
            continue

        if line == '\n':
            counter += 1
            game_boards[counter] = []
        else:
            game_boards[counter].append(line.rstrip().split())
    fhand.close()
    return game_boards


def get_scorecard():
    score_cards = {}
    for i in range(1, 101):
        score_cards[i] = []
        for j in range(5):
            score_cards[i].append([0, 0, 0, 0, 0])
    return score_cards


def play_game():
    numbers = get_numbers()
    game_boards = get_boards()
    score_cards = get_scorecard()

    for number in numbers:
        for game_board in game_boards:
            for line in range(len(game_boards[game_board])):
                if number in game_boards[game_board][line]:
                    num_index = game_boards[game_board][line].index(number)
                    score_cards[game_board][line][num_index] = 1
                if 0 not in score_cards[game_board][line]:
                    return [
                        game_boards[game_board],
                        score_cards[game_board],
                        line,
                        number
                        ]


game = play_game()
winning_board = game[0]
score_win = game[1]
winning_line = game[2]
winning_num = int(game[3])


def calculate_score(board, scorecard, win_line, winning_num):
    unchecked = []
    for line in range(len(score_win)):
        for hit in range(len(score_win[line])):
            if score_win[line][hit] == 0:
                unchecked.append(int(board[line][hit]))
    print(sum(unchecked)*winning_num)


calculate_score(winning_board, score_win, winning_line, winning_num)
