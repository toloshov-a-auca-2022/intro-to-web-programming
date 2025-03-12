//1. Creating Functions
// Using the Function Keyword
// Why We Need It:
// Defining functions using the function keyword helps in organizing code into reusable units. Functions allow you to abstract logic, perform repeated operations, and improve readability.
// Where to Use It:
// When you have a set of operations that will be used multiple times.
// For event handling and processing user input.
// In utility modules to perform common tasks such as calculations or data formatting.
function greet(name) {
    return "Hello, " + name + "!";
}

console.log(greet("Adilet"));

// separate cases
console.log();

const hello = (name) => "Hello, " + name + "!";
console.log(hello("Adilet"));


// 2. Local and Global Scope
// Why We Need It:
// Scope determines the visibility and lifetime of variables. Understanding scope is essential for managing data and preventing conflicts between variables in different parts of your code.
// Global Scope
// Variables declared outside any function or block are in the global scope. They are accessible from anywhere in the code, which can be useful for data that needs to be shared across multiple functions. However, overusing global variables can lead to naming collisions and harder-to-maintain code.

let globalVar = "I am global!";

function display() {
    console.log(globalVar);
}

display();
console.log(globalVar);

// separate cases
console.log();

function localExample() {
    let localVar = "I am local!";
    console.log(localVar);
}
localExample();


//3. Closures
// Why We Need It:
// Closures are a powerful feature in JavaScript that allow functions to "remember" the environment in which they were created. They enable you to maintain private state and create functions with persistent data even after the outer function has finished executing.
// Where to Use It:
// To create private variables and encapsulate functionality.
// In event handlers and callback functions where you need access to variables from an outer scope.
// When implementing modules or factory functions that require state preservation.
function createCounter() {
    let count = 0;
    return function (){
        count++;
        return count;
    }
}

const counter = createCounter();
console.log(counter());
console.log(counter());
console.log(counter());
