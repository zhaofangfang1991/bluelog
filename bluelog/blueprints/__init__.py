# 这个包实际就是从view.py演变来的；
'''
蓝本对象和程序对象有很大不同
在实例化Blueprint类时，除了传入构造函数的第一个参数是蓝本名称之外，其他都与程序对象相同
'''

from flask import Flask, Blueprint
blog = Blueprint('blog', __name__)

