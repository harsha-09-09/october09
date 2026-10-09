from flask import Flask
app = Flask(__name__) # instance

@app.route('/')
def greet():
    return('Welcome')

@app.route('/greet1')
def greet1():
    return('Good Morning')

if __name__ == "__main__":
    app.run(debug = True)