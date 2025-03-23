import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.environ.get('FLASK_KEY')

    UPLOAD_FOLDER = os.path.join(basedir, 'app', 'data', 'uploads')
    MAX_CONTENT_LENGTH = 1 * 1024 * 1024

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app', 'data', 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Gemini API 配置
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
    GEMINI_MODEL = 'gemini-1.5-flash'  # 选择合适的模型