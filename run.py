from python_class import python_06  #导入函数文件
from test_data import test_data     #导入测试数据
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
#1.先将参数取出来，传参到函数调用里
url = test_data.url["url"]  #取值url
user = test_data.login_data["username"]     #取值用户名
pwd = test_data.login_data["password"]      #取值密码
s_key = test_data.s_key["s_key"]
#函数的调用

result = python_06.Search_key(driver=driver,url=url,username=user,password=pwd,s_key=s_key)

if s_key in result:
    print("搜索结果正确")
else:
    print("用例不通过")