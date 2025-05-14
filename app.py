from flask import Flask, render_template, request, jsonify
from utils.scraper import scrape_website
from utils.llm_handler import get_llm_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json['url']
    scraped_content = scrape_website(url)
    summary = get_llm_response(scraped_content, "Summarize this content", model_name='mistral')
    return jsonify({'scraped_content': scraped_content, 'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
