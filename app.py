from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)  # Habilita o CORS

def encrypt_password(password):
    substitution_map = {
        'a': '@', 'b': '8', 'c': '(', 'd': '[}', 'e': '3',
        'f': '#', 'g': '9', 'h': '#', 'i': '!', 'j': ';',
        'k': 'K', 'l': '1', 'm': '$', 'n': 'N', 'o': '0',
        'p': '%', 'q': 'Q', 'r': '#', 's': '5', 't': '7',
        'u': 'U', 'v': 'V', 'w': 'W', 'x': '*', 'y': 'Y', 'z': '2'
    }
    encrypted = ''.join([substitution_map.get(char.lower(), char) for char in password])
    return encrypted

def password_strength(password):
    strength_criteria = {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'numbers': bool(re.search(r'\d', password)),
        'special': bool(re.search(r'[@#$%^&*()_+!]', password)),
    }
    score = sum(strength_criteria.values())
    if score == 5:
        return "strong"
    elif 3 <= score < 5:
        return "medium"
    else:
        return "weak"

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    password = data.get('password', '')
    encrypted = encrypt_password(password)
    strength = password_strength(password)
    message = "Parabéns, agora você está mais seguro!" if strength == "strong" else "Considere melhorar sua senha para maior segurança."
    return jsonify({'encrypted': encrypted, 'strength': strength, 'message': message})

if __name__ == '__main__':
    app.run(debug=True)
