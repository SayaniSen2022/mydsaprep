class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class LinkList {
  constructor() {
    this.head = null;
    this.size = 0;
  }

  insertAtHead(val) {
    const node = new Node(val);

    node.next = this.head;
    this.head = node;
    this.size++;
  }
  insertAtTail(val) {
    let node = new Node(val);
    if (this.head === null) {
      this.head = node;
    }
    let curr = this.head;
    while (curr.next) {
      curr = curr.next;
    }

    curr.next = node;
    this.size++;
  }
  insertAtIndex(val, index) {
    const node = new Node(val);

    if (index === null || index > this.size || index === undefined || index < 0)
      return;

    let curr, temp;
    let count = 0;

    curr = this.head;

    while (count < index - 1) {
      curr = curr.next;
      count++;
    }
    temp = curr.next;
    curr.next = node;
    node.next = temp;
    this.size++;
  }

  printList() {
    let curr = this.head;
    while (curr) {
      console.log(curr.val);
      curr = curr.next;
    }
  }
}

const List1 = new LinkList();

List1.insertAtHead(5);
List1.insertAtHead(55);
List1.insertAtHead(555);
List1.insertAtHead(5555);
List1.insertAtTail(100);
List1.insertAtIndex(2, 3);
List1.printList();
