import random

board = [random.randint(0,7) for i in range(8)]

def h(board):
    c=0
    for i in range(8):
        for j in range(i+1,8):
            if(board[i]==board[j] or abs(board[i]-board[j])==abs(i-j)):
                c+=1
    return c
def prt(board):
    for i in range(8):
        for j in range(8):
            if board[i]==j:
                print("Q", end = ' ')
            else:
                print(".",end=' ')
        print()
    print()
prt(board)
print(h(board))
while h(board)!=0:
    best = board[:]
    best_h = h(board)

    for i in range(8):
        for j in range(8):
            temp = board[:]
            temp[i]=j
            if h(temp)<best_h:
                best = temp[:]
                best_h = h(temp)
    if best == board:
        prt(best)
        print("is min solution ",h(best))
        break
    board = best[:]
    
        
        
        
