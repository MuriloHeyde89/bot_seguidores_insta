from email.errors import HeaderDefect
from lib2to3.pgen2 import driver
from operator import index
from webbrowser import get
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class InstagramBot:
    def __init__ (self, username, password):
        self.username = username
        self.password = password 
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\Murilo Heyde\Desktop\MENTORIA CONQUISTE SUA VAGA\geckodriver.exe')

        #Colocar o caminho para o arquivo geckodriver
    #Passo 1. Criando método de login
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
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
    
    # Passo 2. Clicar no agora não do salvar informações do login

    # Passo 3. Clicar no agora não da notificação

    # Passo 4. Clicar na barra de pesquisa

    # Passo 5. Digitar hashtag programação

    # Passo 6. Clicar no perfil da hashtag programação

    # Passo 7. Clicar no botão de seguir



MuriloBot = InstagramBot('Muriloheydeadvogado', '19022021')
# Entre com o usuário e senha aqui
MuriloBot.login()







