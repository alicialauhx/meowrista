document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById('search');
    const items = document.querySelectorAll('.item');

    searchInput.addEventListener('input', searchItems);

    searchInput.addEventListener('keypress', function (event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            searchItems();
        }
    })

    function searchItems() {
        const query = searchInput.value.toLowerCase();

        items.forEach(item => {
            const img = item.querySelector('a img');
            const altText = img ? img.alt.toLowerCase() : '';
            item.style.display = altText.includes(query) ? '' : 'none';
        });
    }
});