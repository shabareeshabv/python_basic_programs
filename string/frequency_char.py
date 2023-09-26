string='hello hello'
for i in string:
    frequency=string.count(i)
    print(str(i) +str(frequency))    
    print("------------------------------------")  
    
    
string = "Yolo Life"

for i in string:
    frequency = string.count(i)
    print(str(i) +str(frequency), end=", ")   
    #another method 
string_1='bengalore'   
dict={}  
for i in string_1:
    if i in dict:
        dict[i]+=1
        
    else:
        dict[i]=1
print(dict)       
             
 