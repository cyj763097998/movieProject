#coding:utf8
from flask import  Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_RRI"] = "mysql://root:123456@127.0.0.1:3306/db_movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

#会员
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100),unique=True,nullable=False)
    pwd = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100),unique=True, nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    info = db.Column(db.Text)
    face = db.Column(db.String(255), unique=True)
    addtime = db.Column(db.DateTime, index=True,default=datetime.utcnow)
    uuid = db.Column(db.String(255), unique=True,nullable=False)
    userlogs = relationship('Userlog',backref='user') #会员日志外键关系关联
    def __repr__(self):
        return "<User %r>" % self.name

#会员日志
class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))    #外键
    ip = db.Column(db.String(100)
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    def __repr__(self):
        return "<Userlog %r>" % self.id

#标签
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    movies = db.relationship("Movie",backref="tag")#电影外键关系关联
    def __repr__(self):
        return "<Tag %r>" % self.name

#电影
class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    url = db.Column(db.String(255), unique=True,nullable=False)
    info = db.Column(db.Text)
    logo = db.Column(db.String(255), unique=True, nullable=False)
    star = db.Column(db.SmallInteger)
    playnum = db.Column(db.BigInteger)
    commentnum = db.Column(db.BigInteger)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    area = db.Column(db.String(255))
    release_time = db.Column(db.Date)
    lenth = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    def __repr__(self):
        return "<Movie %r>" % self.title

#上映预告
class Preview(db.Model):
    __tablename__ = "preview"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    log = db.Column(db.String(255), unique=True, nullable=False)
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    def __repr__(self):
        return "<Preview %r>" % self.title

