n=int(input("enter the number"))
first=0
second=1
for i in range(0,5+1):
   
    number=first #0
    print( number,end="")
    
    first=second #1
    second=number+first
     