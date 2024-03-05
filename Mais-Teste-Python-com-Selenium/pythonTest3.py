# Exemplo de Teste de login em Python com Selenium:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configura o path para o chromedriver.exe (ou chromedriver para Linux/Mac) 
service = Service(executable_path='C:\\') # Sempre usando aspas duplas (\\)
options = webdriver.ChromeOptions()

# Inicializa o WebDriver (o chromedriver é baixado automaticamente) 
driver = webdriver.Chrome(service=service, options=options)

# Abre o site 
driver.get("https://wordpress.com/log-in/pt-br") # Pode ser qualquer site 
driver.implicitly_wait(15) 

campo_email = driver.find_element(By.ID, "usernameOrEmail") 
campo_email.send_keys("Seu-email") # Substitua pelo seu e-mail/user

# Executa um script para clicar no botão de continuar para a senha
botao_continuar = driver.find_element(By.XPATH,'//*[@id="primary"]/div/main/div[3]/div/form/div[1]/div[2]/button')
botao_continuar.click()

# Aguarda a página de senha carregar e localiza o campo de senha 
campo_senha = driver.find_element(By.ID, "password")

# Envie sua senha
campo_senha.send_keys("Sua-senha") # Substitua "campo_senha" pela sua senha real

# Executa um script para clicar no botão de login
botao_senha = driver.find_element(By.XPATH,'//*[@id="primary"]/div/main/div[3]/div/form/div[1]/div[2]/button')
botao_senha.click()

# Aguarda até que o menu de navegação seja carregado após o login
try:
 menu_navegacao = WebDriverWait(driver, 15).until(
 EC.presence_of_element_located((By.ID, "platform-list-react"))
 )
 print("Testado e aprovado! Login no Wordpress bem sucedido.") 
except: 
 print("Testado e reprovado! Não foi possível fazer login no Wordpress.")

# Abre o site 
driver.get("https://prozds2.wordpress.com") # Pode ser qualquer site 
driver.implicitly_wait(15)

# Abre uma página no site 
paginasite_2 = driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/div/ul/li[1]/div/h2/a')
driver.implicitly_wait(15)

campo_comment = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
campo_comment = driver.find_element(By.ID, "comment") 
campo_comment.send_keys("Seu comentário") # Adiciona um comentário

# Executa um script JavaScript para clicar no botão de Comentário
driver.implicitly_wait(15)
botao_comment = driver.find_element(By.XPATH,'//*[@id="comment-submit"]')
botao_comment.click

# Aguarda até que o menu de navegação seja carregado após o comentário
try:
 menu_navegacao = WebDriverWait(driver, 15).until(
 EC.presence_of_element_located((By.ID, "platform-list-react"))
 )
 print("Testado e aprovado! Comentário adicionado com sucesso no Wordpress pelo Selenium.") 
except: 
 print("Testado e reprovado! Não foi possível fazer um comentário no Wordpress pelo Selenium.")