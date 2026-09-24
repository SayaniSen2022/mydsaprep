// A generator is a special function that can pause its execution and resume later.
function* generator(i) {
  yield i; // pauses here i=10
  yield i * 2; // second pause
}

const gen = generator(10); // gives an object gen

console.log(gen.next().value); // starts executing the function
// next does not return just 10, it returns an object {  value: 10,  done: false}
console.log(gen.next().value); // execution resumes, {value: 20, done: false}
console.log(gen.next()); // {value: undefined, done: true} since no other yield is there

/* the * after the function indicates its a generator function. A generator function can pause whenever
it encounter yield. Yield: Return this value for now, but don't finish the function. */
