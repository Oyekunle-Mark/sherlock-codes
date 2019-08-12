/**
 * Hacker rank birthday cake challenge
 * @param {number[]} ar
 * @returns {number}
 */
function birthdayCakeCandles(ar) {
  const max = Math.max(...ar);
  let count = 0;

  [...ar].map(num => {
    if (num === max) count++;
  });

  return count;
}

console.log(
  'TCL: birthdayCakeCandles([3, 2, 1, 3])',
  birthdayCakeCandles([3, 2, 1, 3]),
);
console.log(
  'TCL: birthdayCakeCandles([82, 49, 82, 82, 41, 82, 15, 63, 38, 25])',
  birthdayCakeCandles([82, 49, 82, 82, 41, 82, 15, 63, 38, 25]),
);
