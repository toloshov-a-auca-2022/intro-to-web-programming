document.getElementById("myForm").addEventListener("submit", function(event) {
    event.preventDefault();
    document.getElementById("message").innerText = "Form submission prevented!";
});
