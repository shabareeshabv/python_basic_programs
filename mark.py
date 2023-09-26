my_list=[['jay',100],['virus',85],['banasa',89],['jai',98]]
my_dict=dict(my_list)
print(my_dict)
marks=set(my_dict.values())
print(marks)

marks=sorted(marks)
print("sorted",marks)
sec_largest=(marks[-2])
for ele in my_list:
    print("ele value       ",ele)
    print("ele[1]       " ,ele[1])
    if (ele[1])==sec_largest:
      print(ele[0])