from flask import Flask, send_from_directory
from endpoints import api_bp
import os


app = Flask(__name__, static_folder='public', static_url_path='')


app.register_blueprint(api_bp)


@app.get("/")
def read_root():
    # 因为现在 index.py 在 api/ 目录下，而 public/ 在根目录下
    # 所以需要去上一级目录找
    api_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(api_dir)
    return send_from_directory(os.path.join(root_dir, 'public'), 'index.html')




@app.get("/health")
def health():
    return {"status": "ok"}

