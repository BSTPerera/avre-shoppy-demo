from flask import Flask, render_template, request

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Vision Pro X1", "price": 3499.99, "image": "https://images.unsplash.com/photo-1622979135225-d2ba269cf1ac?w=500"},
    {"id": 2, "name": "Keychron Q3 Pro", "price": 189.50, "image": "https://images.unsplash.com/photo-1595225476474-87563907a212?w=500"},
    {"id": 3, "name": "LG C3 OLED TV", "price": 1299.00, "image": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500"},
]

@app.route('/')
def index():
    query = request.args.get('q', '')
    return render_template('home.html', products=PRODUCTS, query=query)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
