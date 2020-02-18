def ex_13(n):
    s=set(n)
    answer=0
    for i in s:
        if(n.count(i)%2==1):
            answer +=1
    return answer <=1
print(ex_13([1,2,3,4,1]))
print(ex_13([1,2,3,1,2]))