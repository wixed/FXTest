# encoding: utf-8
"""
@author: lileilei
@file: models.py
@time: 2017/7/13 16:43
"""
from app import  db
import datetime
from werkzeug.security import check_password_hash,generate_password_hash
class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer(),primary_key=True,autoincrement=True)
    username=db.Column(db.String(63),unique=True)
    password=db.Column(db.String(252))
    user_email=db.Column(db.String(64),unique=True)
    status=db.Column(db.Integer(),default=0)
    level=db.Column(db.Integer(),default=0)
    phone = db.relationship('TestResult', backref='users', lazy='dynamic')
    project=db.relationship('Project',backref='users', lazy='dynamic')
    model = db.relationship('Model', backref='users', lazy='dynamic')
    def __repr__(self):
        return  self.username
    def set_password(self,password):
        self.password=generate_password_hash(password)
    def check_password(self,password):
        return  check_password_hash(self.password,password)
class Interface(db.Model):
    __tablename__='interfaces'
    id=db.Column(db.Integer(),primary_key=True,autoincrement=True)
    model_id=db.Column(db.Integer(),db.ForeignKey('models.id'))
    projects_id=db.Column(db.Integer(),db.ForeignKey('projects.id'))
    Interface_name=db.Column(db.String(252))
    Interface_url=db.Column(db.String(252))
    Interface_meth= db.Column(db.String(252),default='GET')
    Interface_par=db.Column(db.String(252))
    Interface_back=db.Column(db.String(252))
    Interface_user_id=db.Column(db.Integer(),db.ForeignKey('users.id'))
    def __repr__(self):
        return  self.Interface_name
class InterfaceTest(db.Model):
    __tablename__='interfacetests'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    model_id=db.Column(db.Integer(),db.ForeignKey('models.id'))
    projects_id=db.Column(db.Integer(),db.ForeignKey('projects.id'))
    Interface_name= db.Column(db.String(252))
    Interface_url = db.Column(db.String(252))
    Interface_meth = db.Column(db.String(252))
    Interface_pase = db.Column(db.String(252))
    Interface_assert=db.Column(db.String(252))
    Interface_user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    def __repr__(self):
        return  self.yongli_name
class TestResult(db.Model):
    __tablename__='tstresults'
    id=db.Column(db.Integer(),primary_key=True,autoincrement=True)
    Test_user_id=db.Column(db.Integer(),db.ForeignKey('users.id'))
    test_num=db.Column(db.Integer())
    pass_num=db.Column(db.Integer())
    fail_num = db.Column(db.Integer())
    skip_num=db.Column(db.Integer())
    test_time=db.Column(db.DateTime(),default=datetime.datetime.now())
    hour_time=db.Column(db.Integer())
    test_rep=db.Column(db.String(252))
    test_log=db.Column(db.String(252))
    def __repr__(self):
        return  self.id
class Project(db.Model):#项目
    __tablename__='projects'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    project_user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    project_name=db.Column(db.String(252))
    status=db.Column(db.Integer(),default=0)
    Interfacetest = db.relationship('InterfaceTest', backref='projects', lazy='dynamic')
    Interface = db.relationship('Interface', backref='projects', lazy='dynamic')
    def __repr__(self):
        return  self.project_name
class Model(db.Model):#模块
    __tablename__ ='models'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    model_name = db.Column(db.String(256))
    model_user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    status = db.Column(db.Integer(),default=0)
    Interfacetest = db.relationship('InterfaceTest', backref='models', lazy='dynamic')
    Interface = db.relationship('Interface', backref='models', lazy='dynamic')
    def __repr__(self):
        return  self.model_name
