function toBinaryString(number) {
  let binary = '';

  if (number === 0) return '0';

  while (number >= 0) {
    if (number === 0) break;
    binary += (number % 2);
    number = Math.floor(number / 2 );
  }

  return [...binary].reverse().join('');
}

console.log('toBinaryString(6): ', toBinaryString(6));
