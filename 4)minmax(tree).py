tree = [
    [
        [
            [80, 30], [25, 35]
        ],
        [
            [55, 20], [5, 65]
        ]
    ],
    [
        [
            [40, 10], [70, 15]
        ],
        [
            [50, 45], [60, 75]
        ]
    ]
]

def min_max(node,is_max):
    if type(node) == int:
        return node

    if is_max:
        best = -1000
        for child in node:
            result = min_max(child,False)
            if result>best:
                best = result
                print(best,"max")
        return best
    else:
        best = 1000
        for child in node:
            result = min_max(child,True)
            if result < best:
                best = result
                print(best,"min")
        return best

x = min_max(tree,True)
print("best value : ",str(x))

              
