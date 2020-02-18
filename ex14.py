def ex_14(n,i):
    s=set()
    for t in n:
        if t>1:
            s.add(t)
    return s
print(ex_14([11,2,44,23], 10))
print(ex_14([1,200,45,-67], 45))
