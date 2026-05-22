tree = [
    [ [2, 3], [5, 9] ],   # B -> D=[2,3], E=[5,9]
    [ [0, 1], [7, 5] ]    # C -> F=[0,1], G=[7,5]
]

def min_max(node,alpha,beta,is_max):
    if type(node) == int:
        return node
    if is_max:
        best = -9999
        for child in node:
            result = min_max(child,alpha,beta,False)

            if result>best:
                best = result
            if best > alpha :
                alpha = best
            if alpha > beta:
                print("purning")
                break
        return best
    else:
        best = 9999
        for child in node:
            result = min_max(child,alpha,beta,True)

            if result<best:
                best = result
            if best < alpha :
                alpha = best
            if alpha > beta:
                print("purning")
                break
        return best
resultt = min_max(tree,-999,999,True)
print(resultt)
