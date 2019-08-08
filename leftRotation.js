function rotLeft(a, d) {
  const arr = [...a];

  for (let i = 0; i < d; i++) {
    arr.push(arr.shift());
  }

  return arr;
}

console.log('TCL: rotLeft([1, 2, 3, 4, 5], 2)', rotLeft([1, 2, 3, 4, 5], 2));
console.log('TCL: rotLeft([1, 2, 3, 4, 5], 4)', rotLeft([1, 2, 3, 4, 5], 4));
