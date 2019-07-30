function aVeryBigSum(ar) {
  return [...ar].reduce((a, b) => a + b, 0);
}

console.log(
  'TCL: aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005])',
  aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]),
);
