/**
 * Determines if there is a 2x2 matrix of vowel in an array of string
 * Returns the row-column index of the top left vowel if there is
 * and the string "not found" if not.
 * @param {*} strArr input string of array
 * @returns {string}
 */
const vowelSquare = strArr => {
  const vowels = 'aeiou';

  for (let i = 0; i < strArr.length - 1; i++) {
    for (let j = 0; j < strArr[i].length - 1; j++) {
      if (vowels.includes(strArr[i][j])) {
        if (
          vowels.includes(strArr[i][j + 1]) &&
          vowels.includes(strArr[i + 1][j + 1]) &&
          vowels.includes(strArr[i + 1][j])
        ) {
          return `${i}-${j}`;
        }
      }
    }
  }

  return 'not found';
};

console.log(vowelSquare(['aba', 'eee']));
console.log(vowelSquare(['aeeekmoo', 'kmnouvoo', 'frrsfsto']));
console.log(vowelSquare(["aa", "aa"]));
