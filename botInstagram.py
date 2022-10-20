from lib2to3.pgen2 import driver
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
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.pesquisar('memes.brasil_hoje')

# Criar método de curtir fotos
    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/')
        time.sleep(5)
        user_element = driver.find_element_by_xpath("//input._aauy.focus-visible")
        user_element.clear()
        user_element.send_keys(self.)
        #olhar acima self de clicar botão pesquisar e preencher
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        hrefs = driver.find_element_by_tag_name('a')
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print(hashtag + ' fotos: ' + str(len(pic_hrefs)))
        testes = [
            href
            for href in pic_hrefs
            in hashtag in href and href.index("https://www.instagram.com/p") != -1
        ]


MuriloBot = InstagramBot('Muriloheydeadvogado', '19022021')
# Entre com o usuário e senha aqui
MuriloBot.login()







