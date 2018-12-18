products = [['Iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]
shopping_cart = []
exit_flag = False
print("---------商品列表----------")
for i, v in enumerate(products):
    print('%s.' % i, v[0], ' ', v[1])
