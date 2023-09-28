
def max_min(ar):
    max=ar[0][0]
    min=ar[0][0]
    for i in range(3):
        for j in range(3):
            if ar[i][j]>max:
                max=ar[i][j]
            if ar[i][j]<min:
                min=ar[i][j]    
    print("maximun",max ,"minimum",min)            


a=[]
for i in range(3):
    b=[]
    for j in range(3):
        j=int(input("enter the number ["+str(i)+"]["+str(j)+"]"))
        b.append(j)
        print("b value is",b)
    a.append(b) 
    print("a value is ",a)  
print()     
print("matrix is")
for i in range(3):
    for j in range(3):
        print(a[i][j],end=" ")
    print()    
max_min()    