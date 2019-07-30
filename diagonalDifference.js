function diagonalDifference(arr) {
  const length = arr.length - 1;
  let primaryDiagonal = 0,
    secondaryDiagonal = 0;

  for (let i = 0, j = length; i <= length; i++, j--) {
    primaryDiagonal += arr[i][i];
    secondaryDiagonal += arr[i][j];
  }

  return Math.abs(primaryDiagonal - secondaryDiagonal);
}

console.log(
  'TCL: diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]])',
  diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]),
);
console.log(
  'TCL: diagonalDifference([[1, 2, 3], [4, 5, 6], [7, 8, 9]])',
  diagonalDifference([[1, 2, 3], [4, 5, 6], [9, 8, 9]]),
);
