# def f(x):
#     d = 0
#     while x >= 1:
#         (x, d) = (x / 4, d + 1)
#     return d
#
#
# print(f(255))
#
#
# def h(n):
#     s = 0
#     for i in range(1, n):
#         if n % i == 0:
#             s = s + i
#     return s
#
#
# print(h(28) - h(27))
#
#
# def g(m, n):
#     res = 0
#     while m >= n:
#         (res, m) = (res + 1, m - n)
#     return res


# def g(m, n):
#     res = 0
#     while m >= n:
#         (res, m) = (res + 1, m - n)
#     return res
#
#
# i = 1
# while i < 47+1:
#     if g(47, i) == 5:
#         print(i)
#     i = i+1


# def mys(m):
#   if m == 0:
#     return(1)
#   else:
#     return(m*mys(m-1))
#
#
# print(mys(-5))
