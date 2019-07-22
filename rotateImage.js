/**
 * Given an image represented by an NxN matrix,
 * where each pixel in the image is an integer from 0 - 9,
 * write a method to rotate the image by 90 degrees counterclockwise.
 * !This solution works in place
 * @param {array[]} arr
 * @returns {array[]}
 */
function rotateImage(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      arr[j].unshift(arr[i].pop())
    }
  }

  return arr.map(ar => ar.reverse());
}

console.log(rotateImage([[1, 2], [3, 4]]));
console.log(
  rotateImage([
    [1, 1, 5, 9, 9],
    [2, 2, 6, 0, 0],
    [3, 3, 7, 1, 1],
    [4, 4, 8, 2, 2],
    [5, 5, 9, 3, 3],
  ]),
);
