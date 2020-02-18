def ex_3(n, i):
    return n[:i]+[j*j for j in n[i:]]
print(ex_3([10, 3, 4, 5, 9], 2))
print(ex_3([9, 0, 12, 3, 4, 56, 9, 16], 6))
