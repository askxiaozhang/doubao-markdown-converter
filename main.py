from flask import Flask, send_from_directory
from endpoints import api_bp
import os


app = Flask(__name__)


app.register_blueprint(api_bp)


@app.get("/")
def read_root():
    return send_from_directory(
        os.path.join(os.path.dirname(__file__), 'public'),
        'index.html'
    )
