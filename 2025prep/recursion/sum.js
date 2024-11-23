// sum(5) = 5+4+3+2+1+0 : base case: sum(1) = 1; sum(2) = 2 + sum(1); sum(3) = 3 + sum(2)
//printlist of linked list

function summation(n) {
  if (n === 1) return 1;
  else return n + summation(n - 1);
}

const result = summation(20);
console.log(result);
