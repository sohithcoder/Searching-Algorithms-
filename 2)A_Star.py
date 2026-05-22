graph_weighted = {
    's': [('a',3), ('b',2)],     
    'a': [('s',3), ('c',1), ('d',3), ('b',3)],  
    'b': [('s',2), ('c',5), ('d',3), ('a',3)],  
    'c': [('a',1), ('b',5), ('d',2)],  
    'd': [('a',3), ('b',3), ('c',2)]
}

h = {'s':1, 'a':3, 'b':3, 'c':0, 'd':0}

node = (input("start"))
goal = (input("goal"))


stack = [(h[node],0,node,[node])]

while stack:
    min_i = 0
    for i in range(0,len(stack)):
        if stack[i][0] < stack[min_i][0]:
            min_i = i
    f,g,n,path = stack.pop(min_i)

    if n == goal :
        print("path found :", path)
        print(g)
        break
    for x , cost in graph_weighted[n]:
        gn = g+cost
        fn = gn + h[x]
        stack.append((fn,gn,x,path+[x]))
