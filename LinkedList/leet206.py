# Given the head of a singly linked list, reverse the list, and return the reversed list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # iteration
    # eliminate the edge cases
    if not head:
      return None
    curr, prev = head, None
    while curr:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp
    return prev

def build_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next


def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# 🔽 Run
if __name__ == "__main__":
    sol = Solution()

    head = build_linked_list([1,2,3,4,5])

    reversed_head = sol.reverseList(head)

    print_list(reversed_head)