# submitted on leetcode:
# time: o(n), space: o(n)
# logic: palindrome means identical from both side
# so just traverse the list two times
# while traversing for first tim ego on pushing the val on stack
# and while traversing for second time compare the val on stack
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        first, second= head,head
        stack= []
        # traverse the whole list and put the data ele on stack
        while first:
            stack.append(first.val)
            first= first.next
            
        # now traverse again and keep comparing the currrent node val
        # with val on stack and keep on poping the ele from stack 
        # if matches till end(after this stack will become empty) 
        # means palindrome else not
        while second and (stack.pop()==second.val):
            second= second.next
        # now  if stack is empty(or second is pointing to None) 
        # means palindrome
        return stack==[]    # will return true if matches to the right side
                    # i.e if stack is empty then return true else return false


# concise way of writing 1st method
class Solution:
    def isPalindrome(self, head):
        first= head
        stack= []
        # traverse the whole list and put the data ele on stack
        while first:
            stack.append(first.data)
            first= first.next
        return stack== stack[::-1]


# method 2: Time- o(n), space- o(1)  (submitted on leetcode)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # first find the middle element
        # in case of even no of elements, midddle one will be 
        # the next middle
        middle= self.middleNode(head)
        print(middle.val)
        # now reverse the element from middle to end
        # after reversing 1st half will contain node till pre_slow of
        
        ReverseHead= self.ReverseByRecursion(None,middle)
        # ReverseHead= self.reverseList(middle)
        
        # temp = ReverseHead  # just for verifying the reverselist
        # # print(ReverseHead)
        # while temp!= None:
        #     print(temp.val)
        #     temp = temp.next
        
        # now compare both the 1st half and 2nd half
        return self.Compare(head,ReverseHead)
    
    def middleNode(self, head1):
        # slow, fast= None, self.head, self.head
        # pre_slow,slow, fast= None, self.head, self.head
        pre_slow,slow, fast= None, head1, head1
        # pre_slow will help in meging the  the two nodes
        # as it will point to last ele in 1st half after reversing the list
        
        # count= 0  # will count no of times loop will execute
                  # if count is odd means even no of elements
                  # if even means odd no of elements
        while fast and fast.next:
            # count+= 1
            pre_slow= slow
            slow= slow.next
            fast= fast.next.next
        # after this slow will point to middle ele in case of odd no
        # of ele and second middle in case no of ele is even
        # pre_slow will point to one node before slow i.e last ele of 1st half
        # so make pre_slow.next== None
        pre_slow== None
        return slow
            
    def ReverseByRecursion(self,pre, current):
        headreverse= None
        if current== None:
            headreverse= pre
        else:
            # Solution().ReverseByRecursion(current,current.next)  # this will return none at last since we are 
                                                                    # not storing the updated value of 'headreverse' 
            headreverse = Solution().ReverseByRecursion(current,current.next)
            current.next= pre
        return headreverse
        # print(headreverse.val)
    
    # def reverseList(self, middle1):
    #     pre,current,first= None,middle1,middle1 
    #     while current:
    #         first= current.next  
    #         current.next= pre    
    #         pre= current        
    #         current= first      
    #     return pre
    
    def Compare(self,pre_head,after_head):
        # first1, first2= self.head, self.ReverseList
        first1, first2= pre_head, after_head
        while first1 != None and first2 != None:
            if first1.val!= first2.val:
                return False
            first1= first1.next
            first2= first2.next
        return True

# method 3: time- o(n), space- o(n) 
# logic: traverse the list and store the value in as string
# now heck whether this string is palindrome or not
class Solution:
    def isPalindrome(self, head):
        str1= ""
        current= head
        while current:
            str1+= str(current.data)
            current= current.next
        return str1== str1[::-1]


# method 4: just traverse the list and right the no from both side
# i.e from left as well as right side 
# just same as we write the no from left and right
# way to write from right side= i*current.val + right_val and incr 'i in multiple of given base
# way to write from left side= left_val*base + current.val

# will only work for integers(also for very long input showing time limit exceeded on leetcode)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        i, right_val, left_val,current= 1,0,0, head
        while current:
            right_val= i*current.val + right_val   # writing from right side
            left_val= left_val*10 + current.val    # writing from left side
            i= i*10
            current= current.next
        return right_val== left_val