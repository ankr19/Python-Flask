from flask import Flask, request, render_template

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
        return post(name)
    return render_template('post.html')

app.route('/post/<string:name>')
def post(name):
    return render_template('name.html', name=name)

@app.route('/postitem')
def postitem():
    return render_template('mainpost.html')

if __name__=="__main__":
    app.run(debug=True)