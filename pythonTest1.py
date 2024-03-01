# VSCode usando Python com Selenium (Teste básico no Selenium)

# Pré-requisitos:
# Certifique-se de ter o Python instalado no seu sistema.
# Instale o pacote selenium via pip se ainda não estiver instalado.
# Crie um arquivo python.py dentro de alguma pasta para realizar os testes.
# Abre o arquivo usando o VSCode.
# Abra o terminal e digite: pip install selenium

# Exemplo de Teste Simples em Python com Selenium:
from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializa o WebDriver (o chromedriver é baixado automaticamente)
driver = webdriver.Chrome()

# Abre o Google
driver.get("https://www.google.com")

# Localiza o campo de pesquisa e envia o texto
campo_pesquisa = driver.find_element(By.NAME, "q")
campo_pesquisa.send_keys("Selenium")

# Envia o formulário
campo_pesquisa.submit()

# Verifica o título da página
if "Selenium" in driver.title:
    print("Testado e aprovado! Encontrou 'Selenium' no título")
else:
    print("Testado e reprovado! Não encontrou 'Selenium' no título")

# Fecha o navegador
driver.quit()

# -----
# -----
# -----

# Caso o VSCode não reconheça o Selenium, siga esses passos:
# Abra a aba de comandos do VSCode (Ctrl+Shift+P)
# Escolha ou digite "Pyton: Selecionar Intérprete"
# Selecione a versão Python padrão do seu sistema operacional (global).

# Explicação Passo a Passo:
# Importação de Bibliotecas: Importamos as bibliotecas necessárias do Selenium.
# Configuração do WebDriver: Definimos o path para o chromedriver.
# Inicialização do WebDriver: Criamos uma instância do ChromeDriver.
# Navegação para o Google: Usamos get() para abrir o Google.
# Localização do Campo de Pesquisa: Usamos find_element(By.NAME, "q") para encontrar o campo de pesquisa.
# Preenchimento o Envio do Formulário: Enviando o texto "Selenium" para o campo de pesquisa e submetendo o formulário.
# Verificação do Título da Página: Usamos title para verificar se o título contém "Selenium".
# Saída do Teste: Uma mensagem é exibida dependendo do resultado.
# Fechamento do Navegador: Usamos quit() para fechar o navegador após o teste.

# Agora é com você:
# Busque compreender a estrutura do código e depois realize alterações, mudando o site destino, tentando
# pressionar botões e fazer login via código Python.
