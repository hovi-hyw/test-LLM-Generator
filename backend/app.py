from flask import Flask
from flask_cors import CORS
from api import chat_bp  # 导入蓝图

app = Flask(__name__)
CORS(app)  # 允许跨域请求

app.register_blueprint(chat_bp, url_prefix='/api/chat')  # 注册蓝图

if __name__ == '__main__':
    app.run(debug=True, port=5000)