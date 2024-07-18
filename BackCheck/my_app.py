from flask import Flask

from AppFolders.Configs import setup_app

# Create a Flask Object
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Cloud Run!'


app = setup_app(app)

# If this file is the entrance, run the AppFolders at the port 6699
if __name__ == '__main__':
    app.run(port=8080)
