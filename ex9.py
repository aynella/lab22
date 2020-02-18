def ex_9(n):
    for i in n:
        if type(i)== list or type(i)==dict or type(i)==set:
            return True
    return False
print(ex_9((10, 2, 5, [4, 8, 2], 3, 5)))
print(ex_9((5, 2.5, 8, 4, 'Hi', -5, True, 6)))