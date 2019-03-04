#coding:utf8
from datetime import datetime
from app import db


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
    addtime = db.Column(db.DateTime, index=True,default=datetime.now)
    uuid = db.Column(db.String(255), unique=True,nullable=False)
    userlogs = db.relationship('Userlog',backref='user') #会员日志外键关系关联
    comments = db.relationship('Comment', backref='user')  # 评论外键关系关联
    moviecols = db.relationship('Moviecol', backref='user')  # 收藏外键关系关联
    def __repr__(self):
        return "<User %r>" % self.name

#会员日志
class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))    #外键
    ip = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    def __repr__(self):
        return "<Userlog %r>" % self.id

#标签
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
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
    comments = db.relationship('Comment', backref='movie')  # 评论外键关系关联
    moviecols = db.relationship('Moviecol', backref='movie')  # 收藏外键关系关联
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Movie %r>" % self.title

#上映预告
class Preview(db.Model):
    __tablename__ = "preview"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    log = db.Column(db.String(255), unique=True, nullable=False)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    def __repr__(self):
        return "<Preview %r>" % self.title

#评论
class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    def __repr__(self):
        return "<Comment %r>" % self.id
#收藏
class Moviecol(db.Model):
    __tablename__ = "moviecol"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    def __repr__(self):
        return "<Moviecol %r>" % self.id

#权限
class Auth(db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    url = db.Column(db.String(255), unique=True, nullable=False)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    def __repr__(self):
        return "<Auth %r>" % self.name

#角色
class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    auths = db.Column(db.String(600))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    def __repr__(self):
        return "<Role %r>" % self.name

#管理员
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100),unique=True,nullable=False)
    pwd = db.Column(db.String(100), nullable=False)
    is_super = db.Column(db.SmallInteger)  #是否是超级管理员  0代表超级管理员
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))  #所属角色
    adminlogs = db.relationship("Adminlog", backref="admin")  # 管理员登录日志外键关系关联
    oplogs = db.relationship("Oplog", backref="admin")  # 操作日志外键关系关联
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    def __repr__(self):
        return "<Admin %r>" % self.name
    def check_pwd(self,pwd):
        """ 验证密码一致性，正确返回true 错误返回false"""
        from werkzeug.security import check_password_hash
        print pwd,self.pwd
        return check_password_hash(self.pwd,pwd)
#管理员登录日志
class Adminlog(db.Model):
    __tablename__ = "adminlog"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))    #外键
    ip = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    def __repr__(self):
        return "<Adminlog %r>" % self.id
#后台操作日志
class Oplog(db.Model):
    __tablename__ = "oplog"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))    #外键
    ip = db.Column(db.String(100))
    reason = db.Column(db.String(600))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    def __repr__(self):
        return "<Oplog %r>" % self.id

if __name__ ==  "__main__":
    #db.create_all()
    '''
        role = Role(
        name=u"超级管理员",
        auths=""
        )
        db.session.add(role)
        db.session.commit()
    '''
    '''
    from werkzeug.security import generate_password_hash
    admin = Admin(
        name="imoocmovie",
        pwd=generate_password_hash("imoocpasswd"),
        is_super=0,
        role_id=1
    )
    db.session.add(admin)
    db.session.commit()
    '''