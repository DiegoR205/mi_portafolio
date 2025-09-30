// Form validation
document.addEventListener('DOMContentLoaded', function() {
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
