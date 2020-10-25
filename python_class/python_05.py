from  selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://erp.lemfix.com/login.html")
driver.maximize_window()
#time.sleep(2)
#driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_xpath("//input[@id = 'username']").send_keys("test123")
#time.sleep(2)
driver.find_element_by_id("password").send_keys("123456")
#time.sleep(2)
driver.find_element_by_id("btnSubmit").click()

'''
xpath元素定位
1.绝对路径
2.相对路径---只靠自己特征定位   //开头--加上我关心的节点
标签名+属性  //标签名[@属性名="属性值"]
3.层级定位
//标签名[@属性值]//标签名[@属性名="属性值"]
4.文本属性  //b[text()="柠檬ERP"]
5.包含属性
//标签名[contains(@属性名,属性值)]   //标签名[contains(text(),属性值)]
--//input[contains(@class,"username")]

对界面进行的操作
1.点击--click
2.传值--send_keys
3.获取页面文本--text
但凡切换了页面，元素可能为显示完成，元素不显示--最后加个等待
4.获取属性  attribute

三种等待方式
1.强制等待：time.sleep() --浪费时间,时间未到就不会继续执行
2.智能等待
    隐试等待：可以设置等待时间，等待时间未结束前找到元素则不继续等待
        注意：一个会话只会有一个
    显示等待：expected_condition

page_title = driver.title      #获取页面标题

页面层级路径出现iframe，需要去切换才能进行元素定位

irame切换
1.通过id进行切换
2.通过元素定位切换
3.通过iframe下标
'''
page_text = driver.find_element_by_xpath('//div[@class = "login-box"]//b').text   #获取文本
print(page_text)
#page_title = driver.title      #获取页面标题
#print(page_title)
#第5条用例
#time.sleep(5)
user_name = driver.find_element_by_xpath("//p[text()='测试用户']").text
if user_name == "测试用户":
    print("登录的用户为：{}".format(user_name))
else:
    print("这个测试用例不通过")

#点击零售出库
driver.find_element_by_xpath("//span[text()='零售出库']").click()
P_id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")     #获取id属性
F_id = P_id + "-frame"
print(F_id)
#通过id进行iframe切换
#driver.switch_to.frame(F_id)

#通过元素定位xpath定位
#driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(F_id)))

#通过iframe下标
driver.switch_to.frame(1)
driver.find_element_by_id("searchNumber").send_keys("314")
#点击查询
driver.find_element_by_id('searchBtn').click()
time.sleep(2)
#找到单据编号
num = driver.find_element_by_xpath("//tr[@id ='datagrid-row-r1-2-0']//td[@field = 'number']/div").text
if "314" in num:
    print("搜素结果正确")
else:
    print("用例不通过")