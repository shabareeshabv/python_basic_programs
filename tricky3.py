l1=[2,3,4,5,6] #[1,9]
output=[]#[1]
sum1=0
output.append(l1[0])
print(output)
for idx in range(1,len(l1)):
    print("index value is ",idx)
    sum1+=l1[idx]
output.append(sum1) 
print(output)   
