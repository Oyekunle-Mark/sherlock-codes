function countingValleys(n, s) {
  let level = 0;
  let valleys = 0;

  for (let i = 0; i < n; i++) {
    if (level === 0 && s[i] === 'D') valleys += 1;

    if (s[i] === 'U') level += 1;
    else level -= 1;
  }

  return valleys;
}

console.log(countingValleys(8, 'UDDDUDUU'));
console.log(countingValleys(8, 'DDUUUUDD'));
console.log(countingValleys(12, 'DDUUDDUDUUUD'));
