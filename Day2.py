This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
  
  #arr=[1, 2, 3, 4, 5]
arr=[3, 2, 1]
l=[]

for i in range(len(arr)):
    s=1
    for j in range(len(arr)):
        if arr[i]!=arr[j]:
            s=s*arr[j]
    l.append(s)
    
