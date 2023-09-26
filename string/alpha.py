char='2'#str(input())
if char.isalpha():
    print(char,"is an alphabet")
else:
    print(char,"is  not alphabet")     
    
    
ch ='3' #input("Enter any character: ")

# check charater is alphabet or not
if((ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >= 97 and ord(ch) <= 122)):
    print(ch, "is an Alphabet.")
else:
    print(ch, "is not an Alphabet.")    