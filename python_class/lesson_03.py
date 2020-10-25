'''
1：a=[1,2,'6','summer'] 请用成员运算符判断 i是否在这个列表里面

a = [1,2,'6','summer']
if "i" in a:
    print("i是成员")
else:
    print("i不是成员")

2：dict_1={"class_id":45,'num':20} 请判断班级上课人数是否大于5
注：num表示课堂人数。如果大于5，输出人数。

dict_1={"class_id":45,'num':20}
print(dict_1['num']>5)
if dict_1['num'] >=5 :
    print("上课人数为：{}".format(dict_1['num']))
else:
    print("上课人数小于5")

3、list1 = ['方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝']
列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。
并且把字典都存在新的 list中，最后打印最终的列表。
方法1： 手动扩充--字典--存放在列表里面；
方法2： 自动--dict（）
'''

list1 = ['方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝']
#手动
#dict1 = {"姓名":"方方土","性别":"男","年龄":"18","城市":"北京"}
#dict2 = dict(姓名 = "七木",性别 = "男",年龄 = "19",城市 = "上海")
#list2 = [dict1,dict2]
#print(dict1)
#print(dict2)
#print(list2)

#自动
list2 = []      #空列表，存储字典
list_age = [18,19,20,21,22,23]
list_sex = ['1','2','1','1','2','1']
list_city = ['北京','上海','武汉','深圳','杭州','昆明']
for i in range(6):
    dict1 = dict(name=list1[i],性别 = list_sex[i],年龄 = list_age[i],城市 = list_city[i])
    list2.append(dict1)
print(list2)