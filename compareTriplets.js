function compareTriplets(a, b) {
  const arr1 = [...a],
    arr2 = [...b];
  let score1 = 0,
    score2 = 0;

  for (let i = 0; i < arr1.length; i++) {
    if (arr1[i] > arr2[i]) score1++;
    else if (arr1[i] < arr2[i]) score2++;
  }

  return [score1, score2];
}

console.log(
  'TCL: compareTriplets([5, 6, 7], [3, 6, 10])',
  compareTriplets([5, 6, 7], [3, 6, 10]),
);
console.log(
  'TCL: compareTriplets([17, 28, 30], [99, 16, 8])',
  compareTriplets([17, 28, 30], [99, 16, 8]),
);
