import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver as wd
import random


def escolher_conversa(nome_conversa):  # select contact
    global driver  # import driver
    wait = WebDriverWait(driver, 30, 2)  # wait
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,f'span[title|="{nome_conversa}"]')))
    time.sleep(2)
    conversa = driver.find_element(By.CSS_SELECTOR, f'span[title^="{nome_conversa}"]')
    conversa.click()
    
def r_txt():  # get random reply from a list
    valor = random.randint(0,(len(texto)-1))
    return texto[valor]
        

def spam(txt):  #send message
    global driver
    janela = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')  # select the window
    janela.click()
    janela.send_keys(txt)
    botao = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[3]/button')  #select chat
    botao.click()
    
def check_message(nome_conversa):
    while True:
        try:        
            if  driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[10]/div/div/div[2]/div[2]/div[2]/span[1]/div/span') \
                    and driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[10]/div/div/div[2]/div[1]/div[1]/span/span').text == nome_conversa:
                escolher_conversa(nome_conversa)
                spam(r_txt())            
                driver.find_element(By.CSS_SELECTOR, 'span[title^="Anotações"]').click() # Fixed chat to switch and wait for notifications
                time.sleep(30) # time between replies
        except:
            None
 

####  Contact + text
nome_conversa = ""  #Nome do contato
texto = [] # lista de mensagens
url = "https://web.whatsapp.com/" #Whatsapp web link
#######  Config
option = Options()
option.add_argument('--user-data-dir=./User_Data')  # temp
option.headless = False  # show or hide
path = Service("C:\\Users\dir\Desktop\Python\Selenium\chromedriver.exe")
driver = wd.Chrome(service=path, options=option) #chromedriver location
###### Run
driver.get(url)
time.sleep(5)
check_message(nome_conversa)

