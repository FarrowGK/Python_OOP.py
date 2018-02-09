tuple1 = (1,2,3)
list1 = [1,2,4]
tl1 = [1, 2, tuple1]
test1 = sum(tuple1)
test2 = sum(list1)
test3 = sum(list1[sum(tuple1)])
print test1
print test2
print test3