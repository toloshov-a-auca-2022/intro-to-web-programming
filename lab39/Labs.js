//lab1

console.log("Start");
setTimeout(() => console.log("Inside setTimeout"), 2000);
console.log("End");


//lab2

function delayedOutput(text, waitTime) {
    setTimeout(() => console.log(text), waitTime);
}

delayedOutput("Hello, after 3 seconds!", 3000);

//lab3

function startCount() {
    let countValue = 1;
    let intervalId = setInterval(() => {
        console.log("Counter: " + countValue);
        if (countValue === 5) {
            clearInterval(intervalId);
        }
        countValue++;
    }, 1000);
}

startCount();

//lab4

function fetchInfo() {
    return new Promise(resolve => {
        setTimeout(() => resolve("Data received"), 2000);
    });
}

fetchInfo().then(result => console.log(result)).finally(() => console.log("Request completed"));


//lab5
//objective:Simulate a failed request using Promises.Instructions:Modify fetchData() to randomly either:Resolve with "Data received"Reject with "Error: Failed to fetch data"Use .then(), .catch(), and .finally() to handle the results.
function fetchInfo() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (Math.random() > 0.5) {
                resolve("Data received");
            } else {
                reject("Error: Failed to fetch data");
            }
        }, 2000);
    });
}

fetchInfo().then(result => console.log(result)).catch(error => console.error(error)).finally(() => console.log("Request completed"));
