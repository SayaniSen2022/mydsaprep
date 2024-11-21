class CallNode {
  constructor(phoneNumber) {
    this.phoneNumber = phoneNumber;
    this.next = null;
    this.prev = null;
  }
}

class CallLog {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
    this.maxSize = 5; // Maximum size limit
  }

  // Candidate should implement this method
  call(phoneNumber) {
    // TODO: Implement this method to:
    // 1. If number exists, move it to front
    // 2. If number doesn't exist:
    //    - Add it to front
    //    - If size exceeds 5, remove tail

    if (phoneNumber === null || phoneNumber === undefined) return;

    const node = new CallNode(phoneNumber);
    const foundNode = this.searchNode(node);

    if (foundNode) {
      let prevNode, nextNode;
      prevNode = foundNode.prev;
      nextNode = foundNode.next;

      prevNode.next = nextNode;
      nextNode.prev = prevNode;

      this.insertAtHead(foundNode);
    } else {
      const newNode = new CallNode(phoneNumber);
      this.insertAtHead(newNode);
      this.size++;
      if (this.size > this.maxSize) {
        this.removeTail();
        this.size--;
      }
    }
  }

  insertAtHead(node) {
    if (this.size === 0) {
      this.tail = node;
    }

    let temp = this.head;
    node.next = temp;
    node.prev = null;
    this.head = node;
  }

  removeTail() {
    let temp = this.tail;
    let prevNode = temp.prev;
    prevNode.next = null;
    this.tail = prevNode;
  }

  searchNode(node) {
    let temp = this.head;
    while (temp !== null) {
      if (node.phoneNumber === temp.phoneNumber) {
        return temp;
      }
      temp = temp.next;
    }
    return null;
  }

  // Helper method to print all calls from head to tail
  printCallsForward() {
    let current = this.head;
    const calls = [];
    while (current) {
      calls.push(current.phoneNumber);
      current = current.next;
    }
    console.log("Forward:", calls.join(" -> "));
    console.log("Size:", this.size);
  }
}

// Test cases
function runTests() {
  const log = new CallLog();

  console.log("Test 1: Adding first 5 numbers");
  log.call("111");
  log.call("222");
  log.call("333");
  log.call("444");
  log.call("555");
  log.printCallsForward();
  // Expected: 555 -> 444 -> 333 -> 222 -> 111 (size: 5)

  console.log("\nTest 2: Adding 6th number");
  log.call("666");
  log.printCallsForward();
  // Expected: 666 -> 555 -> 444 -> 333 -> 222 (size: 5)
  // Note: 111 was removed

  console.log("\nTest 3: Moving existing number to front");
  log.call("333");
  log.printCallsForward();
  // Expected: 333 -> 666 -> 555 -> 444 -> 222 (size: 5)

  console.log("\nTest 4: Adding new number after moves");
  log.call("777");
  log.printCallsForward();
  // Expected: 777 -> 333 -> 666 -> 555 -> 444 (size: 5)

  console.log("\nTest 5: Moving tail to front");
  log.call("444");
  log.printCallsForward();
  // Expected: 444 -> 777 -> 333 -> 666 -> 555 (size: 5)
}

runTests();
