from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def greet():
    return("Hello world")

@app.route('/add1')            # add1
def add1():
    a = 10
    b = 20
    return(f"the addition of 10 and 20 is {a+b}")

@app.route('/add2/<a>/<b>')       # /add2/10/20
def add2(a,b):
    return(f"the addition of a and b is {a+b}")

@app.route('/add3/<int:a>/<int:b>')   # /add3/10/20
def add3(a,b):
    return(f"the addition of a and b is {a+b}")

@app.route('/add4')                 # /add4?number1=10&number2=20
def add4():
    a = request.args.get("number1",default = 0,type = int)
    b = request.args.get("number2",default = 0,type = int)
    return(f"the addition of a and b is {a+b}")