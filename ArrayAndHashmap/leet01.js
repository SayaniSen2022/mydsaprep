// Two Sum: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order.

let nums = [3, 2, 4];
let target = 6;

var twoSum = function (nums, target) {
  let numsMap = new Map();
  for (let j = 0; j < nums.length; j++) {
    let diff = target - nums[j];
    if (numsMap.has(diff) && numsMap.get(diff) !== j) {
      return [j, numsMap.get(diff)];
    } else {
      numsMap.set(nums[j], j);
    }
  }
};

console.log(twoSum(nums, target));

/*
Brute force:

 let [left, right] = [0, nums.length - 1]; // 0,3

  while (left < nums.length) {
    let diff = target - nums[left];
    while (right > left) {
      if (nums[right] === diff) {
        return [left, right];
      } else {
        right--;
      }
    }
    left++;
    right = nums.length - 1;
  }
*/
