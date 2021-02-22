function fibonachhiRecursion(indexOfNumber, arr) {
  if (arr[indexOfNumber]) return arr[indexOfNumber];
  arr.push(arr[arr.length - 1] + arr[arr.length - 2]);
  return fibonachhiRecursion(indexOfNumber, arr);
}

console.log(fibonachhiRecursion(10, [0, 1])); // 55