/**
 * *Takes a numeral and returns a string representation of the number in Roman numerals
 * @param {number} number
 * @returns {string}
 */

function romanNumeralize(number) {
  const romanToNumeralTable = {
    M: 1000,
    CM: 900,
    D: 500,
    CD: 400,
    C: 100,
    XC: 90,
    L: 50,
    XL: 40,
    X: 10,
    IX: 9,
    V: 5,
    IV: 4,
    I: 1
  };

  let arabicNumeral = "";

  for (const i in romanToNumeralTable) {
    if (number >= romanToNumeralTable[i]) {
      while (number >= romanToNumeralTable[i]) {
        arabicNumeral += i;
        number -= romanToNumeralTable[i];
      }
    }
  }

  return arabicNumeral;
}

console.log("romanNumeralize(1973): ", romanNumeralize(1973));
