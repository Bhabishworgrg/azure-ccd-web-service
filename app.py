from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/')
def render_homepage():
    return render_template('index.html') 


@app.route('/service', methods=['GET'])
def convert_miles_kilometers():
    CONVERSION_FACTOR = 1.60934

    if 'miles' in request.args and 'kilometers' in request.args:
        return jsonify({ 'error': 'Service only takes one input' })

    elif 'miles' in request.args:
        value = float(request.args.get('miles'))
        result = round(value * CONVERSION_FACTOR, 2)    
        return jsonify({ 'miles': value, 'kilometers': result })
    
    elif 'kilometers' in request.args:
        value = float(request.args.get('kilometers'))
        result = round(value / CONVERSION_FACTOR, 2)
        return jsonify({ 'kilometers': value, 'miles': result })

    else:
        return jsonify({ 'error': 'No input found' })


if __name__ == '__main__':
    app.run()


