from flask import Flask, request
from flask_sock import Sock
from fib import fib 
import time

app = Flask(__name__)
sock = Sock(app)


@app.route('/fibionacci')
def index():
    number = int(request.args.get("number"))
    out = 0
    
    for i in fib(number):
        out = i
    
    return str(out)


@sock.route('/streaming/fibionacci')
def echo(sock):
    for i in fib(-1):
        sock.send(i)
        time.sleep(2)
