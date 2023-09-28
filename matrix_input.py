x=int(input("enter the value for row"))
y=int(input("enter the value for colomn"))
mat=[]
for i in range(0,x):
    mat.append([])
    print(mat)
for i in range(0,x) :
    for j in range(0,y):
        mat[i].append([j]) 
        mat[i][j]=0
print(mat)
for i in range(0,x):
    for j in range(0,y):
        print("enter the value in row",i+1,'   col',j+1)
        mat[i][j]=int(input())

print((mat))        
        
            
        
           
