# -*- coding: utf-8 -*-
# __author__ = "shaycormac"
# Email: 2814913226@qq.com
# Date: 2018/11/13
import sys

menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '广东': {
        '江门': {
            "蓬江区": {
                '东湖公园': {}
            }
        },
        '深圳': {
            '福田区': {
                '华强北': {}
            }
        },
        '珠海': {
            '港珠澳大桥': {}
        },
    },
}
# 控制停留在第一层
while True:
    print('=' * 10 + '省份及直辖市' + '=' * 10)
    for key in menu.keys():  # 打印第一层key(北京、上海、广东)
        print(key)
    choice = input("请输入想查看的地域('q'or'Q'退出)：").strip()
    if choice in menu.keys():
        # 控制停留在第二层
        while True:
            print('=' * 20)
            print("%s下面的市(区)有：" % choice)
            for key in menu[choice].keys():  # 打印第二层key(海淀...)
                print(key)
            choice1 = input("请输入想查看的区域(输入‘q’or'Q'退出；输入‘b’or‘B’返回上级)：").strip()
            if choice1 in menu[choice].keys():
                # 控制停留在第三层
                while True:
                    print('=' * 20)
                    print("%s下面的区域有：" % choice1)
                    for key in menu[choice][choice1].keys():  # 打印第三层key(五道口...)
                        print(key)
                    choice2 = input("请输入想查看的街道(输入‘q’or'Q'退出；输入‘b’or‘B’返回上级)：").strip()
                    if choice2 in menu[choice][choice1].keys():
                        # 控制停留在第四层
                        while True:
                            print('=' * 20)
                            print("%s下面的企业有：" % choice2)
                            for key in menu[choice][choice1][choice2].keys():  # 打印第四层key(sohu...)
                                print(key)
                            choice3 = input("输入‘q’or'Q'退出；输入‘b’or‘B’返回上级：").strip()  # 随时退出
                            if choice3 == 'q' or choice3 == 'Q':
                                sys.exit(0)
                            elif choice3 == 'b' or choice3 == 'B':  # 返回上层
                                break
                            else:
                                print("无效的输入...")
                    elif choice2 == 'b' or choice2 == 'B':  # 返回上层
                        break
                    elif choice2 == 'q' or choice2 == 'Q':  # 随时退出
                        sys.exit(0)
                    else:
                        print("无效的输入...")
            elif choice1 == 'b' or choice1 == 'B':  # 返回上层
                break
            elif choice1 == 'q' or choice1 == 'Q':  # 随时退出
                sys.exit(0)
            else:
                print("无效的输入...")
    elif choice == 'q' or choice == 'Q':  # 随时退出
        sys.exit(0)
    else:
        print("无效地址...")
