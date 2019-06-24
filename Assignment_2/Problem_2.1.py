def Split(arr, q):
    D = {}
    temp = []
    Sum = 0
    for i in q:
        for j in range(i[0], i[1]+1):
            
            if i[0] == j:
                pass
            else:

                D[tuple(arr[i[0]:j])] = 0
                D[tuple(arr[j:i[1]+1])] = 0
        for key, val in D.items():
            for u in range(len(key)):
                Sum = (key[u] + Sum)

                D[key] = Sum
                
            Sum = 0
        
    

       

    return D

arr = [1, 1, 2, 3] 

q = [[1, 3]]

print(Split(arr,q))