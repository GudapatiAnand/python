#sets and set methods
#anand={1,1,2,3,3,4,5,4,829,575,229,348,19}
#print(type(anand))
#print(anand)
#anand.add(235)
#anand.update({1,88,22,66,78,5,4,"python"})
#anand.remove(229)
#anand.pop()
#anand.clear()
#b=anand.copy()
#print(b)


#set operations
#set1={1,2,3,4,5}
#set2={4,5,6,7,8}
#print(set1.union(set2))
#print(set1.intersection(set2))
#print(set1.difference(set2))
#print(set1.symmetric_difference(set2))
#set1={1,2,3}
#set2={1,2,3,4,5}
#print(set1.isdisjoint(set2))
#print(set1.issubset(set2))
#print(set2.issuperset(set1))


# for i in {1,2,3,4,5,6}:
#     if i==1:
#         print("yes")
#         break
#     else:
#         print("false")    


#frozenset
j=[1,2,3,4,5]
print(type(j))
d=frozenset(j)
print(list(d))