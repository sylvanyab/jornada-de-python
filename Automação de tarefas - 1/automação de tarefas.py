import pyautogui
# docomentação do pyautogui - https://pyautogui.readthedocs.io/en/latest/

import time 

# Tempo de espera para cada comando no pyautogui
pyautogui.PAUSE = 1.5

# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(2)
# Digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Espera 3 segundos (Nada haver/ou diferente do PAUSE do pyautogui)
time.sleep(3.5)

# Passo 2: Fazer login

    # Preencher email
pyautogui.click(x=504, y=419)
pyautogui.write("silvaniab@gmal.com")
 
    # Preencer a senha
pyautogui.press("tab")
pyautogui.write("bomdiaabencoado")

# Botão logar 
pyautogui.press("tab")
pyautogui.press("enter")

#espera de 3 segundos
time.sleep(3.5)

# Passo 3: Importar a base de dados
import pandas

# le a base de dados e armazena na variável tabela 
tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar 1 produto
for linha in tabela.index: # o index é o número de cada linha da tabela 
    pyautogui.click(x=703, y=294)
#fazer o primeiro cadastro manualmente (pra teste) depois automatiza.

    codigo = tabela.loc[linha, "codigo"] # loc é para localizar  a linha
    pyautogui.write(codigo)

    pyautogui.press("tab") # Passar para o próximo campo
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)

# Passo 5: Repetir para todos os produtos


