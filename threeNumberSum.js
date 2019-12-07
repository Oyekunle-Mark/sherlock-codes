/*
 * Complete the 'threeNumberSum' function below.
 *
 * The function is expected to return a 2D_INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY arr
 *  2. INTEGER target
 */

function threeNumberSum(arr, target) {
  const sums = [];

  arr = arr.sort((a, b) => a - b)

  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      for (let k = j + 1; k < arr.length; k++) {
        if (arr[i] + arr[j] + arr[k] === target) {
          sums.push([arr[i], arr[j], arr[k]]);
        }
      }
    }
  }

  return sums;
}

console.log(threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 30));
console.log(threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 33));
