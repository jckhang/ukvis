from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
app.debug = True


@app.route("/")
def vis():
    return render_template('visual.html')


@app.route('/route', methods=['POST'])
def route():
    from_station = request.form['start']
    to_station = request.form['end']
    from_station = "a"
    to_station = "b"
    # Smart routing goes here!
    path = ["a", "b", "c"]
    return render_template('visual.html',
                           from_station=from_station,
                           path=path,
                           to_station=to_station)

if __name__ == "__main__":
    app.run()
