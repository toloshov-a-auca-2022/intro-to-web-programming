const images = document.querySelectorAll(".gallery-item");
let currentIndex = 0;

document.querySelectorAll(".gallery-item").forEach((img, index) => {
    img.addEventListener("click", function() {
        currentIndex = index;
        showImage();
    });
});

function showImage() {
    modal.style.display = "flex";
    modalImg.src = images[currentIndex].src;
}

document.getElementById("prev").addEventListener("click", function() {
    currentIndex = (currentIndex >  1) ? currentIndex - 1 : images.length - 1;
    showImage();
});

document.getElementById("next").addEventListener("click", function() {
    currentIndex = (currentIndex <  images.length - 1) ? currentIndex + 1 : 0;
    showImage();
})