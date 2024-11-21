//leet21

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
  const dummy = { val: 0, next: null }; //creating a dummy node
  let node = dummy;
  //while both are non-empty
  while (list1 && list2) {
    //condition to check and sort
    if (list1.val < list2.val) {
      node.next = list1; //storing the node
      list1 = list1.next; // shifting the pointer
    } else {
      node.next = list2;
      list2 = list2.next;
    }
    node = node.next;
  }

  //edgecase: if one is non-null after the sort checks

  if (list1) {
    node.next = list1;
  } else {
    node.next = list2;
  }
  return dummy.next;
};
