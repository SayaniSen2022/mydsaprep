//Top K Frequent Elements: Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

let nums = [1, 1, 1, 2, 2, 3]; //output: [1,2]
let k = 2;

var topKFrequent = function (nums, k) {
  const map = new Map();
  const arr = new Array(nums.length + 1).fill(0);
  const ans = [];

  nums.forEach((el) => {
    const val = map.get(el) || 0;
    map.set(el, val + 1);
  });

  for (let [key, value] of map) {
    const prev = arr[value] || [];
    prev.push(key);
    arr[value] = prev;
  }

  arr.reverse();
  for (let el of arr) {
    if (k < 1) break;
    if (el) {
      for (let el2 of el) {
        ans.push(el2);
        k--;
      }
    }
  }

  return ans;
};

console.log(topKFrequent(nums, k));
