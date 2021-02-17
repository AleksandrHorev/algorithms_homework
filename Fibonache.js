// with Recursion. it works once, need to reset resultFibonachhiRecursion each time 
function fibonachhiRecursion(countOfNumbers) {
  if (countOfNumbers < 2) throw new Error("countOfNumbers should be at least 2");

  const length = resultFibonachhiRecursion.length;
  if (countOfNumbers > length) {
    return fibonachhiRecursion(countOfNumbers, resultFibonachhiRecursion.push(resultFibonachhiRecursion[length - 1] + resultFibonachhiRecursion[length - 2]));
  }

  return resultFibonachhiRecursion;
}

const resultFibonachhiRecursion = [0, 1];
console.log(fibonachhiRecursion(10)); // [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]





// without Recursion
function fibonachhi(countOfNumbers) {
  const result = [];
  if (countOfNumbers >= 1) result.push(0);
  if (countOfNumbers >= 2) result.push(1);

  for (let i = 1; i < (countOfNumbers - 1); i++) {
    result.push(result[i] + result[i-1]);
  }
  return result;
}

console.log(fibonachhi(10)); // [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]