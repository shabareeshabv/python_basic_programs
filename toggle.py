string="shabareesHA"
string1=str()
for i in string:
   # print(i)
    if i.isupper():
        #print(i)
        i=i.lower()
        #print("ivalue ",i)
        string1=string1+i
        #1print("string1",string1)
        
    else:
       i= i.upper()
      
       print(string1)
    string1=string1+i 
print(string ,"is",string1)           