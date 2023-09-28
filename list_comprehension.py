a=["asb",'huls','jndsa']
#for i in a:
 #   print(i.upper()) thi logic also same
new=[i.upper() for i in a]
print(new)

m =[i for i in range(10)]
print(m) 

k=[0,1,2,3,4,5,6,7,8,9]
new1=[]
for i in k:
    if i%2==0:
        new1.append(i)
print(new1) # the below logic same for this program


m1=[i for i in range(10) if i%2==0]
print(m1)
    