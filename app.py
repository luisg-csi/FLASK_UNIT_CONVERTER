from flask import Flask, render_template, request
import conversion_logic

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/length', methods=['GET', 'POST'])
def length():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = conversion_logic.convert_length(value, from_unit, to_unit)
    return render_template('length.html', result=result)

@app.route('/weight', methods=['GET', 'POST'])
def weight():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = conversion_logic.convert_weight(value, from_unit, to_unit)
    return render_template('weight.html', result=result)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = conversion_logic.convert_temperature(value, from_unit, to_unit)
    return render_template('temperature.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)