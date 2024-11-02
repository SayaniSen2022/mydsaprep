//leet16 => Two Sum II - Input Array Is Sorted

const numbers = [2, 7, 11, 15];
const target = 9;

var twoSum = function (numbers, target) {
  let numsMap = new Map();

  for (let i = 0; i < numbers.length; i++) {
    let diff = target - numbers[i];

    if (numsMap.has(diff) && numsMap.get(diff) !== i) {
      return [numsMap.get(diff) + 1, i + 1];
    } else {
      numsMap.set(numbers[i], i);
    }
  }
};
