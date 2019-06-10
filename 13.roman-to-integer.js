/*
 * @lc app=leetcode id=13 lang=javascript
 *
 * [13] Roman to Integer
 */
/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
  const convertionTable = {
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

  let number = 0;

  for (let i = 0; i < s.length; i++) {
    if (convertionTable[s[i] + s[i+1]]) {
      number += convertionTable[s[i] + s[i+1]];
      i++;
      continue;
    }

    number += convertionTable[s[i]];
  }

  return number;
};

console.log(romanToInt("LVIII"));
console.log(romanToInt("MCMXCIV"));

