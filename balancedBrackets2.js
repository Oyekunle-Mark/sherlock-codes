/*
 * Complete the 'balancedBrackets' function below.
 *
 * The function is expected to return a BOOLEAN.
 * The function accepts STRING string as parameter.
 */

function isMatched(arr) {
  const mapBrackets = {
    '}': '{',
    ')': '(',
    ']': '[',
    '|': '|',
  };

  // set first to zero
  let first = 0;
  // set last to the length of arr minus one
  let last = arr.length - 1;
  // loop while first is less than last
  while (first < last) {
    // if first of arr does not have a closing tag at last of arr
    if (arr[first] !== mapBrackets[arr[last]]) {
      // return false
      return false;
    }
    // increment first
    first++;
    // decrement last
    last--;
  }
  // return true
  return true;
}

function balancedBrackets(string) {
  // should determine of the string contains matched bracket set or not
  // will have to loop through the whole string to check
  // will take O(n) time
  // The bracket set are "{}", "()", "[]" and "||"

  let brackets = [];

  // loop through the string
  for (let i = 0; i < string.length; i++) {
    // if current character in bracketSet
    if ('()[]{}|'.includes(string[i])) {
      brackets.push(string[i]);
    }
  }

  return isMatched(brackets);
}

console.log(balancedBrackets('(([]))'));
console.log(balancedBrackets('({[]})'));
console.log(balancedBrackets('this(si{[]onw })'));
console.log(balancedBrackets('{{||[]||}}'));
console.log(balancedBrackets('[|]|'));