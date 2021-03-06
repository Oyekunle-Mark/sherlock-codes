/*
 * @lc app=leetcode id=35 lang=javascript
 *
 * [35] Search Insert Position
 */
/**
 * *Returns the position of insertion of a number in a sorted array
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
  let position = 0;

  for (const i of nums) {
    if (target > i) position++
  }

  return position;
};

