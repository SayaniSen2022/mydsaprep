//leet125 : palindrome

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  s = s.toLowerCase().replace(/[^a-z0-9]/g, "");

  let [left, right] = [0, s.length - 1];

  while (left <= right) {
    if (s.charAt(left) === s.charAt(right)) {
      left++;
      right--;
    } else {
      return false;
    }
  }
  return true;
};
