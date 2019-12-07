/*
 * Complete the 'fibonacci' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER n as parameter.
 */

function fibonacci(n) {
  // finds the fibonacci sequence to up nth number
  // Number ranges between 1 <= n <= 10

  // initialize sequence to an empty array
  let sequence = [];
  // initialize count to zero
  let count = 0;

  // if n is 1
  if (n === 1) {
    // assign sequence to an array with a zero
    sequence = [0];
    // set count to one
    count = 1;
  }
  // otherwise, if n is greater than or equal 2
  else if (n >= 2) {
    // assign sequence to an array with zero and one
    sequence = [0, 1];
    // set count to two
    count = 2;
  }

  // loop while count of sequence is less than n
  while (count < n) {
    // append the sum of index count - 1 and count - 2 of sequence to sequence
    sequence.push(sequence[count - 1] + sequence[count - 2]);
    // increment count
    count++;
  }

  // return sequence
  return sequence;
}

console.log(fibonacci(4));
console.log(fibonacci(10));
