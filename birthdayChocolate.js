function birthday(s, d, m) {
  let bars = 0;

  s.map((_, i) => {
    const chunk = s.slice(i, i + m);
    const chunkSum = chunk.reduce((acc, val) => acc + val, 0);

    if (chunkSum === d) bars++;
  });

  return bars;
}

console.log(
  'TCL: birthday([2, 2, 1, 3, 2], 4, 2)',
  birthday([2, 2, 1, 3, 2], 4, 2),
);
console.log(
  'TCL: birthday([1, 2, 1, 3, 2], 3, 2)',
  birthday([1, 2, 1, 3, 2], 3, 2),
);
console.log(
  'TCL: birthday([1, 1, 1, 1, 1], 3, 2)',
  birthday([1, 1, 1, 1, 1], 3, 2),
);
