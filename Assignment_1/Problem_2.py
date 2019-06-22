#2A)

def Check(x = [1,2,3]):
    y = []
    for i in range(len(x)):
        if (len(x[i]) >= 2):
            if x[i][0] == x[i][len(x[i])-1]:
                y.append(x[i])
    return y
    

listlist = [[1,2,3], [1,1], [4,5,6,4], [2,1,2],]
# listlist = Check(listlist)
#print(Check(listlist))

#2B)
def Sortlist(x):
    x = Check(x)
    x.sort(key = len, reverse = False)
    return x


listlist = Sortlist(listlist)
print(listlist)

