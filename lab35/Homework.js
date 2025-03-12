//lab1
for (let j = 0; j < 10; j++) {
    console.log(j);
}


//lab2

let num = 10;
while (num >= 1) {
    console.log(num);
    num--;
}

//lab3

let userInput;
do {
    userInput = parseInt(prompt("Enter a number greater than 10: "), 10)
} while (userInput <= 10)
console.log("Valid input is received: " + userInput);

//lab4

const fruits = ["banana", "grape", "apple", "kiwi", "pineapple"];
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

//lab5

const fruits = ["banana", "grape", "apple", "kiwi", "pineapple"];
let i = 0;
while (i < fruits.length) {
    console.log(fruits[i]);
    i++;
}

//lab6

let numbers = [3, 7, 12, 5, 9]

for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] === 12) {
        console.log("The number 12 is found. Stopping the loop.")
        break;
    }

    console.log(numbers[i]);
}


//lab7
let numbers = [1, 2, 3, 4, 5, 6, 7];

for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] === 5) {
        continue; // we will not print the "5" per requirement of Lab
    }

    console.log(numbers[i]);
}