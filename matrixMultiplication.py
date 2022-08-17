#matrix Multiplication

l1=[[12,7,3],
    [4,5,6],
    [7,8,9]]
l2=[[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
l3=[[0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]

for i in range(len(l1)): #Row of l1
    for j in range(len(l2[0])): #Column of l2
        for k in range(len(l2)): #Row of l2
            l3[i][j]+=l1[i][k]*l2[k][j]


for r in l3:
    print(r)
