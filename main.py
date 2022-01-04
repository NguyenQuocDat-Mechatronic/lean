# print(1000000*70**30)
# # print("or')
# print('Brian\'s mother: He\'s not an angel. He\'s a very naughty boy!')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# def cal(a,b):
#     P1 = a+b
#     P2 = a-b
#     P3 = a*b
#     P4 = a/b
"""check lại sao đáp án giá đúng rồi mà vào báo sai  """
# def cal(a,b):
#     P1 = a+b
#     P2 = a-b
#     P3 = a*b
#     P4 = a/b
#     print("%i + %i ="%(a,b),P1)
#     print("%i - %i ="%(a,b),P2)
#     print("%i * %i ="%(a,b),P3)
#     print("%i / %i ="%(a,b),P4)
#
#     print("%i + %i = %i\n%i - %i = %i\n%i * %i = %i\n%i / %i = %r"%(a,b,P1,a,b,P2,a,b,P3,a,b,P4))
# cal(2468,1234)
#
# name = input('who?')
# xh = input("input hour:")
# xr = input("input hour rate:")
# xp = int(xh) *int(xr)
# print(xp)

# a = int(input())
# b = int(input())
# P1 = a+b
# P2 = a-b
# P3 = a*b
# P4 = a/b
# P5 = a%b
# print(a)
# print(b)
# print("%i + %i = %i\n%i - %i = %i\n%i * %i = %i\n%i / %i = %r\n%i + %i = %i"%(a,b,P1,a,b,P2,a,b,P3,a,b,P4,a,b,P5))
# a = int(input())
# b = int(input())
# P1 = a+b
# P2 = a-b
# P3 = a*b
# P4 = a/b
# P5 = a%b
# # ("%i + %i = %i\n%i - %i = %i\n%i * %i = %i\n%i / %i = %r\n%i "" %i = %i"%(a,b,P1,a,b,P2,a,b,P3,a,b,P4,a,b,P5))
# print("a + b = " + str(a + b))
# print("a - b = " + str(a - b))
# print("a * b = " + str(a * b))
# print("a / b = " + str(a / b))
# print("a % b = " + str(a % b))
# # print(21%7)
# a = int(input())
# Total = int(input())
# Total += a # Using += Operator
# print("The Value of the Total after using += Operator is:", Total)
# Total -= a # Using -= Operator
# print("The Value of the Total after using -= Operator is:", Total)
# Total *= a # Using *= Operator
# print("The Value of the Total after using *= Operator is:", Total)
# Total //= a # Using //= Operator
# print("The Value of the Total after using //= Operator is:", Total)
# Total **= a # Using **= Operator
# print("The Value of the Total after using **= Operator is:", Total)
# Total /= a # Using /= Operator
# print("The Value of the Total after using /= Operator is:", Total)
# Total %= a  # Using %= Operator
# print("The Value of the Total after using %= Operator is:", Total)
#
# x = "Heloo"
# y = "Dat"
# lst = x.split("e")
# print(lst)
# for i in lst:
#     if i == "H":
#         result_bool = True
#     else:
#         result_bool = False
# # print(result_bool)
# x = 50
# if x < 2 :
#     print('small')
# elif x<10:
#     print("medium")
#
# print("All done")

# print("Hi")
#
# print("""This
# is
# great""")
# print(num := int(input()))
# print("a">="ab")
# import PtQty5
# import math
#
# import PyQt5
#
# def addition(a,b):
#     return(a+b)
# c =addition(2,3)
# print(c)
# import  math
# from math import  sqrt,cos,radians
#
# a = 18
# b = 24
#
# def gcd(a,b):
#     i = 2
#     lst = []
#     while True:
#         if a%i ==0 and b%i ==0:
#             lst.append(i)
#         i +=1
#         if i > a or i >b:
#             break
# #     return max(lst)
# # print(gcd(a,b))
# try :
#     variable = 10
#     print(variable+"hello")
#     print(variable/0)
# # except ZeroDivisionError:
# #     print("dvided by zero")
# except(ValueError,TypeError,ZeroDivisionError):
#     print("Error occurred")
# try :
#     print(1)
#     print(10/0)
# except ZeroDivisionError:
#     print(unknow_var)
# finally:
#     print("This is executed last")
# try :
#     print(1/0)
# except ZeroDivisionError:
#     print("error occur")
# try:
#     num = 5/0
# except:
#     print("an error occured")
#     # raise
# # name = '123'
# raise  print("2"+"error")
# # raise NameError("Invalid name !")

# try:
#  x = int(input('Nhập một số trong khoảng 1-10: '))
#  if x<1 or x>10:
#     # raise Exception
#     print ('Bạn vừa nhập một số hợp lệ :D')
# except:
#  print ('Số bạn vừa nhập nằm ngoài khoảng cho phép mất rồi!')

#
# class GenderException(Exception):
#      def __init__(self, msg):
#          super().__init__(msg)
#
#          # Ngoại lệ ngôn ngữ.
#
#
# class LanguageException(Exception):
#      def __init__(self, msg):
#          super().__init__(msg)
#
#
# class PersonException(Exception):
#      def __init__(self, msg):
#          super().__init__(msg)


 # Hàm này có thể ném ra GenderException.
# def checkGender(gender):
#      if gender != 'Female':
#          raise ("Accept female only")
# checkGender("Mmale")
# print(1)
# assert 2+2 ==4
# print(2)
# assert 1+1 ==3
# print(3)

# print(0)
# assert "h"!="w"
# print(1)
# assert False,"false rồi"
# # print(2)
# # assert True
# # print(3)
# def my_func(x):
#     assert x>0,"Error"
#     print(x)
# my_func(-1)
# file = open("newfile.txt","w")
# file.write("d2")
# file.close()
# msg = "Hello world!"
# file = open("newfile.txt","w")
# amouit = file.write(msg)
# print(amouit)
# file.close()
# try :
#     print(1)
#     assert 2+2 ==5
# except AssertionError:
#     print(3)
# except:
#     print(4)
# file = open("/usercode/files/books.txt", "r")
#
# #your code goes here
#
#
# file.close()
# names = ["John", "Oscar", "Jacob"]
#
# file = open("names.txt", "w+")
# #write down the names into the file
# for i in names:
#     file.write(i+"\n")
#     # file.write()
#
# file.close()
#
# file= open("names.txt", "r")
# #output the content of file in console
# title = file.readlines()
# print(title)
# for tt in title:
#     code_tt =""
#     if tt != title[-1]:
#         code_tt = code_tt+ tt[0] +str(len(tt)-1)
#         print(code_tt)
#     else:
#         code_tt = code_tt+ tt[0] +str(len(tt))
#         print(code_tt)
#
#
# # file.close()
# stuff =list()
# a_stuff  = []
# print(stuff)
# # print(a_stuff)
# str ="Dat nguyen QUoc"
#
# print("Dat" in str)
# question
# list_a = [expr(i) for i in list_b if func(i)]
#
# list_a = [] for i in list_b: if func(i): list_a.append(i)
# for i in list_b: if func(i): list_a.append(expr(i))
# #correct
# list_a = [] for i in list_b: if func(i): list_a.append(expr(i))
#
# list_a = [expr(i) for i in list_b if func(i)]
# print(list_a)
#
# # list_a = [] for i in list_b: if func(i): list_a.append(i)
# list_a = []
# if func(i):
#     for i in list_b:
# else:
#     list_a.append(((i)))
# # for i in list_b: if func(i): list_a.append(expr(i))
# if func(i):
#     for i in list_b:
# else:
#     list_a.append((expr(i)))
#
# #list_a = [] for i in list_b: if func(i): list_a.append(expr(i))
# list_a = []
# if func(i):
#     for i in list_b:
# else:
#     list_a.append((expr(i)))
# list_a = [expr(i) for i in list_b if func(i)]