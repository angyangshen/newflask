from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Sexy"
    return render_template('index.html', name=name)

@app.route('/hello')
def hello():
    return "hello again"
if __name__ == "__main__":
    app.run(debug=True)

