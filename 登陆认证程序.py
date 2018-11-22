# author：shaycormac
#coding: utf-8

import os


# 创建文件存储用户名和密码，并放入两对用户名和密码
if not os.path.exists('shay.txt'):
    with open('shay.txt', 'a+') as fx:
        fx.write(str({'shay': '001', 'lily': '002'}))

# 创建文件存储用户名和密码输入的次数，初始为空
if not os.path.exists('shaylocktime.txt'):
    with open('shaylocktime.txt', 'a+'):
        pass


with open('shay.txt', 'r')as f:
    user = f.read()
    user = eval(user)    # 把文件中的字典格式的内容读出来，并且转化为字典（默认读进来是字符串）
with open('shaylocktime.txt', 'r')as f2:
    dic_locktime = f2.read()    # 读锁定次数的字典
    if len(dic_locktime) > 0:    # 初始为空，所以读出来的有值的时候才将其转化为字典
        dic_locktime = eval(dic_locktime)
    else:
        dic_locktime = {}    # 无值的时候初始化字典

ifcontinue = 1
while ifcontinue:
    name = input('请输入用户名：')
    name_exist = user.get(name)    # 根据输入的用户名找对应的密码
    if name_exist:
        error_num = dic_locktime.get(name)    # 找到之后读取锁定次数
        if error_num == 3:
            print('账户已被锁定！')
            exit()
        if error_num == None:
            error_num = 0
        while error_num < 3:    # 未锁定时输入密码
            psd = input('请输入密码：')
            if psd == user.get(name):
                dic_locktime[name] = error_num
                print('Welcome %s login ...' % name)
                ifcontinue = 0    # 成功登陆之后不让用户再输入用户名，锁定的时候再继续输入用户名
                break
            else:
                error_num += 1
                print('密码输入错误第%s次，输入错误超过三次后将被锁定！' % error_num)
        if error_num == 3:
            dic_locktime[name] = 3
    else:
        print('未找到此用户名！')
    with open('shaylocktime.txt', 'w+')as f__lock:
        f__lock.write(str(dic_locktime))
