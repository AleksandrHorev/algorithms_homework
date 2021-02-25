// the task: На вход даются числа n и k. Сколько всего последовательностей из 0 и 1 длины n, которые не содержат k единиц подряд?
function sameNumbersRow(countNumbers, sameInRow) {
  const zero = [1];
  const one = [1];
  let sameInRowCounter = sameInRow - 1; // -1 bcs we added one element during initialization of zero and one
  for (let i = 1; i < countNumbers; i++) {
    zero.push(zero[i - 1] + one[i - 1]);
    if (sameInRowCounter > 0) {
      one.push(zero[i - 1] + one[i - 1]);
      sameInRowCounter--;
    } else {
      one.push(zero[i - 1]);
      sameInRowCounter = sameInRow;
    }
  }
  return zero[countNumbers - 1] + one[countNumbers - 1];
}

console.log(sameNumbersRow(1, 2)); //2
console.log(sameNumbersRow(1, 1)); //2
console.log(sameNumbersRow(2, 1)); //3
console.log(sameNumbersRow(2, 2)); //4
console.log(sameNumbersRow(5, 2)); // 24
console.log(sameNumbersRow(3, 2)); // 6