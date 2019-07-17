/**
 * *Returns the not of a value
 * @param {any} b
 * @returns {boolean}
 */
function NOT(b) {
  if (b) return false;

  return true;
}

/**
 * *Returns the and of two arguments
 * @param {any} x
 * @param {any} y
 * @returns {boolean}
 */
function AND(x, y) {
  if (x) if (y) return true;

  return false;
}

/**
 * *Returns the not and of two arguments
 * @param {any} x
 * @param {any} y
 * @returns {boolean}
 */
function NAND(x, y) {
  if (x) if (y) return false;

  return true;
}

/**
 * *Returns the inclusive or of two arguments
 * @param {any} x
 * @param {any} y
 * @returns {boolean}
 */
function OR(x, y) {
  if (x) return true;

  if (y) return true;

  return false;
}

/**
 * *Returns the exclusive or of two arguments
 * @param {any} x
 * @param {any} y
 * @returns {boolean}
 */
function XOR(x, y) {
  if (x) if (y) return false;

  if (x) return true;

  if (y) return true;

  return false;
}

console.log('NOT 0:', NOT(0));
console.log('2 AND "hi":', AND(2, 'hi'));
console.log('2 NAND "hi":', NAND(2, 'hi'));
console.log('2 OR "":', OR(2, ''));
console.log('true XOR true:', XOR(true, true));
