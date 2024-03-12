#!/usr/bin/node
function factorial (a) {
  if (parseInt(a) === 1 || isNaN(parseInt(a))) {
    return (1);
  }
  return parseInt(a) * factorial(parseInt(a) - 1);
}
console.log(factorial(process.argv[2]));
