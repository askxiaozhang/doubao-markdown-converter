from flask import Flask, send_from_directory
from endpoints import api_bp
import os


app = Flask(__name__, static_folder='public', static_url_path='')


app.register_blueprint(api_bp)


@app.get("/")
def read_root():
    return app.send_static_file('index.html')


@app.get("/health")
def health():
    return {"status": "ok"}

