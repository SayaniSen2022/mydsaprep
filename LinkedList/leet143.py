# Reorder List: You are given the head of a singly linked-list. The list can be represented as: L0 → L1 → … → Ln - 1 → Ln

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:    #Do not return anything, modify head in-place instead.
    #find middle : fast and slow pointers
    slow, fast = head, head.next
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    #reverse the second half
    #the beginning of the second half
    second = slow.next
    slow.next = prev = None
    while second:
      temp = second.next
      second.next = prev
      prev = second #holds the value of the second half's head
      second = temp

    #merge the two halves
    first, second = head, prev #heads of the 2 halves
    while second:     #since second half could be shorter we check for the following
      temp1, temp2 = first.next, second.next #since we are breaking the links we need to store them in temporary variables
      first.next = second
      second.next = temp1
      first, second = temp1, temp2 #shifting the pointers


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

#Run
if __name__ == "__main__":
    sol = Solution()

    head = build_linked_list([1,2,3,4,5])

    sol.reorderList(head)

    print_list(head)