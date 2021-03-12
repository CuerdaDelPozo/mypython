from app import app
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/mult')
def mult():
    data = request.args.get('data', None)
    _list = list(map(float, data.split(',')))

    total = pum(_list)
    return 'Result = %f' % total

@app.route('/add')
def add():
    data = request.args.get('data', None)
    _list = list(map(int, data.split(',')))
    
    total = sum(_list)
    return 'Result= ' + str(total)

@app.route('/test')
def test():
    return 'This is a test'

def sum(arg):
    total = 0
    try:
        for val in arg:
            total += val
    except Exception:
        return "Error occured!", 500
    return total

def pum(arg):
    total = 1.0
    try:
        for val in arg:
            print(val)
            total = total * val
            print(total)
    except Exception:
        return "Error occured!", 500
    return total
