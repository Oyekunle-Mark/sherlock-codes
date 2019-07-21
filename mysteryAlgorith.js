/**
 * Takes two numbers,
 * Assigns the first to the value of the first - second if first > second
 * Assigns second to the value of the second - first if second > first.
 * Returns first or second when first === second.
 * @param {number} x
 * @param {number} y
 * @returns {number}
 */
function mystery(x, y) {
  while (x !== y) {
    if (x > y) x = x - y;
    if (x < y) y = y - x;
  }

  return x;
}

console.log(mystery(2437, 875));
