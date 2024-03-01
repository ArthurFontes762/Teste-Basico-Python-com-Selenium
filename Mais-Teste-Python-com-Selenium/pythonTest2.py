# Criando um teste no Selenium
# Certifique-se de ter o Python instalado no seu sistema.
# Crie um projeto no VSCode, adicionando um arquivo Python.
# Escolha um site onde vocês tenham uma conta ou criem uma conta em um site à sua escolha, desde que 
# ele solicite login e senha (deve ser um site diferente do nosso exemplo abaixo).
# Instale o pacote Selenium via pip se ainda não estiver instalado: pip install selenium

# Crie um teste no seu arquivo Python, que deve acessar o site que você escolheu e testar duas opções de 
# login: uma com credenciais válidas, outra com inválidas.

# Para os notebooks/PC's que estiverem apresentando problema de PATH, baixe o driver nesse link:
# https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/win32/chromedriver-win32.zip

# Em seguida, direcione o service para o arquivo dezipado, como feito no exemplo abaixo, isso deve solucionar a questão.
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
driver.get("https://github.com/login") # Pode ser qualquer site 
driver.implicitly_wait(15) 

# Localiza o campo de e-mail e envia o e-mail
 
campo_email = driver.find_element(By.ID, "login_field") 
campo_email.send_keys("exemplo@email.com") # Substitua pelo seu e-mail/user

# Aguarda a página de senha carregar e localiza o campo de senha 
campo_senha = driver.find_element(By.ID, "password")

# Envie sua senha
campo_senha.send_keys("1234") # Substitua "campo_senha" pela sua senha real

# Executa um script JavaScript para clicar no botão de login
driver.execute_script("document.getElementById('user_submit').click()")

# Aguarda até que o menu de navegação seja carregado após o login
try:
 menu_navegacao = WebDriverWait(driver, 15).until(
 EC.presence_of_element_located((By.ID, "platform-list-react"))
 )
 print("Testado e aprovado! Login no Github bem sucedido.") 
except: 
 print("Testado e reprovado! Não foi possível fazer login no Github.")

# Fecha o navegador 
driver.quit()

# Caso o VSCode não reconheça o Selenium, siga esses passos:
# Abra a aba de comandos do VSCode (Ctrl+Shift+P)
# Escolha ou digite "Python: Selecionar intérprete"
# Selecione a versão Python padrão do seu sistema operacional (global)