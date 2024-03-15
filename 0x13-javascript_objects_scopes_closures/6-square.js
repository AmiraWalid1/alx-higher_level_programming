#!/usr/bin/node

const Square5 = require('./5-square');
class Square extends Square5 {

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let shape = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          shape += c;
        }
        if (i !== this.height - 1) {
          shape += '\n';
        }
      }
      console.log(shape);
    }
  }
}
module.exports = Square;
