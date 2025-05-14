async function scrapeWebsite() {
    const url = document.getElementById('url-input').value;
    const response = await fetch('/scrape', {
        method: 'POST',
        body: JSON.stringify({url: url}),
        headers: {'Content-Type': 'application/json'}
    });

    const data = await response.json();
    document.getElementById('scraped').innerText = data.scraped_content;
    document.getElementById('summary').innerText = data.summary;
}
