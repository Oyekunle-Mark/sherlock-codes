function negCheck (num1, num2) {
  if (num1 < 0 && num2 < 0 || num1 > 0 && num2 > 0) 
    return [false, Math.abs(num1), Math.abs(num2)];
  
  return [true, Math.abs(num1), Math.abs(num2)];
}

function multiply(x, y) {
  const arr = negCheck(x, y);
  let value = 0;
  
  for (let i = 0; i < arr[2]; i++)
    value += arr[1];
    
  if (x === 0 || y === 0) return 0;
    
  return arr[0] ? -value : value;
}

function divide(x, y) {
  const arr = negCheck(x, y);
  let value = 0;
  
  while(arr[1] >= arr[2]) {
    arr[1] -= arr[2];
    value += 1;
  }
  
  return arr[0] ? -value : value;
}

function modulo(x, y) {
  const arr = negCheck(x, y);
  
  while (arr[1] >= arr[2]) {
    arr[1] -= arr[2];
  }
  
  return x > 0 ? arr[1] : -arr[1];
}

console.log(negCheck(12, 34)); //   <--- [ false, 12, 34 ]
console.log(negCheck(-12, 34)); //  <--- [ true, 12, 34 ]
console.log(negCheck(12, -34)); //  <--- [ true, 12, 34 ]
console.log(negCheck(-12, -34)); // <--- [ false, 12, 34 ]
console.log(multiply(3, 4)); //     <--- 12
console.log(multiply(-3, 4)); //    <--- -12
console.log(multiply(3, -4)); //    <--- -12
console.log(multiply(-3, -4)); //   <--- 12
console.log(divide(10, 3)); //      <--- 3
console.log(divide(-10, 3)); //     <--- -3
console.log(divide(10, -3)); //     <--- -3
console.log(divide(-10, -3)); //    <--- 3
console.log(modulo(10, 3)); //      <--- 1
console.log(modulo(-10, 3)); //     <--- -1
console.log(modulo(10, -3)); //     <--- 1
console.log(modulo(-10, -3)); //    <--- -1
