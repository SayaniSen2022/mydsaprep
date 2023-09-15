//Contains Duplicate

let nums = [1, 2, 3, 1];

const containsDuplicate = () => {
  if (!nums.length) return false;

  let numsSet = new Set(nums);

  return nums.length === numsSet.size ? false : true;
};

console.log(containsDuplicate(nums));
