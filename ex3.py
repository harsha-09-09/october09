from flask import Flask, redirect, url_for
# we need to create an app instance
app = Flask(__name__)

@app.route('/')
def greet():
    return('https://www.amazon.in/')

@app.route('/go_amazon')
def go_amazon():
    return(redirect("https://www.amazon.in/"))

@app.route('/third_party')
def third_party():
    return(redirect("url for https://www.amazon.in/"))

if __name__=="__main__":
    app.run(debug = True)