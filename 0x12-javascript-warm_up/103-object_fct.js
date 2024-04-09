#!/usr/bin/node

const myObject = {
	type: 'object',
	value: 12
};
console.log(myObject);

myObject.incr = functon () {
	this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
myObject.incr();
console.log(myObject);
