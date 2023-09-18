// Longest Consecutive Sequence: Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.

let nums = [100, 4, 200, 1, 3, 2]; //Output: 4 for [1,2,3,4]

var longestConsecutive = function (nums) {
  let numsSet = new Set(nums);
  let maxScore = 0;

  for (const num of [...numsSet]) {
    const prevNum = num - 1;
    if (numsSet.has(prevNum)) continue;

    let [currNum, score] = [num, 1];
    const isStreak = () => numsSet.has(currNum + 1);

    while (isStreak()) {
      currNum++;
      score++;
    }
    maxScore = Math.max(maxScore, score);
  }
  return maxScore;
};

console.log(longestConsecutive(nums));
