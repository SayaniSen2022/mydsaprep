// leet 49 : hashmap TC: O(mnlogn) ; SC: O(mn) Where m is the number of strings and n is the length of the longest string.

const strs = ["act", "pots", "tops", "cat", "stop", "hat"];

let groupAnagrams = (strs) => {
  const res = {};
  for (let s of strs) {
    const count = new Array(26).fill(0);
    for (let c of s) {
      count[c.charCodeAt(0) - `a`.charCodeAt(0)] += 1;
    }
    const key = count.join(",");

    if (!res[key]) {
      res[key] = [];
    }
    res[key].push(s);
  }
  return Object.values(res);
};

const result = groupAnagrams(strs);
console.log(result);
