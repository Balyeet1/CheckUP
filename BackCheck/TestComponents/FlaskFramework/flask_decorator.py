from flask import Flask, Blueprint

app = Flask(__name__)
my_blueprint = Blueprint('my_blueprint', __name__)


# This file demonstrates how to use flask decorator
# Note that to use the same decorator function in multiple endpoints
# you got to set "endpoint" in the Routes, or else, it raises an error

# Custom decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorator executed before route")
        return func(*args, **kwargs)

    return wrapper


# Applying the decorator to each route within the blueprint
@my_blueprint.route('/route1', endpoint='route1')
@my_decorator
def route1():
    return "Hello from Route 1"


@my_blueprint.route('/route2', endpoint='route2')
@my_decorator
def route2():
    return "Hello from Route 2"


# Register the blueprint with the Flask AppFolders
app.register_blueprint(my_blueprint, url_prefix='/my_blueprint')

if __name__ == '__main__':
    app.run(debug=True)
