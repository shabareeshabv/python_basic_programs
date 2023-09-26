my_dict={'orage':'fruits','potato':'vegitable','banana':'fruits'}
output={}
for ele in my_dict:
 
    if my_dict[ele] not in output:
        
     
        output[my_dict[ele]]=[ele]
    else:
        output[my_dict[ele]].append(ele)    
   
print(output)   #for question check the ouput of the program   