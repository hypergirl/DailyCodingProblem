This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

#arr=[3, 4, -1, 1]
arr=[1, 2, 0]
arr.sort()
s=set(arr)
for i in s:
    if i>=0:
        if (i+1) not in arr:
             print(i+1)
             break;
        
        
