function quickSort(nums) {
  if (nums.length < 2) return nums;

  const pivot = nums.pop();
  const left = [],
    right = [];

  for (const i of nums) {
    if (i <= pivot) left.push(i);
    else right.push(i);
  }

  return [...quickSort(left), pivot, ...quickSort(right)];
}

console.log(quickSort([2, 4, 6, 2, 9, 0, 23, 24, 22, 1]));
console.log(quickSort([55, -5, -10, 4]));
