def ex_2(l):
    new=[]
    for i in range (0, len(l), 2):
        new.append(l[i])
        return new
l=[10, 3, 4, 5, 9]
print(ex_2(l))