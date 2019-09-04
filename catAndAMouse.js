function catAndMouse(x, y, z) {
  const posCatA = Math.abs(z - x);
  const posCatB = Math.abs(z - y);

  return posCatA === posCatB
    ? 'Mouse C'
    : posCatA > posCatB
    ? 'Cat B'
    : 'Cat A';
}

console.log('TCL: catAndMouse(1, 2, 3)', catAndMouse(1, 2, 3));
console.log('TCL: catAndMouse(1, 3, 2)', catAndMouse(1, 3, 2));
