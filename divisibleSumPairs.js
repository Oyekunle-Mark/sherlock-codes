function divisibleSumPairs(n, k, ar) {
  let divisiblePair = 0;

  for (let i = 0; i < ar.length; i++) {
    for (let j = i + 1; j < ar.length; j++) {
      if ((ar[i] + ar[j]) % k === 0) divisiblePair++;
    }
  }

  return divisiblePair;
}

console.log(
  'TCL: divisibleSumPairs(6, 3, [1, 2, 3, 4, 5, 6])',
  divisibleSumPairs(6, 5, [1, 2, 3, 4, 5, 6]),
);
console.log(
  'TCL: divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2])',
  divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]),
);
