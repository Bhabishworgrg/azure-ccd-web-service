from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/')
def render_homepage():
    return render_template('index.html') 


@app.route('/service', methods=['GET'])
def convert_miles_kilometers():
    MILE_KM_FACTOR = 1.60934
    MILE_YARD_FACTOR = 1760
    KM_YARD_FACTOR = 1093.61

    if len(request.args) > 1:
        return jsonify({ 'error': 'Service only takes one input' })

    elif 'miles' in request.args:
        miles = float(request.args.get('miles'))
        kilometers = round(miles * MILE_KM_FACTOR, 2)
        yards = round(miles * MILE_YARD_FACTOR, 2)
        return jsonify({ 'miles': miles, 'kilometers': kilometers, 'yards': yards })
    
    elif 'kilometers' in request.args:
        kilometers = float(request.args.get('kilometers'))
        miles = round(kilometers / MILE_KM_FACTOR, 2)
        yards = round(kilometers * KM_YARD_FACTOR, 2)
        return jsonify({ 'miles': miles, 'kilometers': kilometers, 'yards': yards })

    elif 'yards' in request.args:
        yards = float(request.args.get('yards'))
        miles = round(yards / MILE_YARD_FACTOR, 2)
        kilometers = round(yards / KM_YARD_FACTOR, 2)
        return jsonify({ 'miles': miles, 'kilometers': kilometers, 'yards': yards })

    else:
        return jsonify({ 'error': 'No input found' })


if __name__ == '__main__':
    app.run()


