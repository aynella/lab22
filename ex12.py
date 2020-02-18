def exercise_12(my_list:list):
     some_set=set()
     for i in my_list:
         if i in some_set:
             some_set.add(i**2)
     else:
        some_set.add(i)
     return some_set
print(exercise_12([1,2,2]))
print(exercise_12([1,2,2,3,4]))

