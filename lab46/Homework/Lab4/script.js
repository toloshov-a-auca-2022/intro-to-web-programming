document.addEventListener("DOMContentLoaded", function () {
    const galleryContainer = document.getElementById("gallery");

    const imageUrls = [
        "../../Files/New-York.jpg",
        "../../Files/New-York-2.jpg",
        "../../Files/cat.jpg",
    ];

    imageUrls.forEach(url => {
        const img = document.createElement("img");
        img.src = url;
        img.alt = "Gallery Image";
        galleryContainer.appendChild(img);
    });
});