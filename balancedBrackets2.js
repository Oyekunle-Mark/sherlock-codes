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

function randomPair(string) {
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
    if ('([{|'.includes(string[i])) {
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

  return isMatched(brackets) || randomPair(brackets);
}

console.log(
  balancedBrackets(
    'I (wa)n{t to buy a on}esie[…] b(u{[t] kno}w it) won’t suit me.',
  ),
);
console.log(balancedBrackets('({[]})'));
console.log(balancedBrackets('this(si{[]onw })'));
console.log(balancedBrackets('{{||[]||}}'));
console.log(balancedBrackets('[|]|'));
