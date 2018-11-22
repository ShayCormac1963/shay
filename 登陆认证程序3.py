# -*- coding: utf-8 -*-
# __author__ = "shaycormac"
# Email: 2814913226@qq.com
# Date: 2018/11/7
# import os
import sys

""" ###为什么输出结果有些是/,有些是\
print("sys.path[0] = ", sys.path[0])
print("sys.argv[0] = ", sys.argv[0])
print("__file__ = ", __file__)
print("os.path.abspath(__file__) = ", os.path.abspath(__file__))
print("os.path.realpath(__file__) = ", os.path.realpath(__file__))
print("os.path.dirname(os.path.realpath(__file__)) = ", os.path.dirname(os.path.realpath(__file__)))
print("os.path.split(os.path.realpath(__file__)) = ", os.path.split(os.path.realpath(__file__)))
print("os.path.split(os.path.realpath(__file__))[0] = ", os.path.split(os.path.realpath(__file__))[0])
print("os.getcwd() = ", os.getcwd())
"""
global username  # 应在文件最开始就定义全局变量
with open(sys.path[0] + "/用户数据", 'r') as f:  # /用户数据or\\用户数据?
    accounts = eval(f.read())  # 读取文件字符串转为字典
count = 0
is_same_user = True
previous_input = None
while count < 3:
    username = input("用户名:").strip()  # 让用户输入用户名密码
    password = input("密码:").strip()
    if previous_input is None:
        previous_input = username
    if username != previous_input:  # 若这一次用户与上一次输入不一致
        is_same_user = False  # 标记为不同用户
    if username in accounts:
        if accounts[username][1] == 0:  # 判断用户是否锁定
            if password == accounts[username][0]:
                print("欢迎%s登陆成功" % username)  # 认证成功后显示欢迎信息
                break
            else:
                print("请输入正确的用户名和密码")
        else:
            print("该用户已被锁定,请联系管理员")
    else:
        print("用户不存在")
    count += 1
else:  # 输错三次后退出程序
    print("错误次数太多")
    if is_same_user is True:  # 3次输入一致,锁定用户
        accounts[username][1] = 1
        with open(sys.path[0] + "/用户数据", 'w') as f:
            f.write(str(accounts))
