'''1.
把字符串转成列表 - list()
str1 = 'My name is bai. o((≧▽≦o)太好笑了！！'
list1 = list(str1)
print(list1)
2.
完成任意整数序列的相加 - 生成一个整数序列，里面全是数字。求里面所有数字的和

sum = 0
for i in range(0,6,1):
    print(i)
    sum += i
print(sum)
3.
定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。-- if 判断嵌套


'''
def panduan1(list):
    num = len(list)
    if num >= 5:
        print("True")
    else:
        print("False")
def panduan2(str):
    num = len(str)
    if num >= 5:
        print("True")
    else:
        print("False")

def panduan3(dict):
    num = len(dict)
    if num >= 5:
        print("True")
    else:
        print("False")
list1 = ['1','1','aa','bb']
str1 = 'python hello aaa 123123aabb'
dic1 = {"姓名":"小小","age":"19"}

panduan1(list1)
panduan2(str1)
panduan3(dic1)