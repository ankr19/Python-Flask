from crypt import methods
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/product/<string:name>/', methods=['GET','POST'])
def product(name):
    
    return render_template('product.html')

if __name__ == "__main__":
    app.run(debug=True)