const button = document.getElementById("eventButton");

button.addEventListener("click", function() {
    button.style.backgroundColor = "green";
});

button.addEventListener("mouseover", function() {
    button.style.backgroundColor = "blue";
});

button.addEventListener("mouseout", function() {
    button.style.backgroundColor = "gray";
});
