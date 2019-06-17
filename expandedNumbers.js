function expandedNums(num) {
  const modulo = 10;
  const numStr = num.toString().split('');
  let expanded = [];
  
  for (let i = 0; i < numStr.length; i++) {
    if (numStr[i] === '0') continue;

    expanded.push(numStr[i] * Math.pow(modulo, numStr.length -1 - i));
  }

  return expanded.join(' + ');
}

console.log(expandedNums(562));
