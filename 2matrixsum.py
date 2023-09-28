a=[[1,1,1],[2,2,2],[3,3,3]]
b=[[4,4,4],[5,5,5],[6,6,6]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
   # print("i value is ",i)
    for j in range(len(a[0])):
        print(j)
        result[i][j]=a[i][j]+b[i][j]
print(result)        
        