/**
 * *Creates the collatz sequence for a number
 * @param {number} n
 * @returns {number[]}
 */
function collatzSequence(n) {
  const source = n;
  const result = [];
  result.push(n);

  const sequence = num => {
    if (num === 2) {
      result.push(1);
      return;
    }

    if (num % 2 === 1) {
      const value = num * 3 + 1;
      result.push(value);
      sequence(value);
    } else {
      const value = num / 2;
      result.push(value);
      sequence(value);
    }
  };

  sequence(source);
  return result;
}

console.log(collatzSequence(23));
