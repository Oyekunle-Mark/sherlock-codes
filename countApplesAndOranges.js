function countApplesAndOranges(s, t, a, b, apples, oranges) {
  const fruitsFallOnHouse = (pos1, pos2, dist, arr) => {
    let count = 0;

    const fruitsPos = arr.map(fruit => fruit + dist);

    fruitsPos.map(item => {
      if (item >= pos1 && item <= pos2) count++;
    });

    return count;
  };

  console.log(fruitsFallOnHouse(s, t, a, apples));
  console.log(fruitsFallOnHouse(s, t, b, oranges));
}

countApplesAndOranges(7, 11, 5, 15, [-2, 0, 1], [5, -6]);
countApplesAndOranges(7, 10, 4, 12, [2, 3, -4], [3, -2, -4]);
