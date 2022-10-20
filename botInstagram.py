from lib2to3.pgen2 import driver
from ssl import _PasswordType
from typing_extensions import Self
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def__init__(self, username, password):
        Self.username = username
        Self.password = password 
        Self.driver = webdriver.Firefox(executable_path=r'C:\Users\Murilo Heyde\Desktop\MENTORIA CONQUISTE SUA VAGA\geckodriver.exe')
    
# "//a[@href='/accounts/login/?source=auth_switcher']"
# "//input[@name='username']
# "//input[@name='password']
    def login(self):
        driver = self.driver
        driver.get('https://wwww.instagram.com')

MuriloBot = InstagramBot('murilheydeadvogado', '19022021')
# Entre com o usuário e senha aqui
MuriloBot.login()







