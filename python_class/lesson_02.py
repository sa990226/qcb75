'''
str1 = 'python hello aaa 123123aabb'
print(str1)
print(str1[0:6:1])
str1 = str1.replace("python","lemon")
print(str1)
str1 = str1.replace("lemon","python")
print(str1.find("o a"))
print("o a" in str1)
print(str1.find("he"))
print("o a" in str1)
print(str1.index("ab"))
print("o a" in str1)
print(str1.find('aaa'))
'''

name = input("请输入姓名：")
age = input("请输入年龄：")
sex = input("请输入性别：")

print("*" * 20)
print('''姓名：{0}
年龄：{1}
性别：{2}'''.format(name,age,sex))
print("*" * 20)

