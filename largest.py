a=[10,20,30,40]
b=a[0]
for i in range(len(a)):
    if a[i]>b:
        b=a[i]
print(i) 


####################################  
a = [10, 89, 9, 56, 4, 80, 8]
max_element = a[0]

for i in range(len(a)):
  if a[i] > max_element:
     max_element = a[i]

print (max_element)     