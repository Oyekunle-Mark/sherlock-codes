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

console.log(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]));
console.log(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]));
