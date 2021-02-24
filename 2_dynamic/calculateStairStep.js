// the task: we have a stair. we want to calculate how is difficult to up on the N (first argument) step with K (second argument) steps per turn.
function calculateStairStep(numberStep, countStepsPerTurn, valueSteps) {
  const valueEachStepsSum = [...(valueSteps.slice(1, countStepsPerTurn + 1))];

  if(numberStep <= countStepsPerTurn) {
    return valueSteps[numberStep];
  }

  for (let i = countStepsPerTurn; i < numberStep; i++) {
    valueEachStepsSum.push(Math.min(...valueEachStepsSum.slice(i - countStepsPerTurn, i)) + valueSteps[i + 1]);
  }
  return valueEachStepsSum[numberStep - 1];
}

console.log(calculateStairStep(6, 3, [0, 1, 54, 3, 48, 5, 6, 7, 8, 8, 9, 10, 679])); // 9
console.log(calculateStairStep(4, 3, [0, 1, 54, 3, 4, 5, 6, 7, 8, 8, 9, 10, 679])); // 5
console.log(calculateStairStep(2, 1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 679])); // 3
console.log(calculateStairStep(1, 2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 679])); // 1
console.log(calculateStairStep(5, 5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 679])); // 5
