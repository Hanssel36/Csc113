def two(arr, q):

    
    D = { tuple(q[0]): arr,  tuple(q[1]): arr }

    

    return D



arr = [1, 1, 2, 3] 

q = [[0, 1], [1, 3], [1, 2]]

print(two(arr,q))