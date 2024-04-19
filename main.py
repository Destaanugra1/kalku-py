from flask import Flask, render_template, request
from fractions import Fraction

app = Flask(__name__)

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    return x / y if y != 0 else "Tidak bisa dibagi oleh nol."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hitung', methods=['POST'])
def hitung():
    if request.method == 'POST':
        num1 = Fraction(request.form['num1'])
        num2 = Fraction(request.form['num2'])
        operasi = request.form['operasi']

        if operasi == 'tambah':
            hasil = tambah(num1, num2)
        elif operasi == 'kurang':
            hasil = kurang(num1, num2)
        elif operasi == 'kali':
            hasil = kali(num1, num2)
        elif operasi == 'bagi':
            hasil = bagi(num1, num2)

        return render_template('hasil.html', hasil=hasil)

if __name__ == '__main__':
    app.run(debug=True)
