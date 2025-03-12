document.getElementById("addItemButton").addEventListener("click", function() {
    let newItem = document.createElement("li"); // Create a new <li> element
    newItem.textContent = "New Item"; // Set its text content
    document.getElementById("itemList").appendChild(newItem); // Append to the <ul>
});
