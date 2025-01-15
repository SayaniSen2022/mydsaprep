/**
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 */

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
function containsNearbyDuplicate(nums, k) {
  // Your solution here
  let numsMap = new Map();

  for (let i = 0; i < nums.length; i++) {
    if (numsMap.has(nums[i])) {
      let index = numsMap.get(nums[i]);
      if (i !== index) {
        let diff = Math.abs(i - index);
        if (diff <= k) {
          return true;
        } else {
          numsMap.set(nums[i], i);
        }
      }
    } else {
      numsMap.set(nums[i], i); //1,0 0,1  1,2 1,3
    }
  }
  return false;
}

// Test cases
function runTests() {
  const testCases = [
    {
      nums: [1, 2, 3, 1],
      k: 3,
      expected: true,
      description: "Example 1: Basic case with duplicate at distance 3",
    },
    {
      nums: [1, 0, 1, 1],
      k: 1,
      expected: true,
      description: "Example 2: Adjacent duplicates",
    },
    {
      nums: [1, 2, 3, 1, 2, 3],
      k: 2,
      expected: false,
      description: "Example 3: Duplicates beyond k distance",
    },
    {
      nums: [1, 2, 3, 4, 5],
      k: 3,
      expected: false,
      description: "No duplicates in array",
    },
    {
      nums: [1, 1, 1, 1],
      k: 1,
      expected: true,
      description: "Multiple adjacent duplicates",
    },
    {
      nums: [],
      k: 5,
      expected: false,
      description: "Empty array",
    },
    {
      nums: [-1, -2, -3, -1],
      k: 3,
      expected: true,
      description: "Array with negative numbers",
    },
  ];

  let passed = 0;
  let failed = 0;

  testCases.forEach((test, index) => {
    const result = containsNearbyDuplicate(test.nums, test.k);
    const success = result === test.expected;

    console.log(`Test ${index + 1}: ${test.description}`);
    console.log(`Input: nums = [${test.nums}], k = ${test.k}`);
    console.log(`Expected: ${test.expected}`);
    console.log(`Got: ${result}`);
    console.log(`${success ? "PASSED" : "FAILED"}\n`);

    if (success) passed++;
    else failed++;
  });

  console.log(`\nTest Summary:`);
  console.log(`Passed: ${passed}`);
  console.log(`Failed: ${failed}`);
  console.log(`Total: ${testCases.length}`);
}

// Run the tests
runTests();
