# -*- coding: utf-8 -*-
# __author__ = "shaycormac"
# Email: 2814913226@qq.com
# Date: 2018/11/16
import sys

# 定义商品列表
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
    {"name": "IPhone XS Max", "price": 10666}
]
# 定义一个余额列表
balance = []
# 定义一个购物车列表
shopping_car = []
# 简单定义用户名密码
username = 'alex'
password = '123456'
# 简易的登录验证
i = 0
while i < 3:
    name = input("请输入用户名：").strip()
    passwd = input("请输入密码：").strip()
    if name == username and passwd == password:
        print('=' * 15 + '欢迎光临黑店' + '=' * 15)
        break
    else:
        print("用户名或者密码错误,还剩%d次登陆机会！" % (2 - i))
        i += 1
else:
    sys.exit("三次输入失败，退出...")
# 打开余额文件，查看是否有余额，是则不提示输入工资
with open('balance_file', 'r', encoding='utf-8') as balance_f:
    balance_list = balance_f.readlines()
if len(balance_list) == 0:  # 如若balance_file为空，提示输入工资并作为余额
    salary = int(input("请输入你的工资：").strip())
    balance.append(salary)
else:  # balance_file余额，则将余额添加到余额列表
    history_balance = int(balance_list[0].strip('\n'))
    balance.append(history_balance)
while True:
    # 打印商品列表
    print('=' * 10 + "本店有以下商品，欢迎采购" + '=' * 10)
    for g, good in enumerate(goods, 1):
        print("\033[1;31;0m%s.  %s  %s \033[0m" % (g, good["name"], good["price"]))
    # 获取用户输入
    action = input("请选择购买的商品编号(退出请按q;查询历史购买记录请按f)：").strip()
    # 商品购买
    if action.isdigit():  # 检测输入的字符串是否只由数字组成
        action = int(action)  # 若字符串只有数字组成，将其转换成int类型
        if 0 < action <= len(goods):  # 判断输入的商品编号是否在商品列表内
            if balance[0] >= goods[action - 1]["price"]:  # 判断余额是否充足
                shopping_car.append(goods[action - 1])  # 记录购物车
                history_data = goods[action - 1]["name"] + ':' + str(goods[action - 1]["price"]) + '\n'
                with open('history_file', 'a', encoding='utf-8') as h_f:  # 将选购商品信息写入history_file作为历史清单
                    h_f.write(history_data)
                balance[0] = balance[0] - goods[action - 1]["price"]  # 余额扣款
                print("\033[1;0m%s已购买成功！\033[0m" % (goods[action - 1]["name"]))
            else:
                print("\033[1;0m余额已不足...\033[0m")
        else:
            print("\033[1;0m此商品不存在，请根据商品列表购买！\033[0m")
    # 用户退出
    elif action == 'q' or action == 'Q':
        if len(shopping_car) > 0:
            print('=' * 15 + "您已购买了以下商品：")
        else:
            print("您没有购买商品..")
        for g, good in enumerate(shopping_car, 1):  # 遍历购物车，打印购买商品
            print("\033[1;35;0m%s.  %s  %s \033[0m" % (g, good["name"], good["price"]))
        print("\033[1;0m您的余额为：%d，欢迎下次光临！" % (balance[0]))  # 打印余额
        with open('balance_file', 'r+', encoding='utf-8') as b_f:  # 将余额覆盖到balance_file
            b_f.write(str(balance[0]) + '\n')
        sys.exit(0)
    # 查询历史消费记录
    elif action == 'f' or action == 'F':
        with open('history_file', 'r', encoding='utf-8') as h_f:
            h_list = h_f.readlines()  # 逐行读取history_file
        if len(h_list) == 0:
            print("没有历史购买记录！")
        else:
            print("\033[1;0m以下为历史购买记录：\033[0m")  # 遍历h_list,打印历史清单
            for i, h in enumerate(h_list, 1):
                (name, price) = h.strip('\n').split(":")
                print("\033[1;35;0m%s.  %s  %s\033[0m" % (i, name, price))
