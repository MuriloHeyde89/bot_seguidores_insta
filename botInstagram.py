from email import parser
from parso import parse
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import configparser
import ast
import random
from configparser import ConfigParser


class InstagramBot:

    def __init__(self,  username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(r'C:\Users\Murilo Heyde\Desktop\MENTORIA CONQUISTE SUA VAGA\bot_seguidores_insta\chromedriver.exe')
        self.base_url = 'https://www.instagram.com'
        self.login()

        # 'Not Now' for notifications
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button._a9_1')))
        self.driver.find_element('css selector', 'button._a9_1').click()

        # XPATH: "//button[contains(text(), 'Follow')]"
        
        time.sleep(10)
        

    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        self.driver.find_element('xpath', '/html/body/div[4]/div/div/button[2]').click()
        WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.NAME, 'username'))) # 30 = timeout
        self.driver.find_element('name', 'username').send_keys(self.username)
        self.driver.find_element('name', 'password').send_keys(self.password)
        self.driver.find_element('xpath', '//*[@id="loginForm"]/div/div[3]/button/div').click()

    def nav_user(self, user):
        self.driver.get('{}/{}'.format(self.base_url, user))

    def like_recent_posts(self, url, posts):
        self.driver.get(url)
        recent_image = self.driver.find_elements('css selector', 'div.v1Nh3.kIKUG._bz0w')[12]
        recent_image.click()

        for i in range(posts):
            WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label=Like]")))
            time.sleep(random.randint(3, 10))

            #like only if it's a real account
            should_like = True
            user = self.driver.find_elements('css selector', 'span.MqpiF')[0]
            for word in bad_words:
                if word.lower() in user.text.lower():
                    should_like = False
            
            if should_like == True:
                like_svg = self.driver.find_element('css selector', "[aria-label=Like]")
                like_button = like_svg.find_element('xpath', './../..')
                like_button.click()
            time.sleep(random.randint(1, 5))
            next_svg = self.driver.find_element('css selector', "[aria-label=Next]")
            next_button = next_svg.find_element('xpath', './../../..')
            next_button.click()


    
if __name__ == '__main__':

    parser = configparser.ConfigParser()
    parser.read('config.ini')
    username = parser['AUTH']['USERNAME']
    password = parser['AUTH']['PASSWORD']

    ig_bot = InstagramBot(username, password)
    time.sleep(5)

    urls = ast.literal_eval(cparser.get('INSTRUCTIONS', 'URLS'))
    bad_words = ast.literal_eval(cparser.get('INSTRUCTIONS', 'KEYWORDS_TO_AVOID'))
    
    for i in range(1000000):
        for u in urls:
            ig_bot.like_recent_posts(u, random.randint(1, 9)) #average 20/h
            time.sleep(random.randint(30, 120))
        time.sleep(random.randint(3600, 3600 * 6)) #average 137/d
    

    #Colocar o caminho para o arquivo chrome driver
    #Passo 1. Criando método de login

    
    # Passo 2. Clicar no agora não do salvar informações do login
    
    # Passo 3. Clicar no agora não da notificação

    # Passo 4. Clicar na barra de pesquisa

    # Passo 5. Digitar hashtag programação

    # Passo 6. Clicar no perfil da hashtag programação

    # Passo 7. Clicar no botão de seguir



MuriloBot = InstagramBot('name', 'password')
# Entre com o usuário e senha aqui
MuriloBot.login()







