let slideIndex = 0;

function showSlides() {
    const slides = document.querySelectorAll('.carousel-slide img');
    if (slideIndex >= slides.length) {
        slideIndex = 0;
    } else if (slideIndex < 0) {
        slideIndex = slides.length - 1;
    }

    slides.forEach((slide) => {
        slide.style.display = 'none';
    });

    slides[slideIndex].classList.add('animate__animated', 'animate__fadeIn');
    slides[slideIndex].style.display = 'block';
}

function nextSlide() {
    slideIndex++;
    showSlides();
}

function prevSlide() {
    slideIndex--;
    showSlides();
}

document.addEventListener('DOMContentLoaded', () => {
    showSlides();
});

// Menu Toggle

function toggleMenu() {
    var sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('active');
    var menuToggleIcon = document.querySelector('.menu-toggle');
    menuToggleIcon.classList.toggle('active');
}

