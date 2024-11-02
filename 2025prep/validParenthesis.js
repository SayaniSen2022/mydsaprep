//leet20

let s = "()";

var isValid = function (s) {
  let stack = [];
  for (let i = 0; i < s.length; i++) {
    if (s.charAt(i) === "(" || s.charAt(i) === "{" || s.charAt(i) === "[") {
      stack.push(s.charAt(i));
    } else {
      if (
        stack.length > 0 &&
        stack[stack.length - 1] === getComplement(s.charAt(i))
      ) {
        stack.pop();
      } else return false;
    }
  }
  return stack.length < 1;
};

function getComplement(char) {
  switch (char) {
    case ")":
      return "(";
    case "}":
      return "{";
    case "]":
      return "[";
    default:
      return "x";
  }
}

const result = isValid(s);
console.log(result);
