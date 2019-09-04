function formingMagicSquare(s) {
  const pattern = [
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
  ];

  const allCost = [];

  pattern.map(sq => {
    let cost = 0;

    sq.map((row, i) => {
      row.map((num, j) => {
        cost += Math.abs(num - s[i][j]);
      });
    });

    allCost.push(cost);
  });

  return Math.min(...allCost);
}

console.log(
  'TCL: formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]])',
  formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]]),
);
console.log(
  'TCL: formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]])',
  formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]]),
);
