function NOT(b) {
  if (b) return false;

  return true;
}

function AND(x, y) {
  if (x) if (y) return true;

  return false;
}

function NAND(x, y) {
  if (x) if (y) return false;

  return true;
}

function OR(x, y) {
  if (x) return true;

  if (y) return true;

  return false;
}

function XOR(x, y) {
  if (x) if (y) return false;

  if (x) return true;

  if (y) return true;

  return false;
}
