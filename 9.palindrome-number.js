/*
 * @lc app=leetcode id=9 lang=javascript
 *
 * [9] Palindrome Number
 */
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
  const numberString = String(x);
  const iterationRange = Math.floor(numberString.length / 2);

  for (let i = 0; i <= iterationRange; i++)
    if (numberString[i] !== numberString[numberString.length - 1 - i])
      return false;

  return true;
};
