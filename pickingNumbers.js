function pickingNumbers(a) {
  const nums = [...a].sort();
  const lengthOfSubArrays = [];
  let currentNum = nums[0];
  let subArray = [];

  nums.map(n => {
    if (Math.abs(currentNum - n) > 1) {
      currentNum = n;
      lengthOfSubArrays.push(subArray.length);
      subArray = [];
    }

    subArray.push(n);
  });

  return lengthOfSubArrays.length
    ? Math.max(...lengthOfSubArrays)
    : subArray.length;
}

console.log(
  'TCL: pickingNumbers([4, 6, 5, 3, 3, 1])',
  pickingNumbers([4, 6, 5, 3, 3, 1]),
);
console.log(
  'TCL: pickingNumbers([1, 2, 2, 3, 1, 2])',
  pickingNumbers([1, 2, 2, 3, 1, 2]),
);
console.log(
  'TCL: pickingNumbers([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])',
  pickingNumbers([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
);
