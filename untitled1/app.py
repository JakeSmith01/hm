from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return 'Hello {}'.format(name)


@app.route('/f/<temp>')
def display_converted_celsius(temp):
    temp = float(temp)
    converted_temp = temp * (9/5) + 32
    return '{} fahrenheit converts to {} celsius'.format(temp, converted_temp)


if __name__ == '__main__':
    app.run()
