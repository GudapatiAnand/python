rows=6
for i in range(rows):
    for j in range(i+1):
        print("*",end=" ")
    print()


rows=6
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()