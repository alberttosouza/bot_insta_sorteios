from selenium import webdriver
import random
import time


class insta_bot:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        self.driver.get(f'https://instagram.com/'), time.sleep(4)

    def logar(self):
        # caixa de login / por login
        self.driver.find_element_by_xpath("//input[@name=\"username\"]") \
            .send_keys(self.login)

        time.sleep(1)

        # caixa de senha / por senha
        self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(self.senha)

        # botão entrar
        self.driver.find_element_by_xpath('//button[@type="submit"]') \
            .click()

    def seguir(self, user):

        # perfil alvo
        time.sleep(4)
        print('abrindo perfil da pagina')
        self.driver.get(f'https://www.instagram.com/{user}')

        time.sleep(2)

        print('botão seguir')
        # botão de seguir
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button")\
            .click()

        time.sleep(2)
        print('home perfil')
        self.driver.get(f'https://www.instagram.com/{user}')
        time.sleep(3)

    def seguirPaginasQueApaginaSegue(self, resposta, quant=0):
        resposta = resposta.upper()

        if resposta == 'S':
            print('Perfis seguidos pela pagina')
            self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
            time.sleep(2)

            # seguir/rolagem
            quantidade = quant
            cont = 0
            rolagem = False
            while cont <= quantidade - 1:
                try:  # verifica se há botão de seguir
                    self.driver.find_element_by_class_name("sqdOP.L3NKy.y3zKF")

                except:  # se não houver botão de seguir
                    print('-já seguindo!!!')
                    cont += 1
                    rolagem = True

                else:  # se haver botão de seguir
                    self.driver.find_element_by_class_name("sqdOP.L3NKy.y3zKF").click()
                    print('--> SEGUIU!!!')
                    cont += 1
                    time.sleep(4)

                if rolagem:  # rolagem da barra de seguidores
                    time.sleep(1)
                    try:  # verifica se caixa de seguidores está aberta
                        seguidores = self.driver.find_element_by_xpath("//div[@class='isgrP']")
                    except:  # se estiver fechada
                        print('Caixa de seguidores fechada')
                        time.sleep(1)
                        print('Reabrindo...')
                        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
                        time.sleep(2)
                        seguidores = self.driver.find_element_by_xpath("//div[@class='isgrP']")
                        self.driver.execute_script(
                            'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', seguidores)
                        rolagem = False
                    else:  # se estiver aberta
                        self.driver.execute_script(
                            'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', seguidores)
                        rolagem = False
        if resposta == 'N':
            print('Não seguir perfis seguidas pela pagina!')

        else:
            print('Opção errada!')
    time.sleep(2)

    def publicacao(self, pub, repeticao):

        print('Abrindo publicação da promoção!!!')
        self.driver.get(pub) #abre a publicação da promoção
        time.sleep(2)
        while True:
            for quant_marcar in range(0, repeticao):

                #sorteia a inicial de uma @ de um perfil
                vogais = ['a', 'e', 'i', 'o', 'u']
                consoantes = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 't']

                a = random.choice(consoantes)
                b = random.choice(vogais)
                perfil = '@' + a + b

                #clica na caixa de comentarios
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div[1]/form/textarea")\
                    .click()
                time.sleep(1)
                #passa a inicial do perfil sorteado
                self.driver.find_element_by_class_name("Ypffh").send_keys(perfil)
                time.sleep(2)
                #clica no primeiro perfil sugerido
                self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div[2]/div/div/button[1]')\
                    .click()
                time.sleep(0.5)
                self.driver.find_element_by_class_name("Ypffh").send_keys(' ')
                time.sleep(0.5)

            #clica em publicar
            self.driver.find_element_by_xpath('//button[@type="submit"]') \
                .click()
            time.sleep(2)


bot = insta_bot('login', 'senha') #coloque login e senha entre as aspas
bot.logar()
bot.seguir('aqui entre aspas') #perfil da pagina que esta sorteando
bot.seguirPaginasQueApaginaSegue('n', 4) #coloque 's' para sim 'n' para não, para seguir os perfis que a pagina segue e quantos são
bot.publicacao('link completo', 2) #coloque o link do post do sorteio e quantas pessoas marcar
