/*
 * @lc app=leetcode id=7 lang=javascript
 *
 * [7] Reverse Integer
 */
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
  const numberArray = [...String(x)];
  const reversedArray = [];

  if (numberArray[0] === "-") {
    numberArray.shift();
    reversedArray.push("-");
  }

  for (let i = numberArray.length - 1; i >= 0; i--) {
    reversedArray.push(numberArray[i]);
  }

  const reversedNumber = parseInt(reversedArray.join(""));

  if (reversedNumber <= Math.pow(-2, 31) || reversedNumber >= Math.pow(2, 31))
    return 0;

  return reversedNumber;
};
