#1A)

def Add(x):
    if len(x) == 0:
        return x
    sum = 0
    for i in range(len(x)):
        sum += x[i]

    return sum
    
sum_list = [1,2,3]

#1B)

def Product(x):
    if len(x) == 0:
        return x
    multi = x[0]
    for i in range(1,len(x)):
        multi *= x[i]

    return multi
    


#1C)

def Largest(x):
    if len(x) == 0:
        return x
    y = x[0]
    for i in range(len(x)):
        if y < x[i]:
            y = x[i]
    
    return y



#1D)

print("Sum is {},  Multiplication is {}, Largest number is {}.".format( Add(sum_list), Product(sum_list), Largest(sum_list)))