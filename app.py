from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/calculator/<string:num1>/<string:num2>/<string:operation>', methods=['GET'])
def calculator(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Error: Both num1 and num2 should be numbers.", 400
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed", 400
        result = num1 / num2
    else:
        return "Error: Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'.", 400
    return jsonify({
        "num1": num1,
        "num2": num2,
        "operation": operation,
        "result": result
    })

if __name__ == '__main__':
    app.run(debug=True)
