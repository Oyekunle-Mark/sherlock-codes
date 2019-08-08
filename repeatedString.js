function repeatedString(s, n) {
  if (s.match(/^a$/)) return n;

  const numbersOfAs = s => {
    let count = 0;

    for (let i = 0; i < s.length; i++) {
      if (s[i] === 'a') count++;
    }

    return count;
  };

  const lengthOfStr = s.length;
  const numOfAsInInputString = numbersOfAs(s);

  if (n % lengthOfStr === 0) return numOfAsInInputString * (n / lengthOfStr);

  const stringInRepeatedSting = Math.floor(n / lengthOfStr);
  const stringRemaining = n % lengthOfStr;
  const aInRem = numbersOfAs(s.slice(0, stringRemaining));

  return numOfAsInInputString * stringInRepeatedSting + aInRem;
}

console.log("TCL: repeatedString('abcac', 10)", repeatedString('abcac', 10));
console.log("TCL: repeatedString('aba', 10)", repeatedString('aba', 10));
console.log(
  "TCL: repeatedString('a', 1000000)",
  repeatedString('a', 1000000000),
);
