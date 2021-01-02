from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Bom dia pessoal, isso é apenas um teste de um bot que estou programando, desconsidere essa mensagem"
        self.grupos = ["Teste1", "Teste2"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang-pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        
    def EnviarMensagens(self):
        #<span dir="auto" title="Teste2" class="_1hI5g _1XH7x _1VzZY">Teste2</span>
        #<div tabindex="-1" class="DuUXI">
        #<span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('DuUXI')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)
            
bot = WhatsappBot()
bot.EnviarMensagens()