// loops

for (let i = 0; i < 5; i++){
    console.log(i);
}

// while
console.log();

let i = 5;
while (i < 10){
    console.log(i);
    i++;
}

// do-while
console.log();

i = 10;
do {
    console.log(i);
    i++;
} while (i < 15);


//2. Working with Arrays in Loops

//Why We Need It:
// Arrays are a common way to store collections of data. Loops allow us to iterate over each element in an array to perform operations like transformation, filtering, or aggregation.
// Where to Use It:
// Processing lists of items, such as user data, products, or search results.
// Displaying dynamic content on a web page.

let fruits = ["banana", "grape", "apple"];
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

//case 2
console.log();

let i = 0;
while (i < fruits.length) {
    console.log(fruits[i]);
    i++
}

// using break
console.log();

fruits = ["banana", "grape", "apple", "potatoes", "pineapple"];
for (let i = 0; i < fruits.length; i++) {
    if (fruits[i] === "potatoes") {
        console.log("Oops, you pick vegetable!");
        break;
    }

    console.log(fruits[i]);
}

// using continue

//break
// Why We Need It:
// The break statement exits a loop immediately, which is useful when a certain condition is met and there is no need to continue iterating.
// Where to Use It:
// Stopping the loop once a desired item is found in an array.
console.log();

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
i = 0;
while (i < numbers.length) {
    if (numbers[i] % 5 === 0) {
        console.log(numbers[i] + " is divisible by 5.");
        i++;
        continue;
    }

    console.log(numbers[i]);
    i++;
}