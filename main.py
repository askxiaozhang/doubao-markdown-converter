from flask import Flask, send_from_directory
from endpoints import api_bp
import os


app = Flask(__name__, static_folder='public', static_url_path='')


app.register_blueprint(api_bp)


@app.get("/")
def read_root():
    # 强制使用绝对路径查找文件
    base_path = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(os.path.join(base_path, 'public'), 'index.html')



@app.get("/health")
def health():
    return {"status": "ok"}

