from flask import Flask
from flask import render_template


app = Flask("trialVis")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

