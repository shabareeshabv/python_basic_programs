a=[[2,2,2],[3,3,3],[4,4,4]]
b=[[2,3,4,5],[2,3,4,5],[2,3,4,5]]
result=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
           # print("k is ",k)
            result[i][j] +=a[i][k] *b[k][j]
print(result)            