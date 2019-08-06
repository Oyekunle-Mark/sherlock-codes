function matchingStrings(strings, queries) {
  const matches = [];
  const inputString = strings.join(' ');

  queries.forEach(item => {
    const pattern = new RegExp(`\\b${item}\\b`, 'g');
    const match = inputString.match(pattern);

    if (match === null) matches.push(0);
    else matches.push(match.length);
  })

  return matches;
}

console.log(
  "TCL: matchingStrings(['aba', 'baba', 'aba', 'xzxb'], [aba, xzxb, ab])",
  matchingStrings(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab']),
);
