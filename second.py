arr = [10, 13, 17, 11, 34, 21]
first = arr[0]
second = arr[1]  # Initialize second with the second element of the array

for i in range(0, len(arr)):
    
   if arr[i] < first:
       second = first  # Update second with the previous value of first
       first = arr[i]
    
   elif arr[i] != first and arr[i] < second:
     second = arr[i]

print(second)