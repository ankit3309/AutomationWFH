from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class LoginPAge():

    def __init__(self,driver):
        self.driver = driver

        self.click_login_xpath = '//*[@class="login__body"]/a'
        self.click_account_id = '//*[@class="nyoS7c UzCXuf EIlDfe"]/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/input'
        self.click_password_xpath = '//*[@class="nyoS7c UzCXuf EIlDfe"]/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div/input'

    def click_continue(self):
        continues = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.click_login_xpath)))
        continues.click()

    def enter_email(self,id):
        email = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.click_account_id)))
        email.send_keys(id)
        email.send_keys(Keys.RETURN)

    def enter_password(self,password):
        pwd = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.click_password_xpath)))
        pwd.send_keys(password)
        pwd.send_keys(Keys.RETURN)

