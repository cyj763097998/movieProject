# coding:utf8
from . import admin
from flask import render_template, url_for, redirect,flash,session,request
from app.admin.forms import LoginForm,TagForm,MovieForm
from app.models import Admin,Tag,Movie
from functools import wraps
from app import db

def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if "admin" not in session:
            return redirect(url_for("admin.login",next=request.url))
        return f(*args,**kwargs)
    return decorated_function

@admin.route("/")
@admin.route("/index/")
@admin_login_req
def index():
    return render_template("admin/index.html")


# 登录
@admin.route("/login/",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data["account"]).first()
        if not admin.check_pwd(data["pwd"]):
            flash("密码错误！")
            return redirect(url_for("admin.login"))
        session["admin"] = data["account"]
        return redirect(request.args.get("next") or url_for("admin.index"))
    return render_template("admin/login.html", form=form)

#退出登录
@admin.route("/logout/")
@admin_login_req
def logout():
    session.pop("admin",None)
    return redirect(url_for('admin.login'))


@admin.route("/pwd/")
@admin_login_req
def pwd():
    return render_template("admin/pwd.html")

#添加标签
@admin.route("/tag/add/",methods=["GET","POST"])
@admin_login_req
def tag_add():
    form = TagForm()
    if form.validate_on_submit():
        data = form.data
        tag_num=Tag.query.filter_by(name=data["tag_name"]).count()
        if tag_num == 1:
            flash("标签名称已经存在！","err")
            return redirect(url_for("admin.tag_add"))
        tag = Tag(
            name=data["tag_name"]
        )
        db.session.add(tag)
        db.session.commit()
        flash("添加标签成功！","ok")
        return redirect(url_for("admin.tag_add"))
    return render_template("admin/tag_add.html",form=form)

#标签列表
@admin.route("/tag/list/<int:page>/",methods=["get"])
@admin_login_req
def tag_list(page=None):
    if page is None:
        page=1
    page_data = Tag.query.order_by(
        Tag.addtime.desc()
    ).paginate(page=page,per_page=10)

    return render_template("admin/tag_list.html",page_data=page_data)

#编辑标签
@admin.route("/tag/edit/<int:id>/",methods=["GET","POST"])
@admin_login_req
def tag_edit(id=None):
    form = TagForm()
    tag = Tag.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        tag_num=Tag.query.filter_by(name=data["tag_name"]).count()
        if tag.name != data["tag_name"] and tag_num == 1:
            flash("标签名称已经存在！","err")
            return redirect(url_for("admin.tag_edit",id=id))
        tag.name = data["tag_name"]
        db.session.add(tag)
        db.session.commit()
        flash("修改标签成功！","ok")
        return redirect(url_for("admin.tag_edit",id=id))
    return render_template("admin/tag_edit.html",form=form,tag=tag)

#删除标签
@admin.route("/tag/del/<int:id>/",methods=["get"])
@admin_login_req
def tag_del(id=None):
    tag=Tag.query.filter_by(id=id).first_or_404()
    db.session.delete(tag)
    db.session.commit()
    flash("删除标签成功！","ok")
    return redirect(url_for("admin.tag_list",page=1))

#添加电影
@admin.route("/movie/add/",methods=["GET","POST"])
@admin_login_req
def movie_add():
    form = MovieForm()
    if form.validate_on_submit():
        data = form.data
        movie = Movie(
            title = data["title"],
            url = url,
            info = data["info"],
            logo = logo,
            star = data["star"],
            playnum = 0,
            commentnum = 0,
            tag_id = data["tag_id"],
            area = data["area"],
            lenth = data["lenth"],
            release_time = data["release_time"]
        )
        db.session.add(movie)
        db.session.commit()
        flash("添加电影成功！","ok")
        return redirect(url_for("admin.movie_add"))
    return render_template("admin/movie_add.html",form=form)


@admin.route("/movie/list/")
@admin_login_req
def movie_list():
    return render_template("admin/movie_list.html")


@admin.route("/preview/add/")
@admin_login_req
def preview_add():
    return render_template("admin/preview_add.html")


@admin.route("/preview/list/")
@admin_login_req
def preview_list():
    return render_template("admin/preview_list.html")


@admin.route("/user/list/")
@admin_login_req
def user_list():
    return render_template("admin/user_list.html")


@admin.route("/user/view/")
@admin_login_req
def user_view():
    return render_template("admin/user_view.html")


@admin.route("/comment/list/")
@admin_login_req
def comment_list():
    return render_template("admin/comment_list.html")


@admin.route("/moviecol/list/")
@admin_login_req
def moviecol_list():
    return render_template("admin/moviecol_list.html")


@admin.route("/oplog/list/")
@admin_login_req
def oplog_list():
    return render_template("admin/oplog_list.html")


@admin.route("/adminloginlog/list/")
@admin_login_req
def adminloginlog_list():
    return render_template("admin/adminloginlog_list.html")


@admin.route("/userloginlog/list/")
@admin_login_req
def userloginlog_list():
    return render_template("admin/userloginlog_list.html")


@admin.route("/auth/add/")
@admin_login_req
def auth_add():
    return render_template("admin/auth_add.html")


@admin.route("/auth/list/")
@admin_login_req
def auth_list():
    return render_template("admin/auth_list.html")


@admin.route("/role/add/")
@admin_login_req
def role_add():
    return render_template("admin/role_add.html")


@admin.route("/role/list/")
@admin_login_req
def role_list():
    return render_template("admin/role_list.html")


@admin.route("/admin/add/")
@admin_login_req
def admin_add():
    return render_template("admin/admin_add.html")


@admin.route("/admin/list/")
@admin_login_req
def admin_list():
    return render_template("admin/admin_list.html")
