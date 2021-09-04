#Given a list of numbers and a number k, 
#return whether any two numbers from list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, 
#return true since 10 + 7 is 17.

arr=[10]
k=17
a=False
if(len(arr)>=2):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]+arr[j]==k):
                a=True
                break;
print(a)
