# created by shaycormac
users = [['shay', '666'], ['alex', '233']]
login_state = False
# 设置用户登陆状态为False的标志
count = 0
username_count = []   # 用来计算用户登陆次数
user_name = []
lock_users = []
f = open('F:/路飞学城/lock_file.txt', 'a+', encoding='utf-8')
# 读取文件里已被锁定用户的信息
for i in f:
    lock_users.append(i.strip())
while count < 3:
    username = input('用户名:').strip()
    password = input('密码:').strip()
    username_count.append(username)
    # 将用户输入的用户名添加到计数列表
    if username == lock_users:
        exit('用户已被锁定')
    for user_item in users:
        if username == user_item[0] and password == user_item[1]:
            print("欢迎%s"'登陆成功' % username)
            login_state = True  # 登陆成功,login_state改为True
            break        # 跳出for循环
    else:
        print('请输入正确的的用户名或密码')
        # for 循环正常执行完（登录成功会被break，不会执行else，反之执行），再执行else
    if login_state:
        break            # 用来跳出while循环
    count += 1
else:
    print('错误次数过多')  # 登录成功while被break，不会执行else，反之执行
    for lock in username_count:
        user_name.append(lock)
        if user_name.count(lock) >= 3:  # 列表里面出现次数超过3次的用户名
            lock_write = open('lock_file.txt', 'a+', encoding='utf-8')
            lock_write.write(lock + '\n')
            lock_write.close()