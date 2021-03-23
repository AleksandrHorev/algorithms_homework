// the task: we have a matrix. we want to calculate how many ways to come to the bottom-right angle. we can move on 1 to right, bot and right-bot cell
function countMatrixSteps(rows, columns) {
  const matrix = new Array(rows);
  for (let i = 0; i < rows; i++) {
    matrix[i] = (new Array(columns).fill(0))
  }
  matrix[0][0] = 1;
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < columns; j++) {
      if (matrix[i - 1] && matrix[i - 1][j]) {
        matrix[i][j] += matrix[i - 1][j];
      }
      if (matrix[i][j - 1]) {
        matrix[i][j] += matrix[i][j - 1];
      }
      if (matrix[i - 1] && matrix[i - 1][j - 1]) {
        matrix[i][j] += matrix[i - 1][j - 1];
      }
    }
  } 

  return matrix[rows - 1][columns - 1];
}

console.log(countMatrixSteps(3,5)); // 41
console.log(countMatrixSteps(1,1)); // 41
