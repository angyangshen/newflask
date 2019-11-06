from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    first_name = "Adrian"
    signed_in = True
    return render_template('index.html', first_name=first_name, signed_in = signed_in)

@app.route('/users/<username>')
def profile(username):
    return render_template("profile_page.html", username=username)

@app.route('/hello')
def hello():
    return "hello again"

@app.route('/contact')
def contact():
    return render_template('contact.html')
    
if __name__ == "__main__":
    app.run()
