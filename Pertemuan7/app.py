import random
from flask import Flask, render_template, request
 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    min_val = int(request.form.get('min_val', 1))
    max_val = int(request.form.get('max_val', 100))
    
    # Ensure min is not greater than max
    if min_val > max_val:
        min_val, max_val = max_val, min_val
    
    random_number = random.randint(min_val, max_val)
    
    return render_template('hasil.html', 
                         random_number=random_number, 
                         min_val=min_val, 
                         max_val=max_val)

@app.route('/generate-multiple', methods=['POST'])
def generate_multiple():
    min_val = int(request.form.get('min_val', 1))
    max_val = int(request.form.get('max_val', 100))
    count = int(request.form.get('count', 5))
    
    # Ensure min is not greater than max
    if min_val > max_val:
        min_val, max_val = max_val, min_val
    
    # Limit count to reasonable number
    if count > 50:
        count = 50
    elif count < 1:
        count = 1
    
    random_numbers = [random.randint(min_val, max_val) for _ in range(count)]
    
    return render_template('hasil.html', 
                         random_numbers=random_numbers, 
                         min_val=min_val, 
                         max_val=max_val,
                         count=count)

if __name__ == '__main__':
    app.run(debug=True)