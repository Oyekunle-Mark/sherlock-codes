/**
 * Finds the number of matching pairs from an array
 * @param {number} n
 * @param {number[]} ar
 * @returns
 */
function sockMerchant(n, ar) {
  /*
   * This problem can be solved in linear time
   * The first pass should count the occurrence of each number
   * The second pass should check the number of pairs extractable from
   * number of each pari
   * Return the overall pair count.
   */

  // set sock count to an empty object
  const countOfEachSock = {};
  // set pair count zero
  let pairCount = 0;

  // loop and count each sock using countOfEachSock
  for (let i = 0; i < n; i++) {
    if (!countOfEachSock[ar[i]]) {
      countOfEachSock[ar[i]] = 0;
    }

    countOfEachSock[ar[i]] += 1;
  }

  // check the counts to see number of pairs obtainable
  for (const key in countOfEachSock) {
    const num = countOfEachSock[key];

    if (num >= 2) {
      pairCount += Math.floor(num / 2);
    }
  }

  return pairCount;
}

console.log(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]));
console.log(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]));
