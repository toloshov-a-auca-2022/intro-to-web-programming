// 2. JSON Conversion (response.json())

fetch("https://jsonplaceholder.typicode.com/todos/1")
    .then(response => response.json())
    .then(data => { console.log("Title:", data.title) })