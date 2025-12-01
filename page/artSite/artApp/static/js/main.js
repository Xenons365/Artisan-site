document.addEventListener('DOMContentLoaded', () => {
    // Contact form validation
    const contactForm = document.querySelector('form[action=""]');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();

            if (!name || !email || !message) {
                e.preventDefault();
                alert('Please fill out all fields.');
            } else if (!validateEmail(email)) {
                e.preventDefault();
                alert('Please enter a valid email address.');
            }
        });
    }

    // Gallery modal
    const galleryItems = document.querySelectorAll('.gallery-item img');
    if (galleryItems.length > 0) {
        const modal = document.createElement('div');
        modal.classList.add('modal');
        document.body.appendChild(modal);

        const modalImg = document.createElement('img');
        modal.appendChild(modalImg);

        const closeBtn = document.createElement('span');
        closeBtn.classList.add('close');
        closeBtn.innerHTML = '&times;';
        modal.appendChild(closeBtn);

        galleryItems.forEach(item => {
            item.addEventListener('click', () => {
                modal.style.display = 'block';
                modalImg.src = item.src;
            });
        });

        closeBtn.addEventListener('click', () => {
            modal.style.display = 'none';
        });

        window.addEventListener('click', (e) => {
            if (e.target == modal) {
                modal.style.display = 'none';
            }
        });
    }

    function validateEmail(email) {
        const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }
});
