// Valid Palindrome: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, or false otherwise.

let s = "A man, a plan, a canal: Panama";

var isPalindrome = function (s) {
  let res = s.toLowerCase().replace(/[^a-z0-9]/g, ""); //removing non-alphanumeric characters
  let [left, right] = [0, res.length - 1];

  while (left <= right) {
    if (res.charAt(left) === res.charAt(right)) {
      left++;
      right--;
    } else {
      return false;
    }
  }
  return true;
};

console.log(isPalindrome(s));
