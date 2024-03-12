#!/usr/bin/node
const callMeMoby = function (x, theFunction) {
  while (x > 0) {
    theFunction();
    x--;
  }
};
exports.callMeMoby = callMeMoby;
