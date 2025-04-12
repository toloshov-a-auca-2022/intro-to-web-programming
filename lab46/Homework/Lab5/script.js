document.addEventListener("DOMContentLoaded", function () {
    const galleryContainer = document.getElementById("gallery");
    const modal = document.getElementById("modal");
    const modalImg = document.getElementById("modal-img");
    const closeModal = document.getElementById("close");
    const prevBtn = document.getElementById("prev");
    const nextBtn = document.getElementById("next");

    const imageUrls = [
        "../../Files/New-York.jpg",
        "../../Files/New-York-2.jpg",
        "../../Files/cat.jpg",
    ];

    let currentIndex = 0;

    imageUrls.forEach((url, index) => {
        const img = document.createElement("img");
        img.src = url;
        img.alt = `Gallery Image ${index + 1}`;
        img.dataset.index = index;
        galleryContainer.appendChild(img);

        img.addEventListener("click", function () {
            currentIndex = index;
            showModal();
        });
    });

    function showModal() {
        modal.classList.add("show");
        modalImg.src = imageUrls[currentIndex];
    }

    function closeModalHandler() {
        modal.classList.remove("show");
        setTimeout(() => {
            modal.style.display = "none";
        }, 400);
    }

    closeModal.addEventListener("click", closeModalHandler);

    window.addEventListener("click", (e) => {
        if (e.target === modal) {
            closeModalHandler();
        }
    });

    function nextImage() {
        currentIndex = (currentIndex + 1) % imageUrls.length;
        animateTransition();
    }

    function prevImage() {
        currentIndex = (currentIndex - 1 + imageUrls.length) % imageUrls.length;
        animateTransition();
    }

    function animateTransition() {
        modalImg.style.opacity = "0";
        setTimeout(() => {
            modalImg.src = imageUrls[currentIndex];
            modalImg.style.opacity = "1";
        }, 300);
    }

    nextBtn.addEventListener("click", nextImage);
    prevBtn.addEventListener("click", prevImage);
});