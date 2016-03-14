from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True

@app.route("/")
def vis():
    return render_template('visual.html')
    
@app.route('/route', methods=['POST'])
def route():
    return "Data"
    
if __name__ == "__main__":
    app.run()