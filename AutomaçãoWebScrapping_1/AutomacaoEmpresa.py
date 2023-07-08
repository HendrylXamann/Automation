#Importações:
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import datetime
import time as time
from tkinter import Tk, Label

#Para gerar o arquivo excel com data atual:
data_atual = datetime.datetime.now().strftime("%Y%m%d") #Parte 1: Gerar arquivo final com data do dia;
nome_da_planilha = f"{data_atual}.xlsx" #Parte 2: Gerar arquivo final com data do dia;

#Abrir site:
url_abrir = " site" #link do site reservado (empresa privada)
drive = webdriver.Chrome(url_abrir)
drive.get(url_abrir)

#Função da contagem regressiva
def contagem_regressiva(tempo_total, janela):
    for segundos_restantes in range(tempo_total, 0, -1):
        minutos = segundos_restantes // 60
        segundos = segundos_restantes % 60

        tempo_restante = f"{minutos:02d}:{segundos:02d}"
        janela['text'] = tempo_restante

        janela.update()
        time.sleep(1)

    janela['text'] = "THE TIME IS OVER"
tempo_total = 40  # Tempo total em segundos para a contagem regressiva

# Criar janela com a contagem:
root = Tk()
root.title("Contagem Regressiva")
root.geometry("200x100")
label_contagem = Label(root, text="", font=("Arial", 20)) # Cria o rótulo para a contagem regressiva1
label_contagem.pack(pady=20) # Cria o rótulo para a contagem regressiva2
contagem_regressiva(tempo_total, label_contagem)# Iniciar contagem regressiva
root.destroy()# Fechar janela após a contagem regressiva

# #Leitura do arquivo com os dados a serem analisados, criação de lista para armazenamento definição de ações do loop:  
nome_do_arquivo = "Base.xlsx"
df = pd.read_excel(nome_do_arquivo)
listafinal = []
limite = 100
contador = 0

#Realização da automação:
while not df.empty and contador < limite:
    for index,row in df.iterrows():
        click_linha = drive.find_element(By.XPATH,'//*[@id="msisdn"]')
        click_linha.send_keys(int(row["LINHA"]))
        click_consult = drive.find_element(By.XPATH, '//*[@id="btnSearch"]')
        click_consult.click()
        time.sleep(5)
        try:
            elemnto_except = drive.find_element(By.XPATH,'//*[@id="msg-info"]/p')
            print("lINHA NÃO LOCALIZADA")
            volta_consult = drive.find_element(By.XPATH, '/html/body/center/table/tbody/tr[2]/td/div/ul/li[1]/a')
            volta_consult.click() 
            time.sleep(2)
            continue
        except NoSuchElementException: 
            pass
            situa = drive.find_element(By.XPATH, '//*[@id="frmConsulta"]/div/table/tbody/tr[1]/td[5]').text
            datasituacao = drive.find_element(By.XPATH,'//*[@id="frmConsulta"]/div/table/tbody/tr[1]/td[6]').text
            tipo_product = drive.find_element(By.XPATH, '//*[@id="frmConsulta"]/div/table/tbody/tr[1]/td[4]').text
            volta_consult = drive.find_element(By.XPATH, '/html/body/center/table/tbody/tr[2]/td/div/ul/li[1]/a')
            volta_consult.click()  #Volta pra opção de consultar e entra em loop
            time.sleep(2)
            contador += 1
            # Criação do arquivo, excel, com os resultados da pesquisa: 

            resultadoss = {'Linha': row['LINHA'], 'Situacao': situa, 'Datasitua':datasituacao, 'TipoProduto':tipo_product}
            listafinal.append(resultadoss)
            df_listafinal = pd.DataFrame(listafinal, columns=['Linha', 'Situacao', 'Datasitua', 'TipoProduto'])
            df_listafinal.to_excel(nome_da_planilha, index=False)
print("Portanto alegra-te, Ó Iniciado, pois quanto maior a tua prova, maior o teu Triunfo.")
