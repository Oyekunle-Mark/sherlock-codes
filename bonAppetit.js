/**
 * Hacker rank bonAppetit challenge.
 * @param {number} bill
 * @param {number} k
 * @param {number} b
 */
function bonAppetit(bill, k, b) {
  const billWithoutAnna = [...bill];
  billWithoutAnna.splice(k, 1);

  const annaBill = billWithoutAnna.reduce((acc, val) => acc + val, 0) / 2;

  if (annaBill === b) console.log('Bon Appetit');
  else console.log(b - annaBill);
}

bonAppetit([3, 10, 2, 9], 1, 12);
bonAppetit([3, 10, 2, 9], 1, 7);
