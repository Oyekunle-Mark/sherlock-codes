/**
 * Checks if a fixed increment of 1 converges with a fixed increment of 2
 * @param {number} x1
 * @param {number} v1
 * @param {number} x2
 * @param {number} v2
 * @returns
 */
function kangaroo(x1, v1, x2, v2) {
  if ((x1 > x2 && v1 > v2) || (x2 > x1 && v2 > v1)) return 'NO';

  let firstKangarooDistance = x1,
    secondKangarooDistance = x2;

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
