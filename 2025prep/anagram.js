//leet242

//solution 1: less optimal

var isAnagram = function (s, t) {
  if (s.length !== t.length) return false;

  s = s.toLowerCase().replace(/[^a-z,""]/g, "");
  t = t.toLowerCase().replace(/[^a-z,""]/g, "");

  let sArr = s.split("").sort().join();
  let tArr = t.split("").sort().join();

  if (sArr === tArr) return true;
  return false;
};

//solution 2

let isAnagram = (s, t) => {
  if (s.length !== t.length) return false;

  let sMap = new Map();
  let tMap = new Map();

  for (let i = 0; i < s.length; i++) {
    if (!sMap.has(s.charAt(i))) {
      sMap.set(s.charAt(i), 1);
    } else {
      sMap.set(s.charAt(i), sMap.get(s.charAt(i)) + 1);
    }
  }
  for (let j = 0; j < t.length; j++) {
    if (!tMap.has(t.charAt(j))) {
      tMap.set(t.charAt(j), 1);
    } else {
      tMap.set(t.charAt(j), tMap.get(t.charAt(j)) + 1);
    }
  }

  return compareMaps(sMap, tMap);
};

function compareMaps(tMap, sMap) {
  let testVal;
  if (sMap.size !== tMap.size) return false;

  for (let [key, val] of sMap) {
    testVal = tMap.get(key);

    if (testVal !== val || (testVal === undefined && !tMap.has(key))) {
      return false;
    }
  }
  return true;
}
