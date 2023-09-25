const arr = [-1, -2, 3, 4];

function test(arr) {
  arr.sort((a, b) => a - b);

  return typeof arr;
}
console.log(test(arr));
