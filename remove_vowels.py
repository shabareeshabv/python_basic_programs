string="shabaree"
string2="aeiou"
result=''
for i in string:
    if i not in string2:
        result=result+i
print(result)  


string2="jai kundapura"      
vowels="aeiou"        
for x in string2:
    if x in vowels:
        result=string2.replace(x,'')
print("result is",result)  

value="shabareesha deepu"   
result=value          
vowels="aeiou"
for x in value:
    if x in vowels:
        result=result.replace(x,'')
print (result)       