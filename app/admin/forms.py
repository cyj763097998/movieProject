# coding:utf8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,FileField,TextAreaField,SelectField
from wtforms.validators import DataRequired, ValidationError
from app.models import Admin,Tag

tags = Tag.query.all()
print tags
print "test"
class LoginForm(FlaskForm):
    """管理员登录表单"""
    account = StringField(
        label="帐号",
        validators=[
            DataRequired("请输入帐号！")
        ],
        description="帐号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！",
            "required": False
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！",
            "required": False
        }
    )
    submit = SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )

    def validate_account(self, field):
        account = field.data
        res = Admin.query.filter_by(name=account).count()
        if res == 0:
            raise ValidationError("账号不存在！")


class TagForm(FlaskForm):
    """标签"""
    tag_name = StringField(
        label="标签名称",
        validators=[
            DataRequired("请输入标签名称！")
        ],
        description="标签名称",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入标签名称！",
            "required": False
        }
    )
    submit = SubmitField(
        "添加",
        render_kw={
            "class": "btn btn-primary"
        }
    )
    submit_edit = SubmitField(
        "编辑",
        render_kw={
            "class": "btn btn-primary"
        }
    )

class MovieForm(FlaskForm):
    """电影"""
    title = StringField(
        label="片名",
        validators = [
            DataRequired("请输入片名！")
        ],
        description = "片名",
        render_kw = {
            "class": "form-control",
            "placeholder": "请输入片名！",
            "required": False
        }
    )
    url = FileField(
        label="片名",
        validators=[
            DataRequired("请输入片名！")
        ],
        description="片名",
    )
    info = TextAreaField(
        label="介绍",
        validators=[
            DataRequired("请输入介绍！")
        ],
        description="介绍",
        render_kw={
            "class": "form-control",
            "rows":10,
            "required": False
        }
    )
    logo = FileField(
        label = "封面",
        validators = [
             DataRequired("请输入封面！")
        ],
        description = "封面",
    )
    star = SelectField(
        label="星级",
        validators=[
            DataRequired("请输入星级！")
        ],
        coerce=int,
        choices=[(1,"1星"),(2,"2星"),(3,"3星"),(4,"4星"),(5,"5星")],
        description="星级",
        render_kw={
            "class": "form-control",
            "required": False
        }
    )
    tag_id = SelectField(
        label="标签",
        validators=[
            DataRequired("请输入标签！")
        ],
        coerce=int,
        choices=[(v.id, v.name) for v in tags],
        description="标签",
        render_kw={
            "class": "form-control",
            "required": False
        }
    )
    area = StringField(
        label="地区",
        validators = [
            DataRequired("请输入地区！")
        ],
        description = "地区",
        render_kw = {
            "class": "form-control",
            "placeholder": "请输入地区！",
            "required": False
        }
    )
    length = StringField(
        label="片长",
        validators = [
            DataRequired("请输入片长！")
        ],
        description = "片长",
        render_kw = {
            "class": "form-control",
            "placeholder": "请输入片长！",
            "required": False
        }
    )
    release_time = StringField(
        label="上映时间",
        validators = [
            DataRequired("请输入上映时间！")
        ],
        description = "上映时间",
        render_kw = {
            "class": "form-control",
            "placeholder": "请输入上映时间！",
            "id": "input_release_time",
            "required": False
        }
    )
    submit = SubmitField(
        "添加",
        render_kw={
            "class": "btn btn-primary"
        }
    )