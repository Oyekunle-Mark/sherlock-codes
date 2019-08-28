function getMoneySpent(keyboards, drives, b) {
  const prices = [];

  for (let i = 0; i < keyboards.length; i++) {
    for (let j = 0; j < drives.length; j++) {
      const sum = keyboards[i] + drives[j];

      if (sum <= b) prices.push(sum);
    }
  }

  return prices.length ? Math.max(...prices) : -1;
}

console.log(
  'TCL: getMoneySpent([3, 1], [5, 2, 8], 10)',
  getMoneySpent([3, 1], [5, 2, 8], 10),
);
console.log('TCL: getMoneySpent([4], [5], 5)', getMoneySpent([4], [5], 5));
