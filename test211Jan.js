/**
 Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false. 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 */

// Definition for singly-linked list node
class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var solution = function (head) {
  // Write your solution here
  let [fast, slow] = [head, head];

  while (fast.next) {
    fast = fast.next.next;
    slow = slow.next;

    if (fast === slow) {
      return true;
    }
  }

  return false;
};

// Helper function to create linked list with cycle
function createLinkedList(values, pos) {
  if (!values.length) {
    return null;
  }

  // Create nodes
  const nodes = values.map((val) => new ListNode(val));

  // Link nodes
  for (let i = 0; i < nodes.length - 1; i++) {
    nodes[i].next = nodes[i + 1];
  }

  // Create cycle if pos is valid
  if (pos >= 0 && pos < nodes.length) {
    nodes[nodes.length - 1].next = nodes[pos];
  }

  return nodes[0];
}

// Test cases
function runTests() {
  // Test case 1: [3,2,0,-4], pos = 1
  const head1 = createLinkedList([3, 2, 0, -4], 1);
  console.assert(solution(head1) === true, "Test case 1 failed");

  // Test case 2: [1,2], pos = 0
  const head2 = createLinkedList([1, 2], 0);
  console.assert(solution(head2) === true, "Test case 2 failed");

  // Test case 3: [1], pos = -1
  const head3 = createLinkedList([1], -1);
  console.assert(solution(head3) === false, "Test case 3 failed");

  console.log("All test cases passed!");
}

// Run the tests
runTests();
