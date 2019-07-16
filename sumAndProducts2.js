/**
 * *Returns the numbers that adds up to the first argument and equals the second argument when multiplied
 * *The result is always an array sorted by number
 * @param {number} sum
 * @param {number} product
 * @returns {number[]}
 */
function sumAndProduct(sum, product) {
  let start = 0, end = sum;
  let validCombo = false;
  
  for(start; start <= end; start++) {
    if ((start + end === sum) && (start * end === product)) {
      validCombo = true;
      break;
    }
    
    end--;
  }
  
  return validCombo ? [start, end].sort((a, b) => a > b) : null;
}

console.log(sumAndProduct(6, 9));
console.log(sumAndProduct(20, 0));
console.log(sumAndProduct(36, 180));