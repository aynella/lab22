def ex_11(a, b):
    for i in b:
        if i in a:
            a.remove(i)
    return a
print(ex_11({1,2,3,4},{3,5,7}))
print(ex_11({12,15,16,20,95},{1,2,3,16,17,20}))