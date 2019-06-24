def exist( S, L, R):
    D = {}
    D2 = {}
    y = []
    M = []
    mul = 1
    for i in range(len(S)):
        if i == L and i != R+1:
            L = L+1
            M.append(S[i])
        else:
            y.append(S[i])
    
    D = {i:y.count(i) for i in M}
    D2 = {i:M.count(i) for i in M} 
    for val in D:
        if D[val] < D2[val]:
            return 0
        else:
            mul = D[val]*mul
    return mul


s = "cabcaab"

print(exist(s,1,4))