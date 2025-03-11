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