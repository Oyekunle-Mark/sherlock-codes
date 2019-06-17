/*
 * @lc app=leetcode id=14 lang=javascript
 *
 * [14] Longest Common Prefix
 */
/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
  // if (strs.length <= 1) return '';
  // let prefix = "";
  // const argLength = strs.length;

  // for (let i = 0; i < strs[0].length; i++) {
  //   if (strs[0][i] === strs[1][i] && strs[0][i] === strs[2][i])
  //     prefix += strs[0][i];
  // }

  // return prefix;

  let longestPrefix = '';
    if (strs.length > 0) {
      longestPrefix = strs[0];
      for (let i = 1; i < strs.length; i++) {
        for (let j = 0; j < longestPrefix.length; j++) {
          if (strs[i][j] != longestPrefix[j]) {
            longestPrefix = longestPrefix.slice(0, j);
            break;
          }
        }
      }
    }

    return longestPrefix;
};

// console.log(longestCommonPrefix(["flower","flow","flight"]));
// console.log(longestCommonPrefix(["dog","racecar","car"]));

