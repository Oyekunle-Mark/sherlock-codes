function sockMerchant(n, ar) {
  const numOfEachSock = {};
  let pairs = 0;

  for (let i = 0; i < n; i++) {
    if (!numOfEachSock[`${ar[i]}`]) numOfEachSock[`${ar[i]}`] = 0;

    numOfEachSock[`${ar[i]}`] += 1;
  }

  for (const key in numOfEachSock) {
    const num = numOfEachSock[key];

    if (num >= 2) pairs += Math.floor(num / 2);
  }

  return pairs;
}
