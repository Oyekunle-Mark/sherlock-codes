/**
 * *Checks if a number is an Armstrong number or not
 * *Returns true if it is and false otherwise
 * @param {number} n
 * @returns {boolean}
 */
function isArmstrongNumber(n) {
  const numbersArray = String(n).split('');
  const lengthOfNumbers = numbersArray.length;

  return numbersArray.reduce((a, b) => a + Math.pow(b, lengthOfNumbers), 0) ===
    n
    ? true
    : false;
}

console.log(isArmstrongNumber(6));
console.log(isArmstrongNumber(153));
console.log(isArmstrongNumber(351));
