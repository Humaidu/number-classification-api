from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(digit) for digit in str(n)]
    return n == sum(d ** len(digits) for d in digits)

def is_perfect(n):
    """Check if a number is a perfect number."""
    return n == sum(i for i in range(1, n) if n % i == 0)

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    """API endpoint to classify a number."""
    number = request.args.get("number")

    if not number or not number.isdigit():
        return jsonify({"number": number, "error": True}), 400

    number = int(number)
    properties = []
    
    if is_armstrong(number):
        properties.append("armstrong")
    
    properties.append("odd" if number % 2 else "even")

    # Fetch fun fact from Numbers API
    fun_fact_response = requests.get(f"http://numbersapi.com/{number}/math?json")
    fun_fact = fun_fact_response.json().get("text", "No fun fact found.")

    return jsonify({
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(number)),
        "fun_fact": fun_fact
    })
    
    # Example of how the json will be generated
    # {
    #     "number": 371,
    #     "is_prime": false,
    #     "is_perfect": false,
    #     "properties": ["armstrong", "odd"],
    #     "digit_sum": 11,  // sum of its digits
    #     "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
    # }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
