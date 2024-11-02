// leet 49 : hashmap TC: O(mnlogn) ; SC: O(mn) Where m is the number of strings and n is the length of the longest string.

var groupAnagrams = function (strs) {
  const res = {};

  for (let s of strs) {
    const sortedS = s.split("").sort().join();
    if (!res[sortedS]) {
      res[sortedS] = [];
    }
    res[sortedS].push(s);
  }
  return Object.values(res);
};
