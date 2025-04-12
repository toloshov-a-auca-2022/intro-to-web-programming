document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("modal");
    const modalImg = document.getElementById("modal-img");
    const closeBtn = document.querySelector(".close");
    const nextBtn = document.querySelector(".next");
    const prevBtn = document.querySelector(".prev");

    const images = document.querySelectorAll(".gallery img");
    let currentIndex = 0;

    function openModal(index) {
        modal.style.display = "flex";
        modalImg.src = images[index].src;
        currentIndex = index;
    }

    images.forEach((img, index) => {
        img.addEventListener("click", () => openModal(index));
    });

    closeBtn.addEventListener("click", () => {
        modal.style.display = "none";
    });

    modal.addEventListener("click", (event) => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });

    nextBtn.addEventListener("click", () => {
        currentIndex = (currentIndex + 1) % images.length; // Loop to first
        modalImg.src = images[currentIndex].src;
    });

    prevBtn.addEventListener("click", () => {
        currentIndex = (currentIndex - 1 + images.length) % images.length; // Loop to last
        modalImg.src = images[currentIndex].src;
    });

    document.addEventListener("keydown", (event) => {
        if (modal.style.display === "flex") {
            if (event.key === "ArrowRight") nextBtn.click();
            if (event.key === "ArrowLeft") prevBtn.click();
            if (event.key === "Escape") closeBtn.click();
        }
    });
});