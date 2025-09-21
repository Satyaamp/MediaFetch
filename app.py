from flask import Flask, render_template, request, redirect, send_file
import requests
import os
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)


PIXABAY_API_KEY = os.getenv('PIXABAY_API_KEY', 'default_value')
CATEGORIES = ['fashion', 'electronics', 'sports', 'food', 'travel', 'nature']

# Homepage
@app.route('/')
def home():
  
    trending_images = []
    trending_videos = []


    img_url = f'https://pixabay.com/api/?key={PIXABAY_API_KEY}&editors_choice=true&per_page=8'
    try:
        img_resp = requests.get(img_url).json()
        trending_images = [{
            'small': hit['previewURL'],
            'medium': hit['webformatURL'],
            'large': hit.get('largeImageURL', hit['webformatURL'])
        } for hit in img_resp.get('hits', [])]
    except:
        pass


    vid_url = f'https://pixabay.com/api/videos/?key={PIXABAY_API_KEY}&editors_choice=true&per_page=4'
    try:
        vid_resp = requests.get(vid_url).json()
        trending_videos = [hit['videos']['medium']['url'] for hit in vid_resp.get('hits', [])]
    except:
        pass

    return render_template('index.html', categories=CATEGORIES,
                           trending_images=trending_images,
                           trending_videos=trending_videos)


# Search route
@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    category = request.form.get('category', '')
    page = int(request.form.get('page', 1))
    per_page = 12


    import urllib.parse
    q = urllib.parse.quote(query)
    cat = urllib.parse.quote(category)

 
    img_url = f'https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={q}&category={cat}&image_type=photo&per_page={per_page}&page={page}'
    try:
        img_resp = requests.get(img_url).json()
    except requests.exceptions.JSONDecodeError:
        img_resp = {'hits': [], 'totalHits': 0}
    images = [{
        'small': hit['previewURL'],
        'medium': hit['webformatURL'],
        'large': hit.get('largeImageURL', hit['webformatURL'])
    } for hit in img_resp.get('hits', [])]

 
    vid_url = f'https://pixabay.com/api/videos/?key={PIXABAY_API_KEY}&q={q}&category={cat}&per_page={per_page}&page={page}'
    try:
        vid_resp = requests.get(vid_url).json()
    except requests.exceptions.JSONDecodeError:
        vid_resp = {'hits': []}
    videos = [hit['videos']['medium']['url'] for hit in vid_resp.get('hits', [])]


    total = img_resp.get('totalHits', 0)
    total_pages = (total // per_page) + (1 if total % per_page > 0 else 0)

    return render_template('results.html', images=images, videos=videos,
                           query=query, category=category, page=page,
                           total_pages=total_pages, categories=CATEGORIES)


@app.route('/download_image')
def download_image():
    img_url = request.args.get('url')
    query = request.args.get('query', 'media')
    if not img_url:
        return redirect('/')
    
    ext = img_url.split('.')[-1].split('?')[0]
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"MediaFetch_{query}_{timestamp}.{ext}"
    
    save_path = os.path.join('static', 'downloads', filename)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/140.0.0.0 Safari/537.36"
    }
    try:
        r = requests.get(img_url, headers=headers, stream=True)
        r.raise_for_status()
        with open(save_path, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
    except requests.exceptions.RequestException as e:
        return f"Error downloading image: {e}"

    return send_file(save_path, as_attachment=True)


@app.route('/download_video')
def download_video():
    vid_url = request.args.get('url')
    query = request.args.get('query', 'media')
    if not vid_url:
        return redirect('/')
    
    ext = vid_url.split('.')[-1].split('?')[0]
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"MediaFetch_{query}_{timestamp}.{ext}"
    
    save_path = os.path.join('static', 'downloads', filename)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/140.0.0.0 Safari/537.36"
    }
    try:
        r = requests.get(vid_url, headers=headers, stream=True)
        r.raise_for_status()
        with open(save_path, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
    except requests.exceptions.RequestException as e:
        return f"Error downloading video: {e}"

    return send_file(save_path, as_attachment=True)




@app.route('/autocomplete')
def autocomplete():
    term = request.args.get('term', '')
    suggestions = []

    if term:
        # Call Pixabay API
        url = f'https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={term}&per_page=10'
        try:
            resp = requests.get(url).json()
            for hit in resp.get('hits', []):
                tags = hit.get('tags', '').split(', ')
                for tag in tags:
                    if tag.lower().startswith(term.lower()) and tag not in suggestions:
                        suggestions.append(tag)
        except:
            pass

    return {'suggestions': suggestions[:10]}

if __name__ == '__main__':
    app.run(debug=True)
