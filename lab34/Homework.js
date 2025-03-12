//lab1
let a = 15;
let b = 5;

console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(a / b);
console.log(a % b);
console.log(a ** b);

//lab2
let age = 25;
let isRegistered = true;
if (age <= 18 && isRegistered) {
    console.log("You are eligible to vote!")
} else {
    console.log("You are not eligible to vote!")
}

//lab3

let a = 10;
let b = 90;

if (a > b) {
    console.log(a + " is greater than " + b);
} else if (a < b) {
    console.log(a + " is less than " + b);
} else {
    console.log("Given numbers are equal!");
}

//lab4
let a = -19;

if (a < 0){
    console.log(a + " is a negative number!");
} else if (a > 0) {
    console.log(a + " is a positive number!");
} else {
    console.log("Given number is equal to " + a)
}

//lab5

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

//lab6
let number = -8;

console.log(number % 2 === 0 ? number + " is an even number!" : number + " is an odd number!");

