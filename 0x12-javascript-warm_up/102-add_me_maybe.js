#!/usr/bin/nodejs

// Write a function that increments and calls a function.
function addMeMaybe (number, thefunction) {
  number += 1;
  thefunction(number);
}

module.exports = {
  addMeMaybe: addMeMaybe
};
