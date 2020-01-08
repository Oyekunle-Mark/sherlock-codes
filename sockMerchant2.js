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
  
    const numOfEachSock = {};
  let pairs = 0;

  for (let i = 0; i < n; i++) {
    if (!numOfEachSock[`${ar[i]}`]) numOfEachSock[`${ar[i]}`] = 0;

    numOfEachSock[`${ar[i]}`] += 1;
  }

  for (const key in numOfEachSock) {
    const num = numOfEachSock[key];

    if (num >= 2) pairs += Math.floor(num / 2);
  }

  return pairs;
}
