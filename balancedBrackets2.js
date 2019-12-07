/*
 * Complete the 'balancedBrackets' function below.
 *
 * The function is expected to return a BOOLEAN.
 * The function accepts STRING string as parameter.
 */

function balancedBrackets(string) {
  // should determine of the string contains matched bracket set or not
  // will have to loop through the whole string to check
  // will take O(n) time
  // The bracket set are "{}", "()", "[]" and "||"

  const brackets = [];
  const bracketSet = {
    ')': 1,
    ']': 1,
    '}': 1,
    '|': 1,
    '(': 1,
    '[': 1,
    '{': 1,
  };

  // loop through the string
  for (let i = 0; i < string.length; i++) {
    // if current character in bracketSet
        // add it to brackets
  }

  return isMatched(brackets)
}

console.log(balancedBrackets('(([]))'));
console.log(balancedBrackets('({[]})'));
console.log(balancedBrackets('this(si{[]onw })'));
console.log(balancedBrackets('{{||[]||}}'));
console.log(balancedBrackets('[|]|'));
