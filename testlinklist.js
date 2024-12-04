class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class Solution {
  mergeLists(list1, list2, list3) {
    // TODO: Implement this method
    const res1 = this.merge(list1, list2);
    this.printList(res1);
    console.log("XXXXX");
    const finalRes = this.merge(res1, list3);
    return finalRes;
  }

  merge(list1, list2) {
    const dummy = new ListNode();
    let node = dummy;

    while (list1 && list2) {
      if (list1.val < list2.val) {
        node.next = list1;
        list1 = list1.next;
      } else {
        node.next = list2;
        list2 = list2.next;
      }
      node = node.next;
    }
    if (list1) {
      node.next = list1;
    }
    if (list2) {
      node.next = list2;
    }
    return dummy.next;
  }

  printList(head) {
    let current = head;
    while (current) {
      console.log(current.val);
      current = current.next;
    }
  }
}

// Test cases
function runTests() {
  const solution = new Solution();

  // Create test lists
  console.log("Test Case 1: Basic merge");
  const list1 = new ListNode(1);
  list1.next = new ListNode(4);
  list1.next.next = new ListNode(7);

  const list2 = new ListNode(2);
  list2.next = new ListNode(5);
  list2.next.next = new ListNode(8);

  const list3 = new ListNode(3);
  list3.next = new ListNode(6);
  list3.next.next = new ListNode(9);

  const result1 = solution.mergeLists(list1, list2, list3);
  solution.printList(result1);
  // Expected:
  // 1
  // 2
  // 3
  // 4
  // 5
  // 6
  // 7
  // 8
  // 9

  //   console.log("\nTest Case 2: One empty list");
  //   const list4 = new ListNode(1);
  //   list4.next = new ListNode(3);

  //   const list5 = new ListNode(2);
  //   list5.next = new ListNode(4);

  //   const result2 = solution.mergeLists(list4, list5, null);
  //   solution.printList(result2);
  // Expected:
  // 1
  // 2
  // 3
  // 4

  //   console.log("\nTest Case 3: All empty lists");
  //   const result3 = solution.mergeLists(null, null, null);
  //   solution.printList(result3);
  // Expected: (nothing printed - empty list)
}

runTests();
