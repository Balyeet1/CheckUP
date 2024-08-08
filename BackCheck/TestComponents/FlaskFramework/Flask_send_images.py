from flask import Flask, send_file
from flask_cors import CORS
import os.path

app = Flask(__name__)
CORS(app)


@app.route('/get-image/<path:source>')
def get_image(source):
    print(source)
    # Download image from Supabase

    image_path = os.path.join('images', 'Screenshot 2023-03-03 153528.png')
    # Send the image to the frontend
    return send_file(image_path, mimetype='image/jpg')


if __name__ == '__main__':
    app.run(debug=True)
