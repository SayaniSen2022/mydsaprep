//Product of Array Except Self: Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.

let nums = [1, 2, 3, 4]; //Output: [24,12,8,6]

var productExceptSelf = function (nums) {
  let res = [];
  let [prefix, postfix] = [1, 1];
  for (let i = 0; i < nums.length; i++) {
    res[i] = prefix;
    prefix *= nums[i];
  }
  for (let j = nums.length - 2; j >= 0; j--) {
    postfix *= nums[j + 1];
    res[j] *= postfix;
  }
  return res;
};
console.log(productExceptSelf(nums));
