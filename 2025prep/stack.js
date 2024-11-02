class Stack {
  constructor() {
    this.items = [];
  }

  push(item) {
    this.items.push(item);
  }

  pop() {
    return this.items.pop();
  }
  peek() {
    if (this.items.length === 0) return null;
    return this.items[this.items.length - 1];
  }
  getSize() {
    return this.items.length;
  }
}

const cars = new Stack();

cars.push("Toyota");
cars.push("Volkswagen");
cars.push("Suzuki");
cars.pop();
console.log(cars.peek());
console.log(cars);
console.log(cars.getSize());
