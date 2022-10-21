from email.errors import HeaderDefect
from lib2to3.pgen2 import driver
from operator import index
from webbrowser import get
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__ (self, username, password):
        self.username = username
        self.password = password 
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\Murilo Heyde\Desktop\MENTORIA CONQUISTE SUA VAGA\geckodriver.exe')

        #Colocar o caminho para o arquivo geckodriver
    #Criando método de login
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
        self.curtir_fotos_com_a_hashtag('memes') #alterar a hashtag aqui

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        #Simulando como uma pessoa digita
        print("going to start typing message into message share text area")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

# Criar método de curtir fotos
    def curtir_fotos_com_a_hashtag(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(5)
        for i in range(1, 3): #alterar aqui a quantidade de páginas para descer
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        hrefs = driver.find_element_by_tag_name('a')
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        [href for href in pic_href if hashtag in href]
        print(hashtag + 'fotos: ' + str(len(pic_hrefs)))
        testes = [
            href
            for href in pic_hrefs
            in hashtag in href and href.index("https://www.instagram.com/programa") != -1
        ]
        for pic_href in pic_hrefs:
            try:
                pic_href.index("https://www.instagram.com/p")
            except ValueError as err:
                print("Pulando link inválido!")
                continue
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                #driver.find_element_by_class_name('//button[@class="_9AhH0"')
                #time.sleep(10)
                
                #driver.find_element_by_class_name("wpO6b").click()
                #driver.find_elements_by_css_selector(".eos2AS section span button").click()
                driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button")
                # driver.find_element_by_xpath("//span[@class='fr66n']").click() 

                driver.find_element_by_class_name("eo2As").find_element_by_class_name("ltpMr").find_element_by_class_name("fr66n").find_element_by_tag_name("button").click()
                time.sleep(random.randint(19,23))
                #curtir_element.send_keys(Keys.RETURN)
                # time.sleep(random.randint(19, 32))
            except Exception as e:
                print(e)

                time.sleep(5)
        


MuriloBot = InstagramBot('Muriloheydeadvogado', '19022021')
# Entre com o usuário e senha aqui
MuriloBot.login()







