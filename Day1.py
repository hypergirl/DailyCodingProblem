#Given a list of numbers and a number k, 
#return whether any two numbers from list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, 
#return true since 10 + 7 is 17.

def twoSum(nums, target):
    for i in range(len(nums)):
        
        out=target-nums[i]
            
        if(out in nums[i+1:]):
            return [i,nums.index(out,i+1)]
        
a=twoSum([3,4,1,2],7)
print(a)
