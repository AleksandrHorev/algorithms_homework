function differenceMinMaxValue(array) {
  if (array.lenght < 1) {
    throw new Error("Array must contain at least 2 numbers");
  }

  let max = array[0];
  let min = array[1];
  if (max < min) {
    max = min;
    min = array[0];
  }

  for (let i = 2; i < array.length; i++) {
    if (array[i] > max) {
      max = array[i];
      continue;
    }
    if (array[i] < min) {
      min = array[i];
      continue;
    }
  }
  return max - min;
}

// complexity is O(n)
console.log(differenceMinMaxValue([1,2,34,8,23,21,4,3,5, -8])); // 42
