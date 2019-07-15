/**
 * Returns the numbers that adds up to the first argument and equals the second argument when multiplied
 * The result is always an array sorted by number
 * @param {number} sum
 * @param {number} product
 * @returns {number[]}
 */
function sumAndProduct(sum, product) {
  for (let i = 0; i <= sum / 2; i++)
    if (i + (sum - i) === sum && i * (sum - i) === product) return [i, sum - i];

  return null;
}

console.log(sumAndProduct(6, 9));
console.log(sumAndProduct(20, 0));
console.log(sumAndProduct(36, 180));
