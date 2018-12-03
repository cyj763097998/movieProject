#coding:utf8
from . import admin
from flask import render_template,url_for,redirect
@admin.route("/")
@admin.route("/index/")
def index():
    return render_template("admin/index.html")

@admin.route("/login/")
def login():
    return render_template("admin/login.html")

@admin.route("/logout/")
def logout():
    return redirect(url_for('admin.login'))

@admin.route("/pwd/")
def pwd():
    return render_template("admin/pwd.html")