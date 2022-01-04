"""cách 1"""

list_a = []
def expr(i):
    return i*2
def func(i):
   #  toan tu 3 ngoi
   # return True  if i % 2 ==0  else  False
   #normal
   if i%2==0:
       return True
   else:
       return False
# duyet for neu if dung thì tien hanh expr con sai thi thoi
list_a = [expr(i) for i in range(5) if func(i)]
#duyet for nếu if là đúng thì add i*2 còn ko thì add False
list_a = [i * 2 if i % 2 == 0 else  False for i in range(5)]
print(list_a)
# print(list_a)
"""cach normal"""
# list_a = []

# def expr(i):
#      return i
# for i in range(5):
#     if i % 2 ==0 :
#         list_a.append(expr(i))
# print(list_a)
"""cach 3 """
# def expr(i):
#     return i*2
# def func(i):
#     if i % 2 ==0 :
#         return True
# list_a = []
# for i in range(5):
#     if func(i):
#         # list_a.append(expr(i))
#         print(expr(i))
#
# print(list_a)
""""""

