import random

boards = [[random.randint(0,7) for i in range(8)]for j in range(4)]

def f(board):
    c=0
    for i in range(8):
        for j in range(i+1,8):
            if(board[i]==board[j] or abs(board[i]-board[j])==abs(i-j)):
                c+=1
    return 28-c
def prt(board):
    for i in range(8):
        for j in range(8):
            if board[i]==j:
                print("Q", end = ' ')
            else:
                print(".",end=' ')
        print()
    print()



for xdcfhjk in range(50):
    boards = sorted(boards,key=f,reverse=True)
    p1,p2 =  boards[0],boards[1]

    if f(p1) == 28:
        print("solution found")
        prt(p1)
        break

    if random.random() < 0.3:
        z = random.randint(1,6)
        new_board = p1[:z]+p2[z:]

        boards[-1] = new_board[:]
print("best soultion after 50 mutations : ")
boards = sorted(boards,key=f,reverse=True)

prt(boards[0])
print(f(boards[0]))
