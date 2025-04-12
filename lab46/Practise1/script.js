const modal = document.getElementById("modal");
const modalImg = document.getElementById("modal-img");
const closeBtn = document.querySelector(".close");

document.querySelectorAll(".gallery-item").forEach(img => {
    img.addEventListener("click", (e) => {
        modal.style.display = "flex";
        modalImg.src = this.src;
    });
});

closeBtn.addEventListener("click", function() {
    modal.style.display = "none";
});

window.addEventListener("click", function(event) {
    if(event.target === modal) {
        modal.style.display = "none";
    }
});