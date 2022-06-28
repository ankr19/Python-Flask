from flask import Flask, render_template, request

app2 = Flask(__name__)

# @app2.route('/')
# def home():
#     name = 'Harshika'
#     return render_template('index2.html', name=name)



@app2.route('/', methods=['GET',"POST"])
def home2():
    if request.method=="POST":
        name = request.form["name"]
        return showname(name)
    return render_template("post.html")

@app2.route("/name/<string:name>")
def showname(name):
    return render_template('name.html',name=name)


if __name__== "__main__":
    app2.run(debug=True)