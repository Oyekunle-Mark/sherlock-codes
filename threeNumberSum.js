/*
 * Complete the 'threeNumberSum' function below.
 *
 * The function is expected to return a 2D_INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY arr
 *  2. INTEGER target
 */

function threeNumberSum(arr, target) {
  // will hold the possible combinations
  const sums = [];

  // sort the input array
  arr = arr.sort((a, b) => a - b);

  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      for (let k = j + 1; k < arr.length; k++) {
        // if the three numbers add up to target
        if (arr[i] + arr[j] + arr[k] === target) {
          // add it to the sum array
          sums.push([arr[i], arr[j], arr[k]]);
        }
      }
    }
  }

  // return sums
  return sums;
}

console.log(threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 30));
console.log(threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 33));
