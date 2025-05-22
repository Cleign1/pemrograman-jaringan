import random
from flask import Flask, render_template, request, session, redirect, url_for
 
app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def index():
    if 'angka' not in session:
        session['angka'] = random.randint(1, 100)
        session['attempts'] = 0
    return render_template('index.html')

@app.route('/tebak', methods=['POST'])
def tebak():
    tebakan = int(request.form['tebakan'])
    angka = session.get('angka', None) 
 
    if angka is None:
        return redirect(url_for('index'))
 
    session['attempts'] = session.get('attempts', 0) + 1
 
    if tebakan == angka:
        pesan = f"Selamat! Anda berhasil menebak angka {angka} dalam {session['attempts']} percobaan."
        session.pop('angka', None)
        session.pop('attempts', None)
    elif tebakan < angka:
        pesan = "Tebakan Anda terlalu rendah."  
    else:
        pesan = "Tebakan Anda terlalu tinggi."
 
    return render_template('hasil.html', pesan=pesan, attempts=session.get('attempts', 0))

@app.route('/reset')
def reset():
    session.pop('angka', None)
    session.pop('attempts', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)