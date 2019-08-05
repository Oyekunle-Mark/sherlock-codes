/*
 * Complete the 'gradingStudents' function below.
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY grades as parameter.
 */

function gradingStudents(grades) {
  return [...grades].map(item => {
    const nearestFiveMultiple = (Math.floor(item / 5) + 1) * 5;

    if (item < 38 || item % 5 === 0 || nearestFiveMultiple - item >= 3) return item;

    return nearestFiveMultiple;
  });
}

console.log(
  'TCL: gradingStudents(73, 67, 38, 33)',
  gradingStudents([73, 67, 38, 33]),
);
