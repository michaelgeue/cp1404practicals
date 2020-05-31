from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! :)'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return 'Hello {}'.format(name)


def convert_celsius_to_fahrenheit(degrees):
    return degrees * 9.0 / 5 + 32


@app.route('/f')
@app.route("/f/<temperature>")
def celsius_to_fahrenheit(temperature=0):

    return '{} degrees celsius is {} degrees fahrenheit.'.\
        format(temperature, convert_celsius_to_fahrenheit(float(temperature)))


if __name__ == '__main__':
    app.run()
