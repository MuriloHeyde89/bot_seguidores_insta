from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__ (self, username, password):
        self.username = username
        self.password = password 
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\Murilo Heyde\Desktop\MENTORIA CONQUISTE SUA VAGA\geckodriver.exe')
        #Colocar o caminho para o arquivo geckodriver

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(3)
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)

MuriloBot = InstagramBot('murilheydeadvogado', '19022021')
# Entre com o usuário e senha aqui
MuriloBot.login()







