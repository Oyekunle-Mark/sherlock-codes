function jumpingOnClouds(c) {
  let jumps = 0;

  for (let i = 0; i < c.length; i++) {
    if (c[i] === c[i + 1] && c[i] === c[i + 2]) {
      i++;
      jumps++;
      continue;
    }

    if (c[i + 1] === 0) jumps++;
  }

  return jumps;
}

console.log(
  'TCL: jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])',
  jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]),
);
console.log(
  'TCL: jumpingOnClouds([0, 0, 0, 0, 1, 0])',
  jumpingOnClouds([0, 0, 0, 0, 1, 0]),
);
console.log(
  'TCL: jumpingOnClouds([0, 0, 0, 1, 0, 0])',
  jumpingOnClouds([0, 0, 0, 1, 0, 0]),
);
