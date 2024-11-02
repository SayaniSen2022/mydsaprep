//leet 01

const nums = [2, 7, 5, 8];
const target = 13;

let twoSum = (nums, target) => {
  let numsMap = new Map();

  for (let i = 0; i < nums.length; i++) {
    let diff = target - nums[i];

    if (numsMap.has(diff) && numsMap.get(diff) !== i) {
      return [i, numsMap.get(diff)];
    } else {
      numsMap.set(nums[i], i);
    }
  }
};

const res = twoSum(nums, target);
console.log(res);
