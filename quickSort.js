/**
 * Sorts an array numbers with the quick sort algorithm
 * @param {*} arr array to be sorted
 * @returns
 */
function quickSort(arr) {
  if (arr.length < 2) return arr;

  const pivot = arr.pop();
  const left = [],
    right = [];

  for (const i of arr) {
    if (i <= pivot) left.push(i);
    else right.push(i);
  }

  return [...quickSort(left), pivot, ...quickSort(right)];
}

console.log(quickSort([2, 4, 6, 2, 9, 0, 23, 24, 22, 1]));
console.log(quickSort([55, -5, -10, 4]));
