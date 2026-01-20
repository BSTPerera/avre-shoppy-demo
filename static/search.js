document.getElementById('search-btn').addEventListener('click', () => {
    const query = document.getElementById('search-input').value;
    const resultsDiv = document.getElementById('search-results');

    if (query) {
        resultsDiv.style.display = 'block';
        // VULNERABILITY: DOM-based XSS via innerHTML
        resultsDiv.innerHTML = '<div class="alert alert-info">Found 0 results for: <b>' + query + '</b></div>';

        // Update URL without reload to mimic SPA feel
        const newUrl = new URL(window.location);
        newUrl.searchParams.set('q', query);
        window.history.pushState({}, '', newUrl);
    }
});

// Load from URL on start
document.addEventListener('DOMContentLoaded', () => {
    const params = new URLSearchParams(window.location.search);
    const query = params.get('q');
    if (query) {
        document.getElementById('search-input').value = query;
        document.getElementById('search-btn').click();
    }
});
