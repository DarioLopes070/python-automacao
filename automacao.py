import pyautogui
import time
suporte = 21967218715

pyautogui.PAUSE = 0.5 # Define uma pausa de 0.5 segundos entre as ações do PyAutoGUI
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.press('win') # Pressiona a tecla "Win" para abrir o menu Iniciar
pyautogui.write('opera') # Digita "opera" para buscar o navegador Opera
pyautogui.press('enter') # Pressiona "Enter" para abrir o navegador   
pyautogui.write(link) # Digita o link do site
pyautogui.press('enter') # Pressiona "Enter" para acessar o site
time.sleep(3) # Aguarda o site carregar
pyautogui.click(x=895, y=496) # Clica no campo de email (substitua as coordenadas x e y pelas coordenadas corretas do campo de email na sua tela)
pyautogui.write("teste@gmail.com") # Digita o email (substitua "teste@gmail.com" pelo email correto)
pyautogui.press("tab") # Pressiona a tecla "Tab" para ir para o campo de senha
pyautogui.write("123456") # Digita a senha (substitua "123456" pela senha correta)
pyautogui.press("tab") # Pressiona a tecla "Tab" para ir para o botão de login
pyautogui.press("enter") # Pressiona "Enter" para fazer login
time.sleep(3) # Aguarda a página carregar após o login


import pandas # Importa a biblioteca pandas para manipulação de dados

tabela = pandas.read_csv("produtos.csv") # Lê o arquivo CSV "produtos.csv" e armazena os dados em um DataFrame chamado "tabela"
print(tabela) # Imprime o conteúdo do DataFrame "tabela" na tela
for linha in tabela.index: # Itera sobre cada linha do DataFrame "tabela"
    pyautogui.click(x=820, y=352) # Código do Produto (substitua as coordenadas x e y pelas coordenadas corretas do campo de código do produto na sua tela)
    pyautogui.PAUSE = 0.1 # Define uma pausa de 0.1 segundos entre as ações do PyAutoGUI
    for coluna in tabela.columns: # Itera sobre cada coluna do DataFrame "tabela"
        valor = tabela.loc[linha, coluna]
        if pandas.notna(valor):
            pyautogui.write(str(valor)) # Digita o valor da célula correspondente à linha e coluna atual
        pyautogui.press("tab") # Pressiona a tecla "Tab" para ir para o próximo field   
    pyautogui.press("enter") # Pressiona "Enter" para salvar o produto
    pyautogui.scroll(5000) # Rola a tela para cima
    time.sleep(0.5) # Aguarda 0.5 segundos antes de passar para o próximo produto    