/**
 * Hacker rank staircase challenge
 * @param {number} n the number of steps
 */
function staircase(n) {
  let i = 1;

  while (i <= n) {
    const arr = Array(n - i)
      .fill(' ')
      .concat(Array(i).fill('#'))
      .join('');
    console.log(arr);

    i++;
  }
}

staircase(6);
