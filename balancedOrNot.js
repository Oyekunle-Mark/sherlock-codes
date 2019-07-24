/*
 * Complete the 'balancedOrNot' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. STRING_ARRAY expressions
 *  2. INTEGER_ARRAY maxReplacements
 */

function balancedOrNot(expressions, maxReplacements) {
  const resultArray = [];

  for (let i = 0; i < expressions.length; i++) {
    resultArray.push(determineBalanced(expressions[i], maxReplacements[i]));
  }

  return resultArray;
}

const determineBalanced = (exp, maxRep) => {
  const holder = [];
  let count = 0;

  for (const i of exp) {
    if (i === '<') {
      holder.push(i);
      continue;
    }
    if (i === '>') {
      if (holder.length === 0) {
        count++;
        continue;
      }
      holder.pop();
      // count--;
    }
  }

  if (holder.length) {
    let x = true;
    for (let i of holder) {
      if (i === '>') x = false;
    }
    return x ? 0 : 1;
  }

  return count <= maxRep ? 1 : 0;
};

console.log(determineBalanced('<>>>', 2));
console.log(determineBalanced('<>>>>', 2));
console.log(determineBalanced('<>', 1));
// console.log(determineBalanced('<<>>', 0));
console.log(determineBalanced('<<<><><>', 2));
