// Scroll-triggered animations
document.addEventListener('DOMContentLoaded', function() {
    // Intersection Observer for animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
            }
        });
    }, observerOptions);

    // Observe all animate-on-scroll elements
    const animateElements = document.querySelectorAll('.animate-on-scroll');
    animateElements.forEach(el => observer.observe(el));

    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('nav a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Form validation
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            if (!validateForm()) {
                e.preventDefault();
            }
        });
    }

    // FAQ toggle
    const faqButtons = document.querySelectorAll('.faq-question');
    faqButtons.forEach(button => {
        button.addEventListener('click', function() {
            const targetId = this.getAttribute('data-toggle');
            const answer = document.getElementById(targetId);
            if (answer.style.maxHeight) {
                answer.style.maxHeight = null;
            } else {
                answer.style.maxHeight = answer.scrollHeight + 'px';
            }
        });
    });

    // Event tracking for banners
    const bannerLinks = document.querySelectorAll('.banner-link');
    bannerLinks.forEach(link => {
        link.addEventListener('click', function() {
            const banner = this.getAttribute('data-banner');
            // Google Analytics event
            gtag('event', 'banner_click', {
                'event_category': 'engagement',
                'event_label': banner
            });
        });
    });
});

function validateForm() {
    let isValid = true;

    // Name validation
    const name = document.getElementById('id_name');
    const nameError = document.getElementById('name-error');
    if (!name.value.trim()) {
        nameError.textContent = 'El nombre es requerido.';
        isValid = false;
    } else {
        nameError.textContent = '';
    }

    // Email validation
    const email = document.getElementById('id_email');
    const emailError = document.getElementById('email-error');
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email.value.trim()) {
        emailError.textContent = 'El email es requerido.';
        isValid = false;
    } else if (!emailRegex.test(email.value)) {
        emailError.textContent = 'Por favor ingresa un email válido.';
        isValid = false;
    } else {
        emailError.textContent = '';
    }

    // Message validation
    const message = document.getElementById('id_message');
    const messageError = document.getElementById('message-error');
    if (!message.value.trim()) {
        messageError.textContent = 'El mensaje es requerido.';
        isValid = false;
    } else {
        messageError.textContent = '';
    }

    return isValid;
}
