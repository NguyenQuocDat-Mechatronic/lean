# # dat = i for i in range(5)
#     i for i in range(5) if True
# # list_A =      [i for i in range(5) if True]

# l = ['even' if i % 2 == 0 else i for i in range(10)]
# l = ['even' if i % 2 == 0 else i for i in range(10)]
# l = 'even' if 5 % 2 != 0 else 3
# l = ['even' if i%2 == 0 else i for i in range(20)]
# lst = []
# lst.append('even' if i%2 == 0 else i for i in range(20))
# print(type(lst))
# for i in lst:
#     print(i)
l = ['even' if i%2 == 0 else i for i in range(20)]
print(l)

def explr():
    l = []
    for i in range(20):
        if i%2==0:
            result = "even"
            l.append(result)
        else:
            result = i
            l.append(result)
    return l
# lst = []
# lst.append(explr())
# print(lst)

# print(l)
# ['even', 1, 'even', 3, 'even', 5, 'even', 7, 'even', 9]

# l = [i * 10 if i % 2 == 0 else i for i in range(10)]
# print(l)
# [0, 1, 20, 3, 40, 5, 60, 7, 80, 9]