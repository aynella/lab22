def ex_10(n):
    s=set()
    for i in n:
        s.add(i-1)
        s.add(i+1)
    return s
print(ex_10({1, 5, 9}))
print(ex_10({2, 5, 7, 8, 10}))