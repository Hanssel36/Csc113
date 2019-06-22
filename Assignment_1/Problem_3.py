#3A)

def RemoveDuplicates(x):
    y = []
    for i in range(len(x)):
        if y.count(x[i]) >= 1:
            pass
        else:
            y.append(x[i])

    return y


Test = ['a', 'b', 'a', 'd', 'b']

Test = RemoveDuplicates(Test)
print(Test)

#3B)

def Permutation(x):
    y = []
    t = []
    if len(x) == 0 or len(x) == 1:
        return x

    if len(x) == 2:
        y.insert(0,list(x))
        x[0], x[1] = x[1], x[0]
        y.append(x)
        return y
    else:
        for i in range(len(x)):
            x[0], x[i] = x[i], x[0]
            y = Permutation(x[1:])
            for j in range(len(y)):
                y[j].insert(0,x[0])
            t = t+y     
    return t
Test2 = ['a', 'b', 'c']

print(Permutation(Test2))
