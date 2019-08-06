function getTotalX(a, b) {
  const arrayNumbersAreFactors = (numArray, fac) => {
    let isFactorOfAll = true;

    numArray.map(item => {
      if (fac % item !== 0) isFactorOfAll = false;
    });

    return isFactorOfAll;
  };

  const isFactorOfArrayNumbers = (fac, numArray) => {
    let factor = true;

    numArray.map(item => {
      if (item % fac !== 0) factor = false;
    });

    return factor;
  };

  let factor = Math.max(...a);
  const numsBetween = [];

  while (factor <= Math.min(...b)) {
    if (arrayNumbersAreFactors(a, factor) && isFactorOfArrayNumbers(factor, b))
      numsBetween.push(factor);

    factor++;
  }

  return numsBetween.length;
}

console.log(
  'TCL: getTotalX([2, 4], [16, 32, 96])',
  getTotalX([2, 4], [16, 32, 96]),
);
console.log('TCL: getTotalX([2, 6], [24, 36])', getTotalX([2, 6], [24, 36]));
console.log('TCL: getTotalX([3, 4], [24, 48])', getTotalX([3, 4], [24, 48]));
