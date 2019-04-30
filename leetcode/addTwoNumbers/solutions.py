class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3_head_node = ListNode(0)
        l3_current_node = l3_head_node

        l1_node = l1
        l2_node = l2
        tens_digit =0
        while l1_node or l2_node:
            data1 = data2 = 0
            if l1_node:
                data1 = l1_node.val
            if l2_node:
                data2 = l2_node.val
            sum = int(data1 + data2 + tens_digit)
            tens_digit = int(sum/10)

            l3_next_node = ListNode(sum%10)
            l3_current_node.next = l3_next_node
            l3_current_node = l3_next_node

            if(l1_node):
                l1_node = l1_node.next
            if(l2_node):
                l2_node = l2_node.next
        if tens_digit > 0:
            l3_next_node = ListNode(tens_digit)
            l3_current_node.next = l3_next_node
        return l3_head_node.next
