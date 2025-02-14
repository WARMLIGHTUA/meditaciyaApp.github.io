// Theme handling - Set theme before page load
(function() {
    // Додаємо клас для запобігання миготіння під час завантаження
    document.documentElement.style.visibility = 'hidden';
    document.documentElement.classList.add('theme-changing');
    
    // Отримуємо та встановлюємо тему якомога раніше
    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const isDark = savedTheme ? savedTheme === 'dark' : prefersDark;
    
    document.documentElement.setAttribute('data-theme', isDark ? 'dark' : 'light');
    
    // Функція для відображення контенту
    function showContent() {
        document.documentElement.style.visibility = '';
        setTimeout(() => {
            document.documentElement.classList.remove('theme-changing');
        }, 300);
    }
    
    // Показуємо контент коли все завантажилось
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', showContent);
    } else {
        showContent();
    }
})();

// Main JavaScript file
document.addEventListener('DOMContentLoaded', function() {
    const html = document.documentElement;
    const themeSwitch = document.querySelector('.theme-switcher');
    const themeIcon = document.querySelector('.theme-icon');

    // Function to set theme
    function setTheme(isDark) {
        // Add class to prevent transitions
        html.classList.add('theme-changing');
        
        // Set theme
        html.setAttribute('data-theme', isDark ? 'dark' : 'light');
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
        
        if (themeIcon) {
            themeIcon.textContent = isDark ? '☀️' : '🌙';
        }
        
        // Remove transition prevention class after theme is set
        setTimeout(() => {
            html.classList.remove('theme-changing');
        }, 300);
    }

    // Theme switch handler
    if (themeSwitch) {
        themeSwitch.addEventListener('click', () => {
            const isDark = html.getAttribute('data-theme') === 'light';
            setTheme(isDark);
        });
    }

    // Listen for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!localStorage.getItem('theme')) {
            setTheme(e.matches);
        }
    });
});

// Handle audio player
document.addEventListener('DOMContentLoaded', function() {
    const audioPlayers = document.querySelectorAll('.audio-player');
    
    audioPlayers.forEach(player => {
        const audio = player.querySelector('audio');
        const playBtn = player.querySelector('.play-btn');
        const progressBar = player.querySelector('.progress');
        const timeDisplay = player.querySelector('.time');

        if (playBtn) {
            playBtn.addEventListener('click', () => {
                if (audio.paused) {
                    audio.play();
                    playBtn.textContent = 'Pause';
                } else {
                    audio.pause();
                    playBtn.textContent = 'Play';
                }
            });
        }

        if (audio && progressBar) {
            audio.addEventListener('timeupdate', () => {
                const progress = (audio.currentTime / audio.duration) * 100;
                progressBar.style.width = `${progress}%`;
                
                if (timeDisplay) {
                    const minutes = Math.floor(audio.currentTime / 60);
                    const seconds = Math.floor(audio.currentTime % 60);
                    timeDisplay.textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
                }
            });
        }
    });
});

// Handle mobile menu
document.addEventListener('DOMContentLoaded', function() {
    const menuButton = document.querySelector('.menu-toggle');
    const mobileMenu = document.querySelector('.mobile-menu');

    if (menuButton && mobileMenu) {
        menuButton.addEventListener('click', () => {
            mobileMenu.classList.toggle('active');
            menuButton.classList.toggle('active');
        });
    }
});

// Handle search
document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.querySelector('.search-form');
    const searchInput = document.querySelector('.search-input');

    if (searchForm && searchInput) {
        searchForm.addEventListener('submit', (e) => {
            if (!searchInput.value.trim()) {
                e.preventDefault();
            }
        });
    }
});

// Handle form validation
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;

            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('is-invalid');
                } else {
                    field.classList.remove('is-invalid');
                }
            });

            if (!isValid) {
                e.preventDefault();
            }
        });
    });
});

// Handle notifications
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.classList.add('fade-out');
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 3000);
}

// Register service worker
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/static/meditation/sw.js')
            .then(registration => {
                console.log('ServiceWorker registration successful');
            })
            .catch(err => {
                console.log('ServiceWorker registration failed: ', err);
            });
    });
} 