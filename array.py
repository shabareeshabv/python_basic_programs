def pair(arr,sum):
    arr.sort()
    left=0
    right=len(arr)-1
    while(left<=right):
        if (arr[left]+arr[right]>sum):
            right=right-1
        elif (arr[left]+arr[right]<sum):
            left=left+1
        elif (arr[left]+arr[right]==sum):
            print("values of pair are ",arr[left],arr[right])
            right=right-1
            print(right)
            left=left-1
            print(left)
        
arr=[5,6,7,8,9,19,21]        
sum=17
pair(arr,sum)
    