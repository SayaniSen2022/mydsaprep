class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #create a dummy node
    dummy = ListNode(0, head) # dummy -> 1 -> 2 -> ...
    left, right = dummy, head
    while n > 0 and right:
      right = right.next
      n -= 1
    while right:
      left = left.next
      right = right.next
    
    #deleting the nth node and adjusting the pointer
    left.next = left.next.next
    return dummy.next
  
def build_link_list(arr):
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

if __name__ == "__main__":
  sol = Solution()
  head = build_link_list([1,2,3,4,5,6])
  sol.removeNthFromEnd(head, 2)
  print_list(head)
