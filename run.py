# app/__init__.py
from flask import Flask
from config import Config, db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0',port=port)