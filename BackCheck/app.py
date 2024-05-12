from flask import Flask

from AppFolders.Configs import setup_app

# Create a Flask Object
app = Flask(__name__)

setup_app(app)

# If this file is the entrance, run the AppFolders at the port 6699
if __name__ == '__main__':
    app.run(port=6699)
