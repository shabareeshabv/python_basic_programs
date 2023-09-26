string1=input("enter the string")
string1=string1.split()# split is deside the wheather it is string  or char # split is main part of program
print(string1)
counts=dict()
for char in string1:
    if char in counts:
        counts[char]+=1
    else:
        counts[char]=1 
print(counts) 
word=[]
for char in counts:
    print("keys value",char)
    if counts[char]>=2:
        word.append(char)
print("word",word)

 
## this program for number in string
'''
print("#########################################")
string="jai hanuman"                     
dict={}
for i in string:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)   '''