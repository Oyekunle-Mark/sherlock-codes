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
  // will use a stack based solution to check bracket pair

  const stack = [];
  const mapBrackets = {
    ')': '(',
    ']': '[',
    '}': '{',
    '|': '|',
  };
}
