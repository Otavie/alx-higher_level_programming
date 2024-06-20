#!/usr/bin/node
const list = require('./100-data');

const newList = list(map(value, ind) => value * ind);
