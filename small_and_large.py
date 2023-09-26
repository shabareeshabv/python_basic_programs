a=[2,54,6,5,6,5,4,333,4,5,1]
max=a[0]
small=a[0]
for i in range(len(a)):
    if a[i] > max:
        max=a[i]
    elif a[i] < max:
         small=a[i]
print(max)     
print(small)   
             