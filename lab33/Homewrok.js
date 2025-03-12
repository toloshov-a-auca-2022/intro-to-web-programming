//lab1

let greeting = "Welcome to Javascript!"
let alertMessage = "Javascript is working!";

console.log(greeting, "\n", alertMessage);

//lab2

var userName = "Johnny";
let age = 35;
const country = "UEA"

console.log(userName, age, country)

userName = "Michael";
age = 45;
// country = "Mexico"; const variable cannot be changed
console.log(userName, age, country)

//lab3

let name = "John";
console.log("Name: " + name + " - Type: " + typeof(name));

let age = 28;
console.log("Age: " + age + " - Type: " + typeof(age));

let isStudent = true;
console.log("Is Student: " + isStudent + " - Type: " + typeof(isStudent));

let score = null;
console.log("Score: " + score + " - Type: " + typeof(score));

let address;
console.log("Address: " + address + " - Type: " + typeof(address));

//lab4

let name = prompt("Enter your name: ");
let age = prompt("Enter your age: ");

alert("Hello, " + name + "! You are " + age + " years old!");