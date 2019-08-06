function matchingStrings(strings, queries) {
  const matches = [];
  
  for(let i = 0; i < queries.length; i++) {
    let count = 0;
  
    for(let j = 0; j < strings.length; j++) {
      if (queries[i] === strings[j]) count++;
    }

    matches.push(count);
  }

  return matches;
}

console.log(
  "TCL: matchingStrings(['aba', 'baba', 'aba', 'xzxb'], [aba, xzxb, ab])",
  matchingStrings(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab']),
);
