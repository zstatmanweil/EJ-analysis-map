from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")


@app.route('/map')
def map():
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render_template("map.html", mapbox_access_token=mapbox_access_token)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
