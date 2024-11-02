/**
leet 15: 3 sum
 */
var threeSum = function (nums) {
  const res = [];
  nums.sort((a, b) => a - b); //sorting the array to avoid duplicacies

  for (let i = 0; i < nums.length; i++) {
    let a = nums[i]; //starting point
    if (a > 0) break; //if start is > 0, no point since no sum will be = 0 in that sorted array
    if (i > 0 && a === nums[i - 1]) continue;

    let [l, r] = [i + 1, nums.length - 1]; //setting the pointers
    while (l < r) {
      const threeSum = a + nums[l] + nums[r];
      if (threeSum > 0) {
        r--;
      } else if (threeSum < 0) {
        l++;
      } else {
        res.push([a, nums[l], nums[r]]);
        l++;
        r--;
        //increasing left pointer when left pointers are consecutively same and continue to be less than right pointer
        while (nums[l] === nums[l - 1] && l < r) {
          l++;
        }
      }
    }
  }
  return res;
};
