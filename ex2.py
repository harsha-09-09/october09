from flask import Flask
app = Flask(__name__) # instance

@app.route('/')
def greet():
    return('Welcome')

@app.route('/greet1')
def greet1():
    return('Good AAfternoon')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = '8000',debug = True)