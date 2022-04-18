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
        score_cards[i] = {'board': [], 'win': 0}

        for j in range(5):
            score_cards[i]['board'].append([0, 0, 0, 0, 0])
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


# game = play_game()
# winning_board = game[0]
# score_win = game[1]
# winning_line = game[2]
# winning_num = int(game[3])


# def calculate_score(board, scorecard, win_line, winning_num):
#     unchecked = []
#     for line in range(len(score_win)):
#         for hit in range(len(score_win[line])):
#             if score_win[line][hit] == 0:
#                 unchecked.append(int(board[line][hit]))
#     print(sum(unchecked)*winning_num)


# calculate_score(winning_board, score_win, winning_line, winning_num)

def find_last():
    numbers = get_numbers()
    game_boards = get_boards()
    score_cards = get_scorecard()

    game_wins = 0
    for number in numbers:
        for game_number, game_board in game_boards.items():
            score_card = score_cards[game_number]
            if score_card['win'] == 1:
                continue
            check_board(game_board, number, score_card)
            if check_win(score_card['board']):
                score_card['win'] = 1
                game_wins += 1
            if game_wins == 100:
                return calculate_last(number, game_board, score_card['board'])


def check_board(game_board, number, score_card):
    line_amt = len(game_board)
    for line in range(line_amt):
        if number in game_board[line]:
            score_card['board'][line][game_board[line].index(number)] = 1


def check_win(score_card):
    if check_row(score_card):
        return True
    if check_column(score_card):
        return True
    # if check_diag(score_card):
    #     return True


def check_row(score_card):
    for line in score_card:
        if 0 not in line:
            return True


def check_column(score_card):
    for i in range(5):
        col = []
        for line in score_card:
            col.append(line[i])
        if 0 not in col:
            return True


def check_diag(score_card):
    diag = []
    for i in range(5):
        diag.append(score_card[i][i])
    if 0 not in diag:
        return True
    diag_2 = [
        score_card[4][0],
        score_card[3][1],
        score_card[2][2],
        score_card[1][3],
        score_card[0][4],
        ]
    if 0 not in diag_2:
        return True


def calculate_last(number, game_board, score_board):
    total = 0
    for line_no in range(len(score_board)):
        for num_index in range(len(score_board[line_no])):
            if score_board[line_no][num_index] == 0:
                total += int(game_board[line_no][num_index])
    return total * int(number)


a = find_last()
print(a)
