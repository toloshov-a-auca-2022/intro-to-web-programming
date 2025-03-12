// 1. JavaScript Operators
// Operators are symbols that perform operations on values or variables.
// Arithmetic Operators
// Why We Need Them:
// Arithmetic operators allow you to perform basic mathematical operations such as addition, subtraction, multiplication, and division. They are essential for calculations, data processing, and dynamically determining values in applications.
// Where to Use Them:
// Calculating totals, averages, or percentages in financial or data-driven applications.
// Manipulating numeric values in games, animations, or interactive interfaces.

let a = 10;
let b = 20;

console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(a / b);
console.log(a % b);

//Logical
console.log();

let isMember = true;
let hasCoupon = false;

console.log(isMember && hasCoupon)
console.log(isMember || hasCoupon)
console.log(!isMember)
console.log(!hasCoupon)

//Relational
console.log();

let x = 5;
let y = 10;
console.log(x > y);
console.log(x < y);
console.log(x == y);
console.log(x === y);
console.log(x != y);
console.log(x !== y);


//2. Conditional Constructions
// Conditional statements allow your code to execute different blocks of code based on certain conditions.
// if...else Statements
// Why We Need Them:
// The if...else statement lets you execute code only when a certain condition is met. It is one of the simplest ways to control the flow of your program based on boolean conditions.
let score = 85;
if (score >= 90){
    console.log("Grade: A");
} else if (score <= 90){
    console.log("Grade: B");
} else {
    console.log("Grade: C or below");
}

// switch
let day = 4;
switch (day){
    case 1: {
        console.log("Today is Saturday!");
        break;
    }
    case 2: {
        console.log("Today is Sunday!");
        break;
    }
    default: {
        console.log("Not weekend");
    }
}
// Ternary
console.log();

let isLoggedIn = true;
let welcomeMessage = isLoggedIn ? "Welcome to Your App!" : "Please log in!";
console.log(welcomeMessage);