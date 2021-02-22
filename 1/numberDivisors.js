function numberDivisors(number) {
  const result = [number];
  for (let divisor = 1; divisor < number; divisor++) {
    if (number % divisor === 0) result.push(divisor);
  }
  return result;
}

console.log(numberDivisors(6)); // [1,2,3,6]
console.log(numberDivisors(1)); // [1]