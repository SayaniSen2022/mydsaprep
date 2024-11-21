class CallNode {
  constructor(phoneNumber) {
    this.phoneNumber = phoneNumber;
  }
}

class CallLog {
  constructor() {
    this.head = null;
  }

  call(phoneNumber) {
    // TODO: Implement this method
    const node = new CallNode(phoneNumber);
    let curr = this.head;
    node.next = curr;
    this.head = node;
  }

  printCalls() {
    let current = this.head;
    while (current) {
      console.log(current.phoneNumber);
      current = current.next;
    }
  }
}

// Test cases
function runTests() {
  const log = new CallLog();

  console.log("Test Case 1: Adding first call");
  log.call("rishi");
  log.printCalls();
  // Expected: rishi

  console.log("\nTest Case 2: Adding second call");
  log.call("mom");
  log.printCalls();
  // Expected:
  // mom
  // rishi

  console.log("\nTest Case 3: Adding third call");
  log.call("dad");
  log.printCalls();
  // dad
  // mom
  // rishi
}

runTests();
