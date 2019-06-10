/*
 * @lc app=leetcode id=20 lang=javascript
 *
 * [20] Valid Parentheses
 */
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  const bracketArray = [];
  let equal = true;
  const bracketPair = {
    ")": "(",
    "]": "[",
    "}": "{"
  };

  for (let i of s) {
    if ("([{".includes(i)) {
      bracketArray.push(i);
    } else {
      if (bracketArray.pop() !== bracketPair[i]) equal = false;
    }
  }

  if (bracketArray.length !== 0) return false;

  return equal;
};
