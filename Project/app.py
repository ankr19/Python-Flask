from flask import Flask, request, render_template
from sqlalchemy import false, true

app = Flask(__name__)

post = [
    {
        "author":"Reema Thejha",
        "title": "First Blog",
        "content": "First Post contest",
        "date_posted":"Aprils 29th, 2022"
    },
    {
        "author":"Reema Thejha",
        "title": "First Blog",
        "content": "First Post contest",
        "date_posted":"Aprils 29th, 2022"
    },
    {
        "author":"Reema Thejha",
        "title": "First Blog",
        "content": "First Post contest",
        "date_posted":"Aprils 29th, 2022"
    },
    {
        "author":"Reema Thejha",
        "title": "First Blog",
        "content": "First Post contest",
        "date_posted":"Aprils 29th, 2022"
    },
    {
        "author":"Reema Thejha",
        "title": "First Blog",
        "content": "First Post contest",
        "date_posted":"Aprils 29th, 2022"
    },
    {
        "author":"Reema Thejha",
        "title": "First Blog",
        "content": "First Post contest",
        "date_posted":"Aprils 29th, 2022"
    },
]

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method=="POST":
        name = request.form["name"]
        password=request.form['password']
        if validate(name,password):
            return post(name)
        return render_template('base.html')
    return render_template('base.html') 


@app.route('/post')
def post():
    return render_template('post.html');



@app.route('/postitem')
def postitem():
    return render_template('mainpost.html')

def validate(name, password):
    if name=="Anand" and password=="password":
        return true
    return false

if __name__=="__main__":
    app.run(debug=True)