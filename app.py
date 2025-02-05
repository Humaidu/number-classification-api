from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import math

app = Flask(__name__)
CORS(app)  # Enable CORS

def is_prime(n):
    """Check if a number is prime.""" 
    if n < 2 or n != int(n):  # Exclude numbers < 2 and non-integers
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    if n != int(n):
        return False  # Armstrong numbers only apply to integers
    
    digits = [int(digit) for digit in str(abs(int(n)))]
    return n == sum(d ** len(digits) for d in digits)

def is_perfect(n):
    """Check if a number is a perfect number (only for positive integers)."""
    if n <= 0 or n != int(n):  # Exclude non-integers and negative numbers
        return False
    return n == sum(i for i in range(1, int(n)) if int(n) % i == 0)

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    """API endpoint to classify a number."""
    number = request.args.get("number")
    
    try:
        number = float(number)  # Allow floating-point values
    except ValueError:
        return jsonify({"number": number, "error": True}), 400

    properties = []
    
    if is_armstrong(number):
        properties.append("armstrong")
    
    properties.append("odd" if number % 2 else "even")

    # Fetch fun fact from Numbers API
    fun_fact_response = requests.get(f"http://numbersapi.com/{int(number)}/math?json")
    fun_fact = fun_fact_response.json().get("text", "No fun fact found.")

    return jsonify({
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
         "digit_sum": sum(int(digit) for digit in str(abs(int(number))) if digit.isdigit()),
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
