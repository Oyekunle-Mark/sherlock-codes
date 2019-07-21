/**
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
