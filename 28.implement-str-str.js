/*
 * @lc app=leetcode id=28 lang=javascript
 *
 * [28] Implement strStr()
 */
/**
 * Determines the  position of a needle in a haystack
 * *Returns the index if found otherwise returns -1
 * !if needle is an empty string returns 0
 * 
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
  if (!needle.length) return 0;

  return haystack.indexOf(needle);
};

