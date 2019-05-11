#!/urs/local/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/map')
def map():
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render_template("map.html", mapbox_access_token=mapbox_access_token)

@app.route('/results')
def results():
    return render_template("results.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
