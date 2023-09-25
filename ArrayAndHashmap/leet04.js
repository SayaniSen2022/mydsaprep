// Median Of Two Sorted Arrays

// This solution has time complexity O((m+n)log(m+n)) where m and n are sizes of nums1 and num2 array

let nums1 = [1, 3];
let nums2 = [2];

var findMedianSortedArrays = function (nums1, nums2) {
  let res = nums1.concat(nums2);
  let resSorted = res.sort((a, b) => a - b);
  if (resSorted.length % 2 === 0) {
    let median =
      (resSorted[Math.floor((resSorted.length - 1) / 2)] +
        resSorted[Math.floor((resSorted.length - 1) / 2) + 1]) /
      2;
    return median;
  } else {
    let median = resSorted[(resSorted.length - 1) / 2];
    return median;
  }
};

console.log(findMedianSortedArrays(nums1, nums2));
