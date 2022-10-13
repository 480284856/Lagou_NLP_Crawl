database = open('database.txt','w',encoding='utf-8')

import  time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions

options = EdgeOptions()
options.use_chromium = True
options.binary_location = r'C:\Program Files (x86)\Microsoft\EdgeCore\106.0.1370.42\msedge.exe'

driver = Edge(options=options,executable_path=r'X:\Code\Scrapy\Crawl\edge_driver\msedgedriver.exe')

pages2crawl=17  # 想爬多少页
waittime = 3

def get_and_save_info(driver: Edge):
    '''进入页面后，获取职位信息并保存'''
    description_element_xpath = r'//*[@id="job_detail"]/dd[2]/h3'
    description = driver.find_element(By.XPATH, description_element_xpath).text.replace('\t\r\n','')
    description = re.sub(r'\n|\r|\t', '', description)
    require_xpath = r'//*[@id="job_detail"]/dd[2]/div'
    require = driver.find_element(By.XPATH,require_xpath).text
    require = re.sub(r'\n|\r|\t','',require)
    database.write('{title}\t{context}\n'.format(title=description,context=require))

def go_to_main_page(driver: Edge):
    '''关闭当前标签页，回到主页面'''
    driver.close()
    time.sleep(waittime)
    driver.switch_to.window(main_page)

def crawl_a_page(driver: Edge):
    target_pos = driver.find_elements(By.XPATH,'//*[@id="jobList"]/div[1]//div[@class="item__10RTO"]')
    for pos in target_pos:
        '''鼠标移动'''
        ActionChains(driver=driver).move_to_element(pos).perform()
        time.sleep(waittime)
        ActionChains(driver).click(pos).perform()
        time.sleep(waittime)
        '''进入页面'''
        for h in driver.window_handles:
            if h != main_page:
                driver.switch_to.window(h)
                time.sleep(waittime)
                get_and_save_info(driver)
                go_to_main_page(driver)
                time.sleep(waittime)

driver.get('https://www.lagou.com/wn/jobs?labelWords=&fromSearch=true&suginput=&kd=NLP')
driver.implicitly_wait(20)  # 隐式等待20秒，在元素没有出现时，20s后再报错，若期间找到了，那么就继续执行

next_path_buttom = driver.find_element(By.LINK_TEXT,'下一页')
clik = False

while next_path_buttom.is_enabled():  # 一直爬，直到爬完
    if clik:
        ActionChains(driver).move_to_element(next_path_buttom).perform()
        time.sleep(waittime)
        ActionChains(driver).click(next_path_buttom).perform()
        time.sleep(waittime)
    main_page = driver.current_window_handle

    crawl_a_page(driver)

    next_path_buttom = driver.find_element(By.LINK_TEXT,'下一页')
    clik = True  # 一页爬完，需要点击进入下一页

