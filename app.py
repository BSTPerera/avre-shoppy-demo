from flask import Flask, render_template

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Hack-Proof Laptop", "price": 1299.99, "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500"},
    {"id": 2, "name": "Secure Router", "price": 199.50, "image": "https://images.unsplash.com/photo-1544197150-b99a580bbc7c?w=500"},
    {"id": 3, "name": "Privacy Screen", "price": 49.00, "image": "https://images.unsplash.com/photo-1587829745563-84b705c08dc6?w=500"},
]

@app.route('/')
def home():
    # Vulnerability is client-side in search.js
    return render_template('home.html', products=PRODUCTS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
