from random import randint
board = []
for x in range(3):
    board.append(["[ ]"] * 3)
def print_board(board):
    for row in board:
        print " ".join(row)
print "Let's play Tic Tac Toe!"
print_board(board)

for turn in range(10):
    turn = turn + 1
    guess_row = int(raw_input("Row:"))
    guess_col = int(raw_input("Col:"))
   
    if (guess_row < 0 or guess_row > 2) or (guess_col < 0 or guess_col > 2):
        print "Oops, that's not even on the board."
    elif (board[guess_row][guess_col] == "[O]") or (board[guess_row][guess_col] == "[X]"):
        print "Spot not available."
    else:
        board[guess_row][guess_col] = "[X]"
        print_board(board)
        xwins = (board[0][0] == "[X]" and board[0][1] == "[X]" and board[0][2] == "[X]") or (board[1][0] == "[X]" and board[1][1] == "[X]" and board[1][2] == "[X]") or (board[2][0] == "[X]" and board[2][1] == "[X]" and board[2][2] == "[X]") or (board[0][0] == "[X]" and board[1][0] == "[X]" and board[2][0] == "[X]") or (board[0][0] == "[X]" and board[1][0] == "[X]" and board[2][0] == "[X]") or (board[1][0] == "[X]" and board[1][1] == "[X]" and board[1][2] == "[X]") or (board[2][0] == "[X]" and board[2][1] == "[X]" and board[2][2] == "[X]") or (board[0][0] == "[X]" and board[1][1] == "[X]" and board[2][2] == "[X]") or (board[2][0] == "[X]" and board[1][1] == "[X]" and board[0][2] == "[X]") or (board[0][2] == "[X]" and board[1][1] == "[X]" and board[2][0] == "[X]")
        owins = (board[0][0] == "[O]" and board[0][1] == "[O]" and board[0][2] == "[O]") or (board[1][0] == "[O]" and board[1][1] == "[O]" and board[1][2] == "[O]") or (board[2][0] == "[O]" and board[2][1] == "[O]" and board[2][2] == "[O]") or (board[0][0] == "[O]" and board[1][0] == "[O]" and board[2][0] == "[O]") or (board[0][0] == "[O]" and board[1][0] == "[O]" and board[2][0] == "[O]") or (board[1][0] == "[O]" and board[1][1] == "[O]" and board[1][2] == "[O]") or (board[2][0] == "[O]" and board[2][1] == "[O]" and board[2][2] == "[O]") or (board[0][0] == "[O]" and board[1][1] == "[O]" and board[2][2] == "[O]") or (board[2][0] == "[O]" and board[1][1] == "[O]" and board[0][2] == "[O]") or (board[0][2] == "[O]" and board[1][1] == "[O]" and board[2][0] == "[O]")
        
        if xwins is True:
            print "You win!"
            break
        elif owins is True:
            print "You lose!"
            break
        else:
            print "My turn!"
            
            def random_row(board):
                return randint(0, len(board) - 1)
            def random_col(board):
                return randint(0, len(board[0]) - 1)
            comp_row = random_row(board)
            comp_col = random_col(board)
            while board[comp_row][comp_col] == "[O]" or board[comp_row][comp_col] == "[X]":
                def random_row(board):
                    return randint(0, len(board) - 1)
                def random_col(board):
                    return randint(0, len(board[0]) - 1)
                
                comp_row = random_row(board)
                comp_col = random_col(board)
             
            else:
                board[comp_row][comp_col] = "[O]"
                print_board(board)

#!/usr/bin/env python

