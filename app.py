from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/hello', methods=["POST", "GET"])
def hello():
    # if request.method == 'GET':
    #     return "You made, a GET request", 200
    # elif request.method == "POST":
    #     return "You made a POST request", 201
    # else:
    #     return "You will never see this message."
    res = make_response()
    res.status_code = 201
    res.headers['content-type'] = 'applicaion/octet-stream'
    return res


@app.route('/greet/<name>')
def greet(name):
    return f"Hello,{name}"

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"


# handle url params
@app.route('/url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name= request.args.get('name')
        return f'{greeting}, {name}'
    else:
        return "Some URL params are missing"




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3500, debug=True)