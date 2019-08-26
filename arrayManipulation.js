function arrayManipulation(n, queries) {
  const arr = Array(n).fill(0);

  for (let i = 0; i < queries.length; i++) {
    for (let j = queries[i][0]; j <= queries[i][1]; j++) {
      arr[j - 1] += queries[i][2];
    }
  }

  return Math.max(...arr);
}

console.log(
  'TCL: arrayManipulation(10, [[1, 5, 3], [4, 8, 7], [6, 9, 1]])',
  arrayManipulation(10, [[1, 5, 3], [4, 8, 7], [6, 9, 1]]),
);
console.log(
  'TCL: arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]])',
  arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]),
);
