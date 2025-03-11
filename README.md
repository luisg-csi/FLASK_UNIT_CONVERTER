# Unit Converter Web Application

A simple and efficient web application built with Flask that allows users to convert between different units of measurement.

## Features

- Convert between different units of:
  - Length (mm, cm, m, km, inch, foot, yard, mile)
  - Weight (mg, g, kg, oz, lb)
  - Temperature (Celsius, Fahrenheit, Kelvin)
- Clean and intuitive user interface
- Real-time conversion results
- Mobile-responsive design

## Technologies Used

- Python 3.x
- Flask
- HTML5
- CSS3

## Installation

1. Clone the repository
```bash
git clone https://github.com/luisg-csi/unit-converter.git

## Install the required dependencies
pip install flask
Run the application
python app.py
Open your web browser and navigate to http://localhost:5000

## Trae AI
I'll help you create a simple web application for unit conversion using Python with Flask for the backend and HTML/CSS for the frontend. Let's create this step by step.

First, let's set up the project structure:

```bash
pip install flask
 ```

1. First, create the main Flask application:
```python
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
 ```
```

2. Create the conversion logic:
```python
def convert_length(value, from_unit, to_unit):
    # Convert everything to meters first
    meters = {
        'millimeter': value * 0.001,
        'centimeter': value * 0.01,
        'meter': value,
        'kilometer': value * 1000,
        'inch': value * 0.0254,
        'foot': value * 0.3048,
        'yard': value * 0.9144,
        'mile': value * 1609.344
    }.get(from_unit, 0)

    # Convert from meters to target unit
    result = {
        'millimeter': meters / 0.001,
        'centimeter': meters / 0.01,
        'meter': meters,
        'kilometer': meters / 1000,
        'inch': meters / 0.0254,
        'foot': meters / 0.3048,
        'yard': meters / 0.9144,
        'mile': meters / 1609.344
    }.get(to_unit, 0)

    return round(result, 6)

def convert_weight(value, from_unit, to_unit):
    # Convert everything to grams first
    grams = {
        'milligram': value * 0.001,
        'gram': value,
        'kilogram': value * 1000,
        'ounce': value * 28.3495,
        'pound': value * 453.592
    }.get(from_unit, 0)

    # Convert from grams to target unit
    result = {
        'milligram': grams / 0.001,
        'gram': grams,
        'kilogram': grams / 1000,
        'ounce': grams / 28.3495,
        'pound': grams / 453.592
    }.get(to_unit, 0)

    return round(result, 6)

def convert_temperature(value, from_unit, to_unit):
    # Convert to Celsius first
    celsius = {
        'Celsius': value,
        'Fahrenheit': (value - 32) * 5/9,
        'Kelvin': value - 273.15
    }.get(from_unit, 0)

    # Convert from Celsius to target unit
    result = {
        'Celsius': celsius,
        'Fahrenheit': (celsius * 9/5) + 32,
        'Kelvin': celsius + 273.15
    }.get(to_unit, 0)

    return round(result, 2)
 ```
```

3. Create the templates folder and HTML files:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Unit Converter</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="container">
        <h1>Unit Converter</h1>
        <div class="links">
            <a href="{{ url_for('length') }}" class="button">Length Converter</a>
            <a href="{{ url_for('weight') }}" class="button">Weight Converter</a>
            <a href="{{ url_for('temperature') }}" class="button">Temperature Converter</a>
        </div>
    </div>
</body>
</html>
 ```
```

```html
<!DOCTYPE html>
<html>
<head>
    <title>Length Converter</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="container">
        <h1>Length Converter</h1>
        <form method="POST">
            <input type="number" step="any" name="value" required placeholder="Enter value">
            <select name="from_unit" required>
                <option value="millimeter">Millimeter</option>
                <option value="centimeter">Centimeter</option>
                <option value="meter">Meter</option>
                <option value="kilometer">Kilometer</option>
                <option value="inch">Inch</option>
                <option value="foot">Foot</option>
                <option value="yard">Yard</option>
                <option value="mile">Mile</option>
            </select>
            <span>to</span>
            <select name="to_unit" required>
                <option value="millimeter">Millimeter</option>
                <option value="centimeter">Centimeter</option>
                <option value="meter">Meter</option>
                <option value="kilometer">Kilometer</option>
                <option value="inch">Inch</option>
                <option value="foot">Foot</option>
                <option value="yard">Yard</option>
                <option value="mile">Mile</option>
            </select>
            <button type="submit">Convert</button>
        </form>
        {% if result is not none %}
        <div class="result">
            Result: {{ result }}
        </div>
        {% endif %}
        <a href="{{ url_for('home') }}" class="button">Back to Home</a>
    </div>
</body>
</html>
 ```
```

```html
<!DOCTYPE html>
<html>
<head>
    <title>Weight Converter</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="container">
        <h1>Weight Converter</h1>
        <form method="POST">
            <input type="number" step="any" name="value" required placeholder="Enter value">
            <select name="from_unit" required>
                <option value="milligram">Milligram</option>
                <option value="gram">Gram</option>
                <option value="kilogram">Kilogram</option>
                <option value="ounce">Ounce</option>
                <option value="pound">Pound</option>
            </select>
            <span>to</span>
            <select name="to_unit" required>
                <option value="milligram">Milligram</option>
                <option value="gram">Gram</option>
                <option value="kilogram">Kilogram</option>
                <option value="ounce">Ounce</option>
                <option value="pound">Pound</option>
            </select>
            <button type="submit">Convert</button>
        </form>
        {% if result is not none %}
        <div class="result">
            Result: {{ result }}
        </div>
        {% endif %}
        <a href="{{ url_for('home') }}" class="button">Back to Home</a>
    </div>
</body>
</html>
 ```
```

```html
<!DOCTYPE html>
<html>
<head>
    <title>Temperature Converter</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="container">
        <h1>Temperature Converter</h1>
        <form method="POST">
            <input type="number" step="any" name="value" required placeholder="Enter value">
            <select name="from_unit" required>
                <option value="Celsius">Celsius</option>
                <option value="Fahrenheit">Fahrenheit</option>
                <option value="Kelvin">Kelvin</option>
            </select>
            <span>to</span>
            <select name="to_unit" required>
                <option value="Celsius">Celsius</option>
                <option value="Fahrenheit">Fahrenheit</option>
                <option value="Kelvin">Kelvin</option>
            </select>
            <button type="submit">Convert</button>
        </form>
        {% if result is not none %}
        <div class="result">
            Result: {{ result }}
        </div>
        {% endif %}
        <a href="{{ url_for('home') }}" class="button">Back to Home</a>
    </div>
</body>
</html>
 ```
```

4. Create the CSS file:
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f0f0f0;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

h1 {
    text-align: center;
    color: #333;
}

form {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    align-items: center;
    margin: 20px 0;
}

input, select {
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
}

button {
    padding: 8px 16px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

.result {
    text-align: center;
    margin: 20px 0;
    padding: 10px;
    background-color: #e8f5e9;
    border-radius: 4px;
}

.links {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 20px;
}

.button {
    display: inline-block;
    padding: 8px 16px;
    background-color: #2196F3;
    color: white;
    text-decoration: none;
    border-radius: 4px;
    text-align: center;
}

.button:hover {
    background-color: #1976D2;
}
 ```

To run the application:

```bash
python app.py
 ```

The application will be available at http://localhost:5000 . It features:

1. A home page with links to different converters
2. Three separate pages for length, weight, and temperature conversion
3. Input validation
4. Clean and responsive design
5. Easy-to-use interface
6. Accurate conversion calculations
Each converter page has:

- Input field for the value
- Dropdown menus for selecting units
- Convert button
- Result display
- Back to home link
The application handles all the conversions server-side and displays the results immediately after form submission.

## Luis Gonzalez201
Copy

Delete

genera un archivo readme para subir el mini proyecto a github. explicando el proyecto como tal

## Trae AI
Used 1 Reference

conversion_logic.py 1-1

I'll create a README.md file for your unit converter project:

```markdown
# Unit Converter Web Application

A simple and efficient web application built with Flask that allows users to convert between different units of measurement.

## Features

- Convert between different units of:
  - Length (mm, cm, m, km, inch, foot, yard, mile)
  - Weight (mg, g, kg, oz, lb)
  - Temperature (Celsius, Fahrenheit, Kelvin)
- Clean and intuitive user interface
- Real-time conversion results
- Mobile-responsive design

## Technologies Used

- Python 3.x
- Flask
- HTML5
- CSS3

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/unit-converter.git
 ```
```

2. Install the required dependencies
```bash
pip install flask
 ```

3. Run the application
```bash
python app.py
 ```

4. Open your web browser and navigate to http://localhost:5000
## Project Structure
unit-converter/
│
├── app.py                 # Main Flask application
├── conversion_logic.py    # Conversion calculations
├── static/
│   └── style.css         # CSS styles
│
└── templates/
    ├── index.html        # Home page
    ├── length.html       # Length converter page
    ├── weight.html       # Weight converter page
    └── temperature.html  # Temperature converter page
