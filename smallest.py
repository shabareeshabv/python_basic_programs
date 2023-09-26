a=[2,4,66,55,4,3,3,33,]
small=a[0]
for i in range(len(a)):
      print(a[i])
      if a[i]< small:
        #print(a[i])
        small=a[i]
print(small)        