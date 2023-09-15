// Valid Anagram for any random string

let s = "Ana%^&gra  m";
let t = "nAgara#()m";

const isAnagram = (s, t) => {
  let strS = s.replace(/[^a-z]/gi, "").toLowerCase();
  let strT = t.replace(/[^a-z]/gi, "").toLowerCase();

  if (strS.length !== strT.length) return false;

  let sMap = new Map();
  let tMap = new Map();

  for (let i = 0; i < strS.length; i++) {
    if (sMap.has(strS.charAt(i))) {
      sMap.set(strS.charAt(i), sMap.get(strS.charAt(i)) + 1);
    } else {
      sMap.set(strS.charAt(i), 1);
    }
  }
  for (let j = 0; j < strT.length; j++) {
    if (tMap.has(strT.charAt(j))) {
      tMap.set(strT.charAt(j), tMap.get(strT.charAt(j)) + 1);
    } else {
      tMap.set(strT.charAt(j), 1);
    }
  }

  return compareMaps(sMap, tMap);
};
const compareMaps = (map1, map2) => {
  let testVal;
  if (map1.size !== map2.size) return false; //compare the size of maps: step 1

  for (const [key, val] of map1) {
    testVal = map2.get(key);

    // check if the key actually exists in map2 and does not return a false positive in case of undefined value
    if (testVal !== val || (testVal === undefined && !map2.has(key))) {
      return false;
    }
  }
  return true;
};

console.log(isAnagram(s, t));
