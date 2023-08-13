class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        start_list = ListNode(0)
        result = start_list
        storage_sum = 0
        while l1 or l2 or storage_sum:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            _sum = x + y + storage_sum
            storage_sum = _sum // 10
            result.next = ListNode(_sum % 10)
            result = result.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return start_list.next

# Hàm trợ giúp để tạo danh sách liên kết từ một mảng
def createLinkedList(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Hàm trợ giúp để in danh sách liên kết
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

if __name__ == "__main__":
    l1_vals = input("Enter the number of l1: ").split()
    l1 = createLinkedList([int(val) for val in l1_vals])

    l2_vals = input("Enter the number of l2: ").split()
    l2 = createLinkedList([int(val) for val in l2_vals])
    
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    print("Kết quả:")
    print("l1 =", end=" ")
    printLinkedList(l1)
    print("l2 =", end=" ")
    printLinkedList(l2)
    print("Output =", end=" ")
    printLinkedList(result)
