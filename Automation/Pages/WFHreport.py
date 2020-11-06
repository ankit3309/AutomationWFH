from selenium.webdriver.common.keys import Keys as K
from selenium.webdriver import ActionChains as A
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



class LeavePage():


    def __init__(self,driver):
        self.driver = driver


        self.click_leave_xpath = '//*[@class="header-left__nav left"]/li[3]/a'
        self.click_wfh_xpath = '//*[@class="btn btn--primary btn--curved btn--notification-available"]'
        self.copy_todo_name = "taskToDo"
        self.paste_done_name = "taskDone"
        self.send_class = "btn btn--primary btn--curved mr-10"
        self.click_send_report_xpath = '//*[@class="action-bar-footer action-bar-footer--bordered-top"]/button'



    def click_leave(self):
        leave = WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.XPATH, self.click_leave_xpath)))
        leave.click()

    def click_wfh(self):
        wfh = WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.XPATH, self.click_wfh_xpath)))
        wfh.click()

    def copy(self):
        a = A(self.driver)
        WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.NAME, self.copy_todo_name))).click()
        a.key_down(K.CONTROL).send_keys("a").perform()
        # time.sleep(3)
        a.key_down(K.CONTROL).send_keys("c").perform()
        # time.sleep(2)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.NAME, self.paste_done_name))).click()
        a.key_down(K.CONTROL).send_keys("v").perform()

    def send_report(self):
        report = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.click_send_report_xpath)))
        report.click()
        print("Reported Successfully")
