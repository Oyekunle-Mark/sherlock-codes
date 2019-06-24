/**
 * Determines if the parenthesis in a string is balanced or not.
 * Returns true if balanced and false if otherwise
 * @param {string} str
 * @returns {boolean}
 */
function balancedBrackets(str) {
  let matched = true;
  const brackets = [];
  const mapBrackets = {
    '{': '}',
    '}': '{',
    '(': ')',
    ')': '(',
    '[': ']',
    ']': '[',
  };

  for (const i of str) {
    if ('([{'.includes(i)) brackets.push(i);
    else if (')]}'.includes(i))
      if (brackets.pop() === mapBrackets[i]) continue;
      else matched = false;
  }

  if (brackets.length !== 0) return false;

  return matched;
}

console.log(balancedBrackets('('));
console.log(balancedBrackets('[](){}'));
console.log(balancedBrackets('[({})]'));
console.log(balancedBrackets('[(]{)}'));
