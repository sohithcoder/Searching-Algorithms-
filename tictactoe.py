    import math

board = [0,0,0,
         0,0,0,
         0,0,0]

def check_win(board):
    win_states = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for state in win_states:
        if board[state[0]]==board[state[1]]==board[state[2]] !=0:
            return board[state[0]]
    return 0

def min_max(node,is_max):
    win = check_win(node)
    if win == 1: return 10
    if win == -1 : return -10
    if 0 not in node  : return 0

    if is_max:
        best = -1000

        for i in range(9):
            if node[i]==0:
                node[i]=1
                result = min_max(node,False)
                node[i]=0
                best = max(result,best)
        return best
    else:
        best = 1000

        for i in range(9):
            if node[i] == 0:
                node[i] =-1
                result = min_max(node,True)
                node[i] = 0
                best = min(result,best)
        return best
    
def prt(b):
    for i in range(9):
        print(b[i],end = ' ')
        if (i+1)%3 == 0:
            print()
prt(board)

while 0 in board and check_win(board) ==0:
    move = int(input("enter 0-8"))
    board[move] = -1
    prt(board)

    if 0 not in board or check_win(board) !=0:
        break

    best = -1000
    ai_move = -1
    for i in range(9):
        if board[i] ==0:
            board[i] =1
            result = min_max(board,False)
            board[i] = 0
            if result>best:
                best = result
                ai_move = i
    board[ai_move] = 1
    prt(board)

win = check_win(board)
if win ==1:print("Ai win")
elif win ==-1:print("you win")
else:print("draw")

    
            


    
    
