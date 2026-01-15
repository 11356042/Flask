from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/") #route Fast API->GET
def home():
    return "QAQ"

@app.route("/page/<name>") #route Fast API->GET
def page(name):
    return render_template("index.html",name=name)

# @app.route("/hello/<name>",methods=['GET','POST'])
# def hello(name):
#     return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)