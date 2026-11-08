from flask import Flask, render_template, redirect, url_for, abort

app = Flask(__name__)

# Data user dengan 3 status berbeda untuk pengujian kondisi if-elif-else
USER_DATABASE = {
    'admin': 'sudah_pakai',
    'budi': 'tersedia',
    'sitifatimah': 'sudah_pakai',
    'pelanggan1': 'tersedia'
}

DATA_PRODUK = {
    1: {
        "nama": "Kopi Susu Aren", 
        "harga": 18000, 
        "deskripsi": "Espresso dengan fresh milk dan manisnya gula aren asli.",
        "gambar": "https://images.unsplash.com/photo-1541167760496-1628856ab772?auto=format&fit=crop&w=600&q=80"
    },
    2: {
        "nama": "Caffè Latte", 
        "harga": 22000, 
        "deskripsi": "Perpaduan sempurna espresso dan steamed milk dengan foam lembut.",
        "gambar": "https://images.unsplash.com/photo-1570968915860-54d5c301fa9f?auto=format&fit=crop&w=600&q=80"
    },
    3: {
        "nama": "Americano Ice", 
        "harga": 15000, 
        "deskripsi": "Espresso shot dengan air dingin, menyegarkan hari-hari Anda.",
        "gambar": "https://images.unsplash.com/photo-1517701604599-bb29b565090c?auto=format&fit=crop&w=600&q=80"
    },
    4: {
        "nama": "Caramel Macchiato", 
        "harga": 25000, 
        "deskripsi": "Vanila, susu segar, espresso, dan saus karamel di atasnya.",
        "gambar": "https://images.unsplash.com/photo-1485808194679-f6ad6ca72a7f?auto=format&fit=crop&w=600&q=80"
    }
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tentang')
def tentang():
    return render_template('tentang.html')

@app.route('/produk')
def produk():
    return render_template('produk.html', daftar_produk=DATA_PRODUK)

@app.route('/kontak')
def kontak():
    return render_template('kontak.html')

# Dynamic Route untuk pengecekan username dengan 3 kondisi
@app.route('/cek/<username>')
def cek_username(username):
    uname_lower = username.lower()
    
    if uname_lower not in USER_DATABASE:
        status = "tidak_valid"
    elif USER_DATABASE[uname_lower] == "tersedia":
        status = "tersedia"
    else:
        status = "sudah_pakai"
        
    return render_template('cek_user.html', username=username, status=status)

@app.route('/produk/<int:id>')
def detail_produk(id):
    if id not in DATA_PRODUK:
        abort(404)
    return render_template('detail_produk.html', item=DATA_PRODUK[id], id=id)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)