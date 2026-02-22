from flask import Flask, render_template

# 不需要再算 os.path 了，默认就在当前目录找
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.get("/health")
def health():
    return {"status": "ok"}

