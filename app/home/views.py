#coding:utf8
from . import home

@home.route("/")
def index():
    return "this is home"