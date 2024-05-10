# 列表推导式（List Comprehension）和生成器表达式（Generator Expression）
zero=0
a = [i for i in range(10)]
b = (i for i in range(10))
c = [(i, j) for i in range(10) for j in range(5)]

# print(id(a[0]))
# print(id(zero))

# print(type(a))
# print(type(b))
# print(len(c))

# print(a[0])
# # print(b[0])

# 海象表达式 :=
# x = "ABC"
# codes = [last := ord(c) for c in x]
# print(codes)
# print(last)

# map filter
# m = map(lambda i: i**3, a)
# f = filter(lambda i: i % 2 == 0, a)
# print(type(m))
# print(m)
# print(list(m))
# print(list(f))

# 元组  %表示格式话字符串
# traveler_ids = [("USA", "31195855"), ("BRA", "CE342567"), ("ESP", "XDA205856")]
# for passport in sorted(traveler_ids):
#     print("%s %s" % passport)


# * 剩余元素
# def fun(a, b, c, d, *rest):
#     return a, b, c, d, rest

# print(fun(*[1, 2], 3, *range(4, 7)))

