dict1={'jhon':89 ,'lisa':99}
dict2 ={'lisa':94,"peter":78}
#print(dict1|dict2) logic one
#print({**dict1,**dict2}) #logic 2
dict3=dict2.copy()
dict3.update(dict1)
print(dict3)

