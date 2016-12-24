import re
import random
import copy

def x_and_o(grid,mark):
    s = grid[2] + grid[1] + grid[0]
    s = re.sub(r'\.',r' ',s)
    board = list(s)
    if mark == 'O':
        player_marker = 'X'
        bot_marker = 'O'
    else:
        player_marker = 'O'
        bot_marker = 'X'
    winning_combos = (
    [6, 7, 8], [3, 4, 5], [0, 1, 2], [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6])
    corners = [0,2,6,8]
    sides = [1,3,5,7]
    middle = 4

    def is_winner(board, marker):
        for combo in winning_combos:
            if (board[combo[0]] == board[combo[1]] == board[combo[2]] == marker):
                return True
        return False

    def is_space_free(board, index):
        return board[index] == ' '

    def is_board_full(board):
        for i in range(1,9):
            if is_space_free(board, i):
                return False
        return True

    def make_move(board,index,move):
        board[index] =  move

    def choose_random_move(move_list):
        possible_winning_moves = []
        for index in move_list:
            if is_space_free(board, index):
                possible_winning_moves.append(index)
                if len(possible_winning_moves) != 0:
                    return random.choice(possible_winning_moves)
                else:
                    return None

    def get_bot_move():
        for i in range(0,len(board)):
            board_copy = copy.deepcopy(board)
            if is_space_free(board_copy, i):
                make_move(board_copy,i,bot_marker)
                if is_winner(board_copy, bot_marker):
                    return i

        for i in range(0,len(board)):
            board_copy = copy.deepcopy(board)
            if is_space_free(board_copy, i):
                make_move(board_copy,i,player_marker)
                if is_winner(board_copy, player_marker):
                    return i

        move = choose_random_move(corners)
        if move != None:
            return move

        if is_space_free(board,middle):
            return middle
        
        return choose_random_move(sides)
    def get_ans(a):
        return (2 - a // 3,a % 3)
    ans = get_bot_move()
    return get_ans(ans)
