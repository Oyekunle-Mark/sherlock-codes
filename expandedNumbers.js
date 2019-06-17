/**
 * *Expands the digits in a number.
 * @param {*} num
 * @returns {string}
 */
function expandedNums(num) {
  const modulo = 10;
  const numStr = num.toString();
  let expanded = [];
  
  for (let i = 0; i < numStr.length; i++) {
    if (numStr[i] === '0') continue;

    expanded.push(numStr[i] * Math.pow(modulo, numStr.length -1 - i));
  }

  return expanded.join(' + ');
}

console.log(expandedNums(562));
console.log(expandedNums(12345));
