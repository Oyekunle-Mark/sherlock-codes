/**
 * Checks if a fixed increment of 1 converges with a fixed increment of 2
 * @param {number} x1
 * @param {number} v1
 * @param {number} x2
 * @param {number} v2
 * @returns {string}
 */
function kangaroo(x1, v1, x2, v2) {
  // if both the start point and jump rate of any kangaroo
  // is greater than start point and jump of the other
  // then, the answer is a 'NO'
  if ((x1 > x2 && v1 > v2) || (x2 > x1 && v2 > v1)) {
    return 'NO';
  }

  // initialize variables to hold the start point of both kangaroos
  let firstKangarooDistance = x1;
  let secondKangarooDistance = x2;

  // keep looping while kangaroos distance is not the same
  while (firstKangarooDistance !== secondKangarooDistance) {
    firstKangarooDistance += v1;
    secondKangarooDistance += v2;

    if (
      firstKangarooDistance >= 100000000 ||
      secondKangarooDistance >= 100000000
    )
      return 'NO';
  }

  return 'YES';
}
