'''
Created on Oct 17, 2018

@author: me
'''
import connectfour

running = True

game_state = connectfour.new_game()
#this is the only user defined function
#it displays the board
def display_board(game_state: connectfour.GameState, BOARD_COLUMNS: int, BOARD_ROWS: int) -> str:
    for x in range(0, BOARD_COLUMNS):
        print(" ", end = "")
        print(x+1, end = "")
        print(" ", end = "")
    print("")
    for y in range(0, BOARD_ROWS):
        for x in range(0, BOARD_COLUMNS):
            '''
            print("test block")
            print(game_state.board)
            print("y:", y)
            print("x:", x)
            #print("y_count:", y_count)
            print("test block")
            '''
            if game_state.board[x][y] == 1:
                print(" ", end = "")
                print("R", end = "")
                print(" ", end = "")
            elif game_state.board[x][y] == 2:
                print(" ", end = "")     
                print("Y", end = "")
                print(" ", end = "")
            else:
                print(" ", end = "")
                print(".", end = "")
                print(" ", end = "")
        print("")
while running:
    display_board(game_state, connectfour.BOARD_COLUMNS, connectfour.BOARD_ROWS)
    print("the current player is: ", end = "")
    if game_state.turn==2:
        print("Yellow")
    if game_state.turn==1:
        print("Red")
    command = input("this is the current board. Enter d, followed by the collumn you wish to drop in to drop. Enter p to pop")
    if command[0] == 'd':
        game_state = connectfour.drop(game_state, int(command[1]))
        print("drop was correct")
        print(game_state)
    if command[0] == 'p':
        game_state = connectfour.pop(game_state, int(command[1]))
        print("pop was correct")
        print(game_state)
    if connectfour.winner(game_state)==1:
        print("player one (red) won!")
        running = False
    if connectfour.winner(game_state)==2:
        print("player two (yellow) won!")
        running = False