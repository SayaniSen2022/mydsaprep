// Immediately Invoked Function Expression

function sayHi() {
  return (() => 0)(); // IIFE
}

console.log(sayHi()); // 0

console.log(typeof sayHi()); // number

// the iife here returns 0 which is a number, hence sayhi returns 0->number
// NOTE: typeof null returns "object".
// typeof can return the following list of values:
// undefined, boolean, number, bigint, string, symbol, function and object
(() => {
  let x, y;
  try {
    throw new Error();
  } catch (x) {
    ((x = 1), (y = 2));
    console.log(x); // 1
  }
  console.log(x); // undefined
  console.log(y); // 2
})();

// output: 1 undefined 2
/* the x that catch block receives is not same as the variable x. This x is block-scoped. We then set
this block scoped x to 1, and y = 2. Outside the catch block, x is still undefined, y is 2 */

[
  [0, 1],
  [2, 3],
].reduce(
  (acc, curr) => {
    return acc.concat(curr);
  },
  [1, 2],
);
/* Here [1, 2] is our initial value of acc. First round, curr = [0, 1]. We concat acc with curr to get
[1, 2, 0, 1]. Second round, acc = [1, 2, 0, 1], curr = [2, 3]. Answer: [1, 2, 0, 1, 2, 3] */

!!null; // null is falsy, not falsy = true. not true is false
!!""; // '' is falsy. not falsy is true, not true is false
!!1; // 1 is truthy. not truthy is false. not false is true
// output: false false true

setInterval(() => console.log("Hi"), 1000);
/* What does the setInterval method return in the browser? a unique id, which can be
used to clear the interval with the clearInterval() function. */

[..."Lydia"]; // string is an iterable
// spread operator, maps every character of an iterable to one element ["L", "y", "d", "i", "a"]
