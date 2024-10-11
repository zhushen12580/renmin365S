# config.py
import os
from flask_sqlalchemy import SQLAlchemy

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Zhushen%4001@120.79.81.153/renmin365'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# 初始化数据库
db = SQLAlchemy()