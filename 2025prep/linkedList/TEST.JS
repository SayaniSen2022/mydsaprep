class Stack {
  constructor() {
    this.arr = [];
  }

  push(element) {
    this.arr.push(element);
  }

  pop() {
    if (this.isEmpty()) return null;
    return this.arr.pop(); // [5,6,1] => using pop => [5, 6]
  }
  peek() {
    return this.arr[this.arr.length - 1];
  }

  isEmpty() {
    return this.arr.length === 0;
  }

  size() {
    return this.arr.length;
  }
}

const stack = new Stack();

stack.pop();

class QueueUsingStacks {
  constructor() {
    // TODO: Initialize your data structure here
    this.stack1 = new Stack();
    this.stack2 = new Stack();
  }

  enqueue(element) {
    // TODO: Add element to back of queue
    this.stack1.push(element);
  }

  dequeue() {
    // TODO: Remove and return element from front of queue
    //[1,2,3,4] => dequeue removes 1

    while (!this.stack1.isEmpty()) {
      this.stack2.push(this.stack1.pop());
    }

    const poppedVal = this.stack2.pop();

    while (!this.stack2.isEmpty()) {
      this.stack1.push(this.stack2.pop());
    }

    return poppedVal;

    //can you optimise so that its not O(2n)??
  }

  peek() {
    // TODO: Return element at front of queue without removing it
  }

  isEmpty() {
    // TODO: Return whether queue is empty
  }

  size() {
    // TODO: Return number of elements in queue
  }
}
