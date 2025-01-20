class Solution(object):
    def addTwoNumbers(self, l1, l2):

        head = ListNode() 
        curr = head
        carry = 0
        
        while l1 != None or l2 != None or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            column_sum = l1_val + l2_val + carry
            carry = column_sum // 10
            new_node = ListNode(column_sum % 10)
            curr.next = new_node
            curr = new_node
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return head.next

# ListNode() is already defined by LeetCode in this case.
      
# https://leetcode.com/problems/add-two-numbers/
