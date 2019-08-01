function miniMaxSum(arr) {
  const sums = [];

  const findSums = (nums, index) => {
    let sum = 0;

    for (let i = 0; i < 4; i++) {
      if (index > 4) index -= 5;
      sum += nums[index];
      index++;
    }

    return sum;
  };

  for (let i = 0; i < 5; i++) {
    sums.push(findSums(arr, i));
  }

  console.log(Math.min(...sums), Math.max(...sums));
}

miniMaxSum([1, 2, 3, 4, 5]);
