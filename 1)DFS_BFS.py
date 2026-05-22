graph  = {
    1:[3,2],
    3:[5,7],
    5:[],
    2:[4,5],
    4:[6],
    6:[],
    7:[]
    }

node = int(input("starting node"))
goal = int(input("goal"))
c = int(input("0 for bfs and -1 for dfs"))
visited = {node}
stack = [(node,[node])]

while stack:
    n,path = stack.pop(c)

    if n==goal:
        print("goal",path)
        break

    for x in graph[n]:
        if x not in visited:
            stack.append((x,path+[x]))
            visited.add(x)
else:
    print("no state found")



#            1
#          /   \
#         2     3
#       /   \ /   \
#      4     5     7
#      |
#      6
''' 
BFS : - FIFO(First in First out)
      - Queue
      1 [2, 3]
      2 [3, 4, 5]
      3 [4, 5, 7]
      4 [5, 7, 6]
      5 [7, 6]
      7 [6]
      6 [BFS complete...]
---------------------------------------
---------------------------------------
DFS : - LIFO(Last in First out) 
      - Stack
      1 [2, 3]
      3 [2, 5, 7]
      7 [2, 5]
      5 [2]
      2 [4]
      4 [6]
      6 [DFS complete...]

'''
#By - K.Sohith 😊😉
