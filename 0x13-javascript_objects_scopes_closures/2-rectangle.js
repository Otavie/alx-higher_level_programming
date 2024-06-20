#!/usr/bin/node

class Rectangle {
  // This is a class that defines a rectangle with width and height
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      this.width = 0;
      this.height = 0;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
