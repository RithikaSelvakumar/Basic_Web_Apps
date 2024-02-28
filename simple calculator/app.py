from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    try:
        result = str(eval(expression))
        if result == 'nan' or result == 'inf' or result == '-inf':
            return "Result not defined"
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"

if __name__ == '__main__':
    app.run(debug=True)
