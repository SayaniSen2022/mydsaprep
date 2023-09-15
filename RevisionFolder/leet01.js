// Two Sum

let nums = [2, 7, 11, 15];
let target = 9;

const towSum = (nums, target) => {
  let numsMap = new Map();
  for (let i = 0; i < nums.length; i++) {
    let diff = target - nums[i];
    if (numsMap.has(diff)) {
      return [i, numsMap.get(diff)];
    } else {
      numsMap.set(nums[i], i);
    }
  }
};

console.log(towSum(nums, target));
