string="shabaree253254"
result=0
for i in string:
    if  ord(i)>=65 and  90<=ord(i):
        pass
    else:
        result=result+int(i)
print(result)   

String = "Daya123Ben456"
#initialize integer variable
sum1 = 0
for i in String:
    #check if values lies between range of numbers or not
    #according to ascii tale
    if ord(i) >= 48 and ord(i) <= 57:
        #convert it to integer and add
        sum1 = sum1 + int(i)
print('Sum is :' + str(sum1)) 