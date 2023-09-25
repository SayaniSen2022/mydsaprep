/*
 Is Subsequence : Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
*/

let s = "abc";
let t = "ahbgdc";

let isSubsequence = (s, t) => {
  let tMap = new Map();

  for (let i = 0; i < t.length; t++) {
    if (tMap.has(t.charAt(i))) {
      tMap.set(t.charAt(i), tMap.get(t.charAt(i)) + 1);
    } else {
      tMap.set(t.charAt(i), 1);
    }
  }

  for (let j = 0; j < s.length; j++) {
    if (!tMap.has(s.charAt(j))) {
      return false;
    } else {
      if (s.indexOf(s.charAt(j)) <= t.indexOf(s.charAt(j))) continue;
    }
  }
  return true;
};

console.log(isSubsequence(s, t));
