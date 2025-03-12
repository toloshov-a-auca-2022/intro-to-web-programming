//lab1
function sum(num1, num2) {
    return num1 + num2;
}
console.log(sum(5,6));

// Task 2
console.log();

const square = (num1) => num1 * num1;
console.log(square(5));

// Task 3
console.log();

function max(num1, num2) {
    return num1 > num2 ? num1 : num2;
}
console.log(max(5, 3));



//lab2

// Task 1
let globalVar = "Hello from global";
function display1() {
    console.log(globalVar);
}
display1();

// Task 2
console.log();

function display2 () {
    let localVar = "Hello from global";
    console.log(localVar);
}
display2();

// Task 3
console.log();

function display3() {
    let localVar = "Hello from global";
    console.log(localVar);
}
display3();
// console.log(localVar); gives an error

//lab3
// Task 1
let num1 = 2;
if (num1 <= 5) {
    var localVar = "Smaller than " + num1;
}
console.log(localVar);

// Task 2
console.log();

if (num1 <= 5) {
    let localLet = "Smaller than " + num1;
}
// console.log(localLet); gives an error

// Task 3
console.log();

if (num1 <= 5) {
    const localConst = "Smaller than " + num1;
}
// console.log(localConst); gives an error



//lab4
// Task 1
function createCounter() {
    let count = 0;
    return function () {
        count++;
        return count;
    }
}
const counter1 = createCounter();
console.log(counter1());
console.log(counter1());

// Task 2
console.log();

const counter2 = createCounter();
console.log(counter2());
console.log(counter2());