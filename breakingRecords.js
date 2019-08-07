function breakingRecords(scores) {
  let maxScore = scores[0];
  let minScore = scores[0];
  let brokeHighCount = 0,
    brokeLowCount = 0;

  scores.forEach(score => {
    if (score > maxScore) {
      brokeHighCount++;
      maxScore = score;
    } else if (score < minScore) {
      brokeLowCount++;
      minScore = score;
    }
  });

  return [brokeHighCount, brokeLowCount];
}

console.log(
  'TCL: breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42])',
  breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]),
);
console.log(
  'TCL: breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1])',
  breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]),
);
