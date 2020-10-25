import  time
def login_page(username,password,driver):
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()

def open_url(url,driver):
    driver.get(url)
    driver.maximize_window()

def Search_key(url,driver,username,password,s_key):
    open_url(url,driver)
    login_page(username,password,driver)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    P_id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")  # 获取id属性
    F_id = P_id + "-frame"
    # 通过id进行iframe切换
    driver.switch_to.frame(F_id)
    driver.find_element_by_id("searchNumber").send_keys(s_key)
    # 点击查询
    driver.find_element_by_id('searchBtn').click()
    time.sleep(2)
    # 找到单据编号
    num = driver.find_element_by_xpath("//tr[@id ='datagrid-row-r1-2-0']//td[@field = 'number']/div").text
    return num