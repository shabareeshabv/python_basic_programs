array=[4,2,1,7,8,989,3,32,2]
n=len(array)
firsthalf=sorted(array[:n//2])
secondhalf=sorted(array[n//2:],reverse=True)
result=firsthalf+secondhalf
print(result)