#sets and set methods
# anand={1,1,2,3,3,4,5,4,829,575,229,348,19}
# print(type(anand))
# print(anand)
# anand.add(235)
# print(anand)
# anand.update({1,88,22,66,78,5,4,"python"})
# print(anand)
# anand.remove(229)
# print(anand)
# anand.pop()
# print(anand)
# anand.clear()
# print(anand)
# b=anand.copy()
# print(b)


#set operations
# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# print(set1.union(set2)) # it will print all the elements in both the sets
# print(set1.intersection(set2)) # it will print the common elements from both the sets
# print(set1.difference(set2)) # it will print only set1 elements which is not common in both the sets.
# print(set2.difference(set1)) # it will print only set2 elements which is not common in both the sets.
# print(set1.symmetric_difference(set2)) # it will remove common elements and print remaining elements from both the sets.
set1={1,2,3}
set2={1,2,3,4,5}
# print(set1.isdisjoint(set2)) # the elements in both the sets should be different then it will print true
# print(set1.issubset(set2)) #it will print true if all the elements in set1 should present in set2 and it can be more elements in set2
print(set2.issuperset(set1)) #it will print true if all the elements in set1 present in set2


# for i in {1,2,3,4,5,6}:
#     if i==1:
#         print("yes")
#         break
#     else:
#         print("false")    


#frozenset
# j=[1,2,3,4,5]
# print(type(j))
# d=frozenset(j)
# print(list(d))