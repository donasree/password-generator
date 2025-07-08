# app.py

from flask import Flask, request, render_template, jsonify
from passwordgen import generate_password

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()

    length = data.get('length', 12)
    use_upper = data.get('use_upper', True)
    use_lower = data.get('use_lower', True)
    use_digits = data.get('use_digits', True)
    use_special = data.get('use_special', True)

    password = generate_password(
        length=int(length),
        use_upper=use_upper,
        use_lower=use_lower,
        use_digits=use_digits,
        use_special=use_special
    )

    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
