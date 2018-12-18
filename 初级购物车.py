products = [['Iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]
shopping_car = []
exit_flag = False
while not exit_flag:
    print("---------商品列表----------")
    for i, v in enumerate(products):
        print('%s.' % i, v[0], ' ', v[1])
    choice = input("请输入想买的商品编号:")
    if choice.isdigit():
        choice = int(choice)
        if 0 <= choice < len(products):
            shopping_car.append(products[choice])
            print("已添加商品 %s 进购物车" % (products[choice]))
        else:
            print("商品不存在")
    elif choice == 'q':
        exit_flag = True
        if len(shopping_car) > 0:
            print("-------你已购买以下商品-------")
            for i, v in enumerate(shopping_car):
                print('%s.' % i, v[0], ' ', v[1])
    else:
        print("输入有误,请输入商品的\33[31m数字\33[0m编号")
