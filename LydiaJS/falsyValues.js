/*
There are 8 falsy values in JS: 
undefined, null, NaN, false, ''(empty string), 0, -0, 0n(BigInt(0))

Function constructors, like new Number and new Boolean are truthy.
*/

0; // falsy
new Number(0); // truthy
(""); //falsy
(" "); // truthy
new Boolean(false); // truthy
undefined; // falsy

console.log(typeof typeof 1); // string
// typeof 1 is "number", typeof "number" is "string"

const numbers = [1, 2, 3];
numbers[10] = 11;
console.log(numbers); // [1, 2, 3, undefined,...undefined, 11]; there will be 7 undefined.
// [ 1, 2, 3, <7 empty items>, 11 ]
