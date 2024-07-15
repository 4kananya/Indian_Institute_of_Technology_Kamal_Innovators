from flask import Flask, request, jsonify
from flask_cors import CORS
from Scrappers.Blog_Scrappers.blog_scrapper import BlogScraper
from Scrappers.Image_Scrappers.image_scrapper import ImageScraper
from NER.fashion_trend_extractor import FashionTrendExtractor
from Outfit_Recommendation_System.outfit_recommender import OutfitGenerator


app = Flask(__name__)
CORS(app)  

blog_scraper = BlogScraper()
image_scraper = ImageScraper()
ner_trends  = FashionTrendExtractor()
outfit_generator = OutfitGenerator()

@app.route('/ner', methods=['POST'])
def ner():
    if request.method == 'POST':
        blogs = request.json.get('blogs')
        response = ner_trends.process_document(blogs)
        return jsonify({'response': response})
    else:
        return jsonify({'error': 'Invalid request method'}), 405


@app.route('/outfit', methods=['POST'])
def outfit():
    if request.method == 'POST':
        id = request.json.get('id')
        response = outfit_generator.generate_outfit(id)
        return jsonify({'response': response})
    else:
        return jsonify({'error': 'Invalid request method'}), 405
    

@app.route('/image', methods=['POST'])
def image():
    if request.method == 'POST':
        response = image_scraper.scrape_images()
        return jsonify({'response': response})
    else:
        return jsonify({'error': 'Invalid request method'}), 405

@app.route('/blog', methods=['POST'])
def blog():
    if request.method == 'POST':
        response = blog_scraper.scrape_blogs()
        return jsonify({'response': response})
    else:
        return jsonify({'error': 'Invalid request method'}), 405


if __name__ == '__main__':
    app.run(port=5050)
