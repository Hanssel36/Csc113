def two(arr, q):

    
    D ={ }
    Sum = 0
   

    for i in q:
        D[tuple(i)] = 0

    for i in D:
        for j in range(i[0],i[1]+1):
            Sum = arr[j] + Sum
            D[i] = Sum
            
        Sum = 0

    for key,val in D.items():
        if val%2 != 0:
            print("No")
        else:
            for j in range(key[0], key[1]+1):
                if val/2 == arr[j]:
                    print("Yes")
                    break
                else:
                    print(arr[j])
                    print("No")
                    break

    

    return



arr = [1, 1, 2, 3] 

q = [[0, 1], [1, 3], [1, 2]]

print(two(arr,q))