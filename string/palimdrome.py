number=int(input("enter the number"))
temp=number
remainder=0
while(temp>0):
    div=temp%10
    remainder=remainder*10+div
    temp//=10
    
if(number==remainder):
    print("palindrome")
else:
    print("not palindrome")        