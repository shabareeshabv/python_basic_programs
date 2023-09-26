exp = "(a-b)+[c*d]+{e/f}"
value=''
for i in exp:
    if ord(i) == 41 or ord(i) == 40 or ord(i) == 91 or ord(i) == 93 or ord(i) == 123 or ord(i) == 125:
       pass
    else:
        value+=i
print(value)        