// complexity O(log n) - I'm not sure
function numberDivisors(number) {
  const result = [];
  for (let divisor = 1; divisor < (number/divisor + 1); divisor++) {
    if (number % divisor === 0 && !result[divisor]) { result.push(divisor); result.push(number/divisor);}
  }
  return result;
}




console.log(numberDivisors(6)); // [1,6,2,3]
console.log(numberDivisors(1)); // [1, 1] a side effect for 1
console.log(numberDivisors(12543)); // [ 1, 12543, 3, 4181, 37, 339, 111, 113]
console.log(numberDivisors(543980)); // [1, 2, 4, 10, 20, 59, 118, 236, 295, 461, 590, 922, 1180, 1844, 2305, 4610, 9220, 27199, 54398, 135995, 271990, 543980] or originall 
/*[
  1, 543980,   2, 271990,
  4, 135995,  10,  54398,
 20,  27199,  59,   9220,
118,   4610, 236,   2305,
295,   1844, 461,   1180,
590,    922
]*/