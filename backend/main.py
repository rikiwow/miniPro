from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    input_data1 = data.get('test', {}).get('input1', '')
    input_data2 = data.get('test', {}).get('input2', '')
    # Perform complex calculation (example)
    # result = sum(ord(char) for char in input_data)
    try:
        num1 = int(input_data1)
        num2 = int(input_data2)
        result = num1 + num2
    except ValueError:
        result = "Invalid input: input_data1 and input_data2 must be numbers"
    print(f"Calculation result: {result}")
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
