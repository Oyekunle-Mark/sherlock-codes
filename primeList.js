/**
 * *returns the list of prime numbers between a range of numbers inclusive.
 * @param {number} start
 * @param {number} end
 * @returns {number[]}
 */
function primeList(start, end) {
  const primes = [];

  for (let i = start; i <= end; i++) {
    if (isPrime(i)) primes.push(i);
    debugger;
  }

  return primes;
}

/**
 * Returns true or false if a number is false or not
 * todo try reducing traversing the whole length of number
 * @param {number} n
 * @returns {boolean}
 */
const isPrime = n => {
  let i = 2;

  while (i < n) {
    if (n % i === 0) return false;
    i++;
  }

  return true;
};

console.log(primeList(2, 100));
