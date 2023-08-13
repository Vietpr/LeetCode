# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        temp = ListNode(0)
        current = temp
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        else:
            current.next = list2 
        return temp.next

    def linkedlist(self, lst):
        temp = ListNode(0)
        current = temp 
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return temp.next
    
    def printlinkedlist(self, head):
        result = []
        current = head 
        while current:
            result.append(current.val)
            current = current.next 
        return result

solution = Solution()
# testcase 1
list1 = solution.linkedlist([1,2,4])
list2 = solution.linkedlist([1,3,4])

merged_list = solution.mergeTwoLists(list1, list2)
output_is = solution.printlinkedlist(merged_list)
print(output_is)  # output1 is [1, 1, 2, 3, 4, 4]
# testcase 2
list1 = solution.linkedlist([])
list2 = solution.linkedlist([])

merged_list = solution.mergeTwoLists(list1, list2)
output_is = solution.printlinkedlist(merged_list)
print(output_is) # output 2 is []
# testcase 3
list1 = solution.linkedlist([])
list2 = solution.linkedlist([0])

merged_list = solution.mergeTwoLists(list1, list2)
output_is = solution.printlinkedlist(merged_list)
print(output_is) # output 3 is [0]

        



