// LH Q30

const foo = () => console.log("First");
const bar = () => setTimeout(() => console.log("Second"));
const baz = () => console.log("Third");

bar();
foo();
baz();
// output: First Third Second

// Q33

const person = { name: "Lydia" };

function sayHi(age) {
  return `${this.name} is ${age}`;
}

console.log(sayHi.call(person, 21)); // Lydia is 21
console.log(sayHi.bind(person, 21)); // [Function: bound sayHi]
console.log(sayHi.apply(person, [21])); // Lydia is 21

/*
Lydia is 21 (call attached this to the object we passed and executes immediately.)
Function 
(copy of the function with bound context. 
Since bind returns that and is not executed immediately.)
*/
