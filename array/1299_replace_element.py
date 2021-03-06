# # 1st method(myslef): Brute force but haven't get accpeted due to time limit 
# # but gives correct output for all cases
# # this approach gives best case: o(n) when maximum element is last or 2nd last
# # for above case there is no need of for loop
# # and without 1st for loop , answer will be always correct, there is no need 
# # of 1st for loop. just replace 'k' with '0' in arr[k:n-1] in 2nd for loop
arr = [4,9,8,4,7]
n= len(arr)
#find the index of maximum element
k=arr.index(max(arr))
#arr[n-1]= -1  # writing here this will lead to wrong answer 
#replacing every element on left side of maximum value with maximum value
for i in range(0,k):
    if(i!= n-1):
        arr[i]= arr[k]
#replacing every element from maximum element to n-2(except last) 
# index element with greatest element on their right side
for num in arr[k:n-1]:
    # print(arr[k])
    greatest= -1000000
    j=k+1
    while(j<=n-1):
        if(arr[j]>=greatest):
            greatest= arr[j]
        j+= 1
    arr[k]= greatest
    k+= 1
arr[n-1]= -1
print(arr)


# # 2nd method(normal brute force): modified of 1st methode(commented lines)
# arr = [4,9,8,4,7]
# n= len(arr)
# k=0
# for num in arr[k:n-1]:
#     greatest= -1000000
#     j=k+1
#     while(j<=n-1):
#         if(arr[j]>=greatest):
#             greatest= arr[j]
#         j+= 1
#     arr[k]= greatest
#     k+= 1
# arr[n-1]= -1
# print(arr)

# # simple and straight foward brute force
# arr = [4,9,8,4,7]
# n= len(arr)
# for i in range(0,n-1):
#     greatest= -1000000
#     k= i+1
#     while(k<=n-1):
#         if(arr[k]>=greatest):
#             greatest=arr[k]
#         k+= 1
#     arr[i]= greatest
# arr[n-1]= -1
# print(arr)


# brute force but very concise and simple: Accepted 
# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         n= len(arr)
#         for i in range(n-1):
#             arr[i]= max(arr[i+1:])
#         arr[n-1] = -1
#         return arr


# 2nd method- time: o(n), space= o(n)
# logic: tranverse from right to left and store the element with max_ele_seen_so_far
# comparing the element while iterating
# and replace the iterating element with max_ele_seen_so_far

arr = [17,18,5,4,6,1]
n= len(arr)
max_ele_seen_so_far= arr[n-1]
arr[n-1]= -1
for i in range(n-2,-1,-1):
    temp=arr[i]
    arr[i]= max_ele_seen_so_far
    if(temp>=max_ele_seen_so_far):
        max_ele_seen_so_far= temp
print(arr)

# another method:
def LargerElement(arr,n):
    stack= [] # will store the maximum ele from right side till now
            # stack will contain exactly opne or no ele always
    ans= []
    for i in range(n-1,-1,-1):
        if stack== []:  # since we are poping in above steps so we have to check for empty stack
                        # empty stack means either it is the largest ele or the last ele
            ans.append(-1)
            stack.append(arr[i])
        elif stack[-1]> arr[i]:  
            ans.append(stack[-1])
        else: # means new greater ele found
            ans.append(-1)
            stack.pop()
            stack.append(arr[i])
    # now print the ans in reverse to get the ans
    for i in range(n-1,-1,-1):
        print(ans[i], end=" ")

# another way of writing above code
# just exactly same code as replacing by nextLargerElement in right 
# just we have commented one line in 'else' condition of that code

def LargestRight(arr,n):
    stack= [] # will store the all the larger ele till index 'i'
              # no maximum then it will become empty
    ans= []
    # traverse the array from right to left
    for i in range(n-1,-1,-1):
        while(stack and stack[-1]<= arr[i]):
                stack.pop()
        if stack== []:  # since we are poping in above steps so we have to check for empty stack
                        # empty stack means either it is the largest ele or the last ele
            ans.append(-1)
            stack.append(arr[i])
        else:  # means stack top is greater than arr[i]
            ans.append(stack[-1])
            # stack.append(arr[i])  # after uncommenting it will give ans for nextgreater ele on right
    for i in range(n-1,-1,-1):
        print(ans[i], end=" ")

arr= [0,1,8,3,2,4,6,7]
LargestRight(arr,8)


# another method: better one-concise way of above methods (16/04/2022)
# traverse from right to left and only store the maximum ele in the stack 
# i.e stack will contain only one ele always at any point 
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n= len(arr)
        if n== 1:
            return [-1]
        stack, ans= [], []
        # initialise for last ele
        stack.append(arr[n-1])
        ans.append(-1)
        for i in range(n-2,-1,-1):
            # if arr[i]> stack measn arr[i] is the maximum ele on RHS till now
            # so just pop the stack top and append 'poped one' to the ans
            # poped will be the greatest for arr[i] and all the ele so far
            if arr[i]> stack[-1]:
                temp= stack.pop()
                ans.append(temp)
                # append arr[i] to the stack since arr[i] is the greatest till now
                stack.append(arr[i])
            else:  # means top of the stack is the greatest . so no need to append arr[i] in the stack
                ans.append(stack[-1])
        return ans[::-1]

