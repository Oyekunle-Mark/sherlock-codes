/**
 * *Returns the sum of the individual digits in a number
 * ?perhaps a more efficient solution
 * TODO find a more efficient solution
 * @param {number} num
 * @returns {number}
 */

function sumOfDigits(num) {
  let sum = 0;
  
  for (const i of [...String(num)]) {
    sum += Number(i);
  }
  
  return sum;
}

console.log(sumOfDigits(23));  // <--- 5
console.log(sumOfDigits(496)); // <--- 19
