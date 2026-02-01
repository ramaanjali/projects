document.addEventListener('DOMContentLoaded', function() {
    const starIconWrapper = document.querySelector('#star-icon');
    const starIcon = starIconWrapper.querySelector('i');
    const offersBox = document.getElementById('offers-box');

    if (starIconWrapper && offersBox) {
        starIconWrapper.addEventListener('click', function(e) {
            e.preventDefault();
            offersBox.classList.toggle('show');
            starIconWrapper.classList.toggle('sparkle');
        });
    }
});