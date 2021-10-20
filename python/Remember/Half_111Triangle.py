for row in range(1, 10):
    for i in range(10-row):
        print(" ",end=" ")
    for i in range(1, row):
        print(i,end=" ")
    for i in range (row, 0 , -1):
        print(i,end=" ")
    print()
       