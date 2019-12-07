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

  // loop through the string
  for (let i = 0; i < string.length; i++) {
    // if current character in "([{"
    if ('([{'.includes(string[i])) {
      // push it to the stack
      stack.push(string[i]);
    }
    // otherwise, if character in ")]}"
    else if (')]}'.includes(string[i])) {
      // pop an item from the stack
      const item = stack.pop();
      // if item popped is equal to mapBrackets of character
      if (item === mapBrackets[string[i]]) {
        // continue
        continue;
      }
      // otherwise,
      else {
        // return false
        return false;
      }
    }
  }
  // if stack is not empty
  if (stack.length !== 0) {
    // return false
    return false;
  }
  // return true
  return true;
}
