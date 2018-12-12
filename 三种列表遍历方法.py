l = ["这", "是", "一个", "测试"]
for i in l:
    print(l.index(i), i)
for i in range(len(l)):
    print(i, l[i])
for index, item in enumerate(l):
    print(index, item)
