//1. Array Methods
// Arrays in JavaScript come with many built-in methods that simplify common operations. Here are some key methods:
// push and pop
// Why We Need Them:
// push adds an element to the end of an array, and pop removes the last element. They are essential for working with dynamic lists where items are added or removed frequently.
// Where to Use Them:
// Use these methods when managing lists like a stack (last-in, first-out), or when collecting user input and processing it sequentially.
// Examples:
let numbers = [1, 2, 3];
numbers.push(4);
let last = numbers.pop();
console.log(last);

// slice
console.log();

let fruits = ["banana", "apple", "kiwi", "melon"];
let someFruits = fruits.slice(1, 3);
console.log(someFruits);

// map
console.log();

let doubled = numbers.map(x => x * 2);
console.log(doubled);

// filter
console.log();

let evens = numbers.filter(x => x % 2 === 0);
console.log(evens);


// 2. Basic Operations with Objects
// Objects in JavaScript are collections of key-value pairs, making them ideal for representing structured data.
// Key-Value Pairs
// Why We Need Them:
// Objects allow you to group related data together in a structured manner. They help in organizing information and are used extensively for storing configuration settings, user data, and more.
// Where to Use Them:
// Use objects to represent entities such as a person, a product, or a configuration setting, where each property describes an aspect of that entity.
// Example:

const person = {
    name: "John",
    age: 25,
    occupation: "Farmer"
};
console.log(person.name);


console.log();

let keys = Object.keys(person);
let values = Object.values(person);

keys.forEach(key => {
    console.log(key + ": " + person[key]);
})