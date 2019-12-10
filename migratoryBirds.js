/**
 * Hacker rank migratory bird challenge.
 * @param {number[]} arr input array
 * @returns {number}
 */
function migratoryBirds(arr) {
  const findMostFrequencyForNumberOneToFive = ar => {
    const mostFrequent = [];

    const range = new Map([
      [1, 0],
      [2, 0],
      [3, 0],
      [4, 0],
      [5, 0],
    ]);

    ar.map(num => range.set(num, range.get(num) + 1));

    const maximum = Math.max(...range.values());

    range.forEach((val, key) => {
      if (val === maximum) mostFrequent.push(key);
    });

    return mostFrequent;
  };

  return Math.min(...findMostFrequencyForNumberOneToFive(arr));
}

console.log(
  'TCL: migratoryBirds([1, 4, 4, 4, 5, 3])',
  migratoryBirds([1, 4, 4, 4, 5, 3]),
);
console.log(
  'TCL: migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4])',
  migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]),
);
