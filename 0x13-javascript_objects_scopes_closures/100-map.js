#!/usr/bin/node
const list = require('./100-data').list;

const newList = list.map((value, ind) => value * ind);
console.log(list);
console.log(newList);
