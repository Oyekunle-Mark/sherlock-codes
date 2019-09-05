function tickets(peopleInLine) {
  let cashAtHand = [];

  const deductChange = (bill, ch) => {
    change = [...ch];
    let len = change.length;

    if (bill === 50) {
      for (let i = 0; i < change.length; i++) {
        if (change[i] === 25) {
          change.shift();
          change.push(50);

          return change;
        }
      }

      return false;
    } else {
      let balance = 75;

      for (let i = 0; i < len; i++) {
        if (balance > 0) {
          if (change.includes(50)) {
            change.splice(change.indexOf(50), 1);
            balance -= 50;

            continue;
          }

          balance -= change[0];
          change.shift();
        }
      }

      return balance === 0 ? change : false;
    }
  };

  for (let i = 0; i < peopleInLine.length; i++) {
    if (peopleInLine[i] === 25) cashAtHand.push(25);
    else {
      if (cashAtHand.length === 0) return 'NO';

      cashAtHand = deductChange(peopleInLine[i], cashAtHand);

      if (!cashAtHand) break;
    }
  }

  return cashAtHand ? 'YES' : 'NO';
}

console.log('TCL: tickets([25, 25, 50])', tickets([25, 25, 50]));
console.log('TCL: tickets([25, 100])', tickets([25, 100]));
console.log(
  'TCL: tickets([25, 25, 50, 50, 100])',
  tickets([25, 25, 50, 50, 100]),
);
console.log(
  'TCL: tickets([25, 25, 25, 25, 50, 100, 50])',
  tickets([25, 25, 25, 25, 50, 100, 50]),
);
