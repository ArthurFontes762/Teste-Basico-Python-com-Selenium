# Exemplo de Teste de login em Python com Selenium, vamos fazer um teste com o "site saucedemo"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configura o path para o chromedriver.exe (ou chromedriver para Linux/Mac) 
# Site para baixar chromedriver.exe para testes: https://chromedriver.chromium.org/downloads
service = Service(executable_path='C:\\') # Sempre usando aspas duplas (\\)
options = webdriver.ChromeOptions()

# Inicializa o WebDriver (o chromedriver é baixado automaticamente) 
driver = webdriver.Chrome(service=service, options=options)

try:
    # Abre o site 
    driver.get("https://www.saucedemo.com/") # Pode ser qualquer site 
    driver.implicitly_wait(15) 

    campo_email = driver.find_element(By.ID, "user-name") 
    campo_email.send_keys("standard_user") # Substitua o campo dentro das aspas duplas

    # Aguarda a página de senha carregar e localiza o campo de senha 
    campo_senha = driver.find_element(By.ID, "password")
    campo_senha.send_keys("secret_sauce") # Substitua o campo dentro das aspas duplas

    # Executa um script para clicar no botão de login
    driver.implicitly_wait(15)
    botao_senha = driver.find_element(By.ID, "login-button")
    botao_senha.click()

    # Adiciona duas compras no carrinho 
    pagina_compra1 = driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]')
    pagina_compra1.click()

    pagina_compra2 = driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-bike-light"]')
    pagina_compra2.click()

    # Abre o carrinho
    carrinho = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    carrinho.click()
    driver.implicitly_wait(15) 

    # Prossiga com a compra ficticia
    carrinho_fechamento = driver.find_element(By.XPATH, '//*[@id="checkout"]')
    carrinho_fechamento.click()

    # Veja se seu teste passou

    print("Testado e aprovado! Passou do teste de compras ficticias.") 
except: 
    print("Testado e reprovado! Não passou do teste de compras ficticias.")

# Fecha o navegador
driver.quit()
