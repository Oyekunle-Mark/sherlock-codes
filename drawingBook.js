function pageCount(n, p) {
  const books = [];
  let pages = [];

  for (let i = 1; i <= n; i++) {
    if (i % 2 === 0) {
      pages.push(i);

      if (i === n) books.push(pages);
    } else {
      pages.push(i);
      books.push(pages);
      pages = [];
    }
  }

  let countFromFront = 0;
  let countFromBehind = 0;

  for (let pages of books) {
    if (pages.includes(p)) break;

    countFromFront += 1;
  }

  for (let pages of [...books].reverse()) {
    if (pages.includes(p)) break;

    countFromBehind += 1;
  }

  return Math.min(countFromBehind, countFromFront);
}

console.log(pageCount(6, 2));
console.log(pageCount(5, 4));
