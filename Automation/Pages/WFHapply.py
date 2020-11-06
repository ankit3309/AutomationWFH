from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys as K
import time

class ApplyWFH():

    def __init__(self,driver):
        self.driver = driver

        self.click_apply_xpath = '//*[@class="btn btn--alternate btn--curved mr-10 ml-10 d-inline-flex flex-fix"]'
        self.click_availability_xpath = '//*[@class="form-wrap__col col-sm-6"]/div[3]/input'
        self.click_tasktodo_name = "taskToDo"
        self.click_emo_xpath = '//*[@class="form-wrap__col col-sm-6"]/div[6]/div/div/div/div[1]/div/div/label'
        self.click_apply_wfh_xpath = '//*[@class="action-bar-footer action-bar-footer--bordered-top"]/button'


    def click_wfh(self):
        wfh = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.click_apply_xpath)))
        wfh.click()

    def enter_availability(self,whour):
        availabilities = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.click_availability_xpath)))
        availabilities.clear()
        # time.sleep(2)
        # import pdb
        # pdb.set_trace()
        availabilities.send_keys(whour)
        # print(whour)
        availabilities.send_keys(whour)

    def enter_todo(self,task):
        todo = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.NAME,self.click_tasktodo_name)))
        todo.send_keys(task)

    def click_emoji(self):
        emoji = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.click_emo_xpath)))
        emoji.click()

    def click_apply(self):
        apply = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.click_apply_wfh_xpath)))
        apply.click()
        print("WFH Applied Successfully")




