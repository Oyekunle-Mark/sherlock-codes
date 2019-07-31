function plusMinus(arr) {
  let pos = 0,
    neg = 0,
    zero = 0,
    arrLength = arr.length;

  [...arr].map(item => {
    if (item > 0) pos++;
    else if (item < 0) neg++;
    else zero++;
  });

  console.log(parseFloat(pos / arrLength).toFixed(6));
  console.log(parseFloat(neg / arrLength).toFixed(6));
  console.log(parseFloat(zero / arrLength).toFixed(6));
}

plusMinus([-4, 3, -9, 0, 4, 1]);
