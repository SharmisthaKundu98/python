#making a game tic-tac-toe

def print_the_board(dict_board):
    print(dict_board[1],"|",dict_board[2],"|",dict_board[3],"|")
    print("------------")
    print(dict_board[4],"|",dict_board[5],"|",dict_board[6],"|")
    print("------------")
    print(dict_board[7],"|",dict_board[8],"|",dict_board[9],"|")

dict_board = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
def change_board(player_turn,button): #player_1//player_2
        dict_board[player_turn] = button # 5 --> X
        return print_the_board(dict_board) # 1 2 3 | 4 X 6 | 7 8 9

list_board = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
print_the_board(dict_board)
dict_player_turn = {True:"X",False:"O"}
turn = True

while True:
    position = int(input("player {} turn : ".format("one" if turn else "two"))) # 5
    if dict_board[position] == "X" or dict_board[position] == "O":
        print("Already taken")
        continue
    change_board(position,dict_player_turn[turn])
    is_win = False
    for x,y,z in list_board:
            if dict_board[x] == dict_board[y] == dict_board[z]:
                is_win = True
                print("player {} win".format("one" if turn else "two"))
    if is_win:
        break
    is_draw = True
    for value in dict_board.values():
        if type(value) != str:
            is_draw = False
            break
    if is_draw:
        print("Game Draw")
        break
    turn = not turn