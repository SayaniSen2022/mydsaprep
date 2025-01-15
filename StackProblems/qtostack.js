// Implement a queue using two stacks
/** a queue follows FIFO and stack follows LIFO */

//first implementation of stack

class Stack {
  constructor() {
    this.stack = [];
  }

  insertElement(val) {
    this.stack.push(val);
  }
  deleteElement() {
    if (this.stack.length === 0) return;

    let poppedElement = this.stack.pop();
    return poppedElement;
  }
  peek() {
    return this.stack[this.stack.length - 1];
  }
  isEmpty() {
    return this.stack.length === 0;
  }
  size() {
    return this.stack.length;
  }
}
