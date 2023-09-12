// Group Anagram : Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

let strs = ["eat", "tea", "tan", "ate", "nat", "bat"];

var groupAnagrams = function (strs, map = new Map()) {
  if (!strs.length) return []; //if length=0 returns []

  groupWords(strs, map); //calling grouWords function, takes the inout array and map as argument

  return [...map.values()]; //returning final array with group anagrams
};

var groupWords = (strs, map) => {
  for (const eachWord of strs) {
    const hash = getHash(eachWord);
    const values = map.get(hash) || [];

    values.push(eachWord);
    map.set(hash, values);
  }
};

//getHash calculates the frequency of each character in a string, and forms the key for the map

const getHash = (str) => {
  const frequency = new Array(26).fill(0);

  for (const char of str) {
    const charCode = getCode(char);
    frequency[charCode]++;
  }
  return buildHash(frequency);
};

const getCode = (char) => char.charCodeAt(0) - "a".charCodeAt(0);
const buildHash = (frequency) => frequency.toString();

console.log(groupAnagrams(strs));
