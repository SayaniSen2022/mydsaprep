// closure

function init(){
  let name = "Sam";
  function displayName(){
    console.log(name)
  }
  return displayName;
}

const myRes = init()
myRes()