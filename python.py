from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = num1 + num2
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/subtract', methods=['GET'])
def subtract():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = num1 - num2
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/multiply', methods=['GET'])
def multiply():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = num1 * num2
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/divide', methods=['GET'])
def divide():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        if num2 == 0:
            return jsonify({'error': 'Cannot divide by zero'})
        result = num1 / num2
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/power', methods=['GET'])
def power():
    try:
        base = float(request.args.get('base'))
        exponent = float(request.args.get('exponent'))
        result = math.pow(base, exponent)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/sqrt', methods=['GET'])
def sqrt():
    try:
        num = float(request.args.get('num'))
        result = math.sqrt(num)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/sin', methods=['GET'])
def sin():
    try:
        angle = float(request.args.get('angle'))
        result = math.sin(math.radians(angle))
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/cos', methods=['GET'])
def cos():
    try:
        angle = float(request.args.get('angle'))
        result = math.cos(math.radians(angle))
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/tan', methods=['GET'])
def tan():
    try:
        angle = float(request.args.get('angle'))
        result = math.tan(math.radians(angle))
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/log', methods=['GET'])
def log():
    try:
        num = float(request.args.get('num'))
        result = math.log10(num)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/ln', methods=['GET'])
def ln():
    try:
        num = float(request.args.get('num'))
        result = math.log(num)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/factorial', methods=['GET'])
def factorial():
    try:
        num = int(request.args.get('num'))
        result = math.factorial(num)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
