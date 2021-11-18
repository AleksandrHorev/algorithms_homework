// the task: we have a matrix. we want to calculate how many ways to come to the bottom-right angle. we can move on 1 to right, bot with step 1 or 2
function calculateMatrixStepJump(rows, columns) {
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
      if (matrix[i - 2] && matrix[i - 2][j]) {
        matrix[i][j] += matrix[i - 2][j];
      }
      if (matrix[i][j - 2]) {
        matrix[i][j] += matrix[i][j - 2];
      }
    }
  } 

  return matrix[rows - 1][columns - 1];
}

console.log(calculateMatrixStepJump(3,5)); // 71
console.log(calculateMatrixStepJump(3,6)); // 149
console.log(calculateMatrixStepJump(1,1)); // 1
