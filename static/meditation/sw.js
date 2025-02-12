const CACHE_NAME = 'meditation-app-v1';
const urlsToCache = [
    '/',
    '/static/meditation/css/styles.css',
    '/static/meditation/js/main.js',
    '/static/meditation/manifest.json',
    '/static/meditation/icons/icon-72x72.png',
    '/static/meditation/icons/icon-96x96.png',
    '/static/meditation/icons/icon-128x128.png',
    '/static/meditation/icons/icon-144x144.png',
    '/static/meditation/icons/icon-152x152.png',
    '/static/meditation/icons/icon-192x192.png',
    '/static/meditation/icons/icon-384x384.png',
    '/static/meditation/icons/icon-512x512.png'
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('Opened cache');
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                if (response) {
                    return response;
                }
                return fetch(event.request)
                    .then(response => {
                        if (!response || response.status !== 200 || response.type !== 'basic') {
                            return response;
                        }
                        const responseToCache = response.clone();
                        caches.open(CACHE_NAME)
                            .then(cache => {
                                cache.put(event.request, responseToCache);
                            });
                        return response;
                    });
            })
    );
}); 