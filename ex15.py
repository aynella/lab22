def ex_15(a):
    answer=0
    for i in  a[1::2]:
        if(i%2==1):
            answer += 1
    return answer
print(ex_15([0,3,11,2,44,23,4]))
print(ex_15([22,23,24,33,34,35]))